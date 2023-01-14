import sys, time
import keyboard, term
from util import util

BOARD_SIZE = 19
WHITE = chr(0x25CB)
BLACK = chr(0x25CF)
PLAYERS = [WHITE, BLACK]

def getKey(row, col):

    enter = False

    while True:

        if keyboard.is_pressed('up'):
            if row != 0:
                row -= 1
                time.sleep(0.2)
                break
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('down'):
            if row != BOARD_SIZE - 1:
                row += 1
                time.sleep(0.2)
                break
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('left'):
            if col != 0:
                col -= 1
                time.sleep(0.2)
                break
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('right'):
            if col != BOARD_SIZE - 1:
                col += 1
                time.sleep(0.2)
                break
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('q'):
            sys.exit()

        elif keyboard.is_pressed('enter'):
            enter = True
            time.sleep(0.2)
            break

    return enter, row, col

def newBoard(starPoint=True):
    board = [['.' for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]

    if starPoint and BOARD_SIZE >= 9 and BOARD_SIZE % 2 == 1:

        starPoints = [BOARD_SIZE // 2 - BOARD_SIZE // 3,
                      BOARD_SIZE // 2,
                      BOARD_SIZE // 2 + BOARD_SIZE // 3]

        for row in starPoints:
            for col in starPoints:
                board[row][col] = '+'

    return board

def displayBoard(board, cusPos):
    print('+'.ljust(2) + '-'.ljust(2) * BOARD_SIZE + '+')

    for i in range(BOARD_SIZE):
        print('|', end=' ')
        for j in range(BOARD_SIZE):
            if (i, j) == cusPos:
                print(f'{term.black + term.bgwhite + board[i][j] + term.off}', end=' ')
            else:
                print(f'{board[i][j]}', end=' ')
        print('|')

    print('+'.ljust(2) + '-'.ljust(2) * BOARD_SIZE + '+')
    print(f'>>> 현재 위치 : {cusPos[0]}행 {cusPos[1]}열')

def isOmok(playerTile, board):
    # 각 열에 대해서 각 줄에 수평으로 5개가 연속인지 확인
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE - 4):
            tile1 = board[col][row]
            tile2 = board[col + 1][row]
            tile3 = board[col + 2][row]
            tile4 = board[col + 3][row]
            tile5 = board[col + 4][row]

            if tile1 == tile2 == tile3 == tile4 == tile5 == playerTile:
                return True

    # 각 열에 대해서 각 줄에 수직으로 5개가 연속인지 확인
    for row in range(BOARD_SIZE - 4):
        for col in range(BOARD_SIZE):
            tile1 = board[col][row]
            tile2 = board[col][row + 1]
            tile3 = board[col][row + 2]
            tile4 = board[col][row + 3]
            tile5 = board[col][row + 4]

            if tile1 == tile2 == tile3 == tile4 == tile5 == playerTile:
                return True

    # 각 열에 대해서 오른쪽 아래 대각선으로 5개가 연속인지 확인
    for row in range(BOARD_SIZE - 4):
        for col in range(BOARD_SIZE - 4):
            tile1 = board[col][row]
            tile2 = board[col + 1][row + 1]
            tile3 = board[col + 2][row + 2]
            tile4 = board[col + 3][row + 3]
            tile5 = board[col + 4][row + 4]

            if tile1 == tile2 == tile3 == tile4 == tile5 == playerTile:
                return True

    # 각 열에 대해서 왼쪽 아래 대각선으로 5개가 연속인지 확인
    for row in range(BOARD_SIZE - 4):
        for col in range(BOARD_SIZE - 1, 3, -1):
            tile1 = board[col][row]
            tile2 = board[col - 1][row + 1]
            tile3 = board[col - 2][row + 2]
            tile4 = board[col - 3][row + 3]
            tile5 = board[col - 4][row + 4]

            if tile1 == tile2 == tile3 == tile4 == tile5 == playerTile:
                return True

    return False

def isFull(board):
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            if board[col][row] == '.' or board[col][row] == '+':
                return False

    return True

def main():
    util.print_header("Omok game", "2022.12.13", "(c) Lee, Sang-gwon")

    gameBoard = newBoard()

    player = PLAYERS[0]

    cusPos = (BOARD_SIZE // 2, BOARD_SIZE // 2)

    print(f'>>> Player {player}가 먼저 시작합니다.')
    print('>>> 방향키로 위치를 선택하고 Enter키를 누르세요.')
    print('>>> Q를 누르면 게임이 종료됩니다.')

    while True:
        displayBoard(gameBoard, cusPos)

        enter, row, col = getKey(*cusPos)

        cusPos = (row, col)

        if enter:
            gameBoard[row][col] = player

            displayBoard(gameBoard, cusPos)

            if isOmok(player, gameBoard):
                print(f'Player {player}가 이겼습니다!')
                break

            elif isFull(gameBoard):
                print('비겼습니다!')
                break

            player = PLAYERS[1] if player == PLAYERS[0] else PLAYERS[0]

if __name__ == '__main__':
    main()
