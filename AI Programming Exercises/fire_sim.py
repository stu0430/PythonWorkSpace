import random, time, sys, bext

WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5

def create_new_forest():
    # forest 공간 만들기
    forest = {'width': WIDTH, 'height': HEIGHT}

    # 초기 나무 할당
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest

def display_forest(forest):
    # 화면 좌측 상단으로 이동
    bext.goto(0, 0)

    # 화면 공간에 나무, 화재 표시
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            else:
                print(EMPTY, end='')
        print()

    bext.fg('reset')

    # 안내 정보 등 추가 표시
    print(f'나무가 자랄 확률 : {GROW_CHANCE * 100}%')
    print(f'산불이 날 확률 : {FIRE_CHANCE * 100}%')
    
def main():
    forest = create_new_forest()
    bext.clear()
    
    while True:
        display_forest(forest)
        
        next_forest = {'width' : forest['width'], 'height' : forest['height']}
        
        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in next_forest:
                    continue
                
                if forest[(x, y)] == EMPTY:
                    if random.random() <= GROW_CHANCE:
                        next_forest[(x, y)] = TREE
                    else:
                        next_forest[(x, y)] = EMPTY
                        
                elif forest[(x, y)] == TREE:
                    if random.random() <= FIRE_CHANCE:
                        next_forest[(x, y)] = FIRE
                    else:
                        next_forest[(x, y)] = TREE
                    
                elif forest[(x, y)] == FIRE:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < forest['width'] and 0 <= y + j < forest['height']:
                                if forest[(x + i, y + j)] == TREE:
                                    next_forest[(x + i, y + j)] = FIRE
                    
                    # if x - 1 >= 0 and forest[(x - 1, y)] == TREE:    
                    #     next_forest[(x - 1, y)] = FIRE  
                    # if x + 1 < forest['width'] and forest[(x + 1, y)] == TREE:
                    #     next_forest[(x + 1, y)] = FIRE
                    # if y - 1 >= 0 and forest[(x, y - 1)] == TREE:
                    #     next_forest[(x, y - 1)] = FIRE
                    # if y + 1 < forest['height'] and forest[(x, y + 1)] == TREE:
                    #     next_forest[(x, y + 1)] = FIRE   
                    
                    next_forest[(x, y)] = EMPTY
                    
                else:
                    # next_forest[(x, y)] = forest[(x, y)]
                    pass
                
        forest = next_forest
        time.sleep(PAUSE_LENGTH)

if __name__ == '__main__':
    main()
