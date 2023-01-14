from util import util

def int_get(input_str, minval=-15, maxval=None, default=None):

    while True:
        val = input(f'{input_str}[{str(default)}] ')
        if val == '' and default is not None:
            return default
        elif set(val) <= set("-0123456789"):
            val = int(val)
            if maxval is not None:
                if minval <= val <= maxval:
                    return val
                else:
                    print(">>> [ERROR] 입력값이 범위를 벗어났습니다!")
            else:
                if minval <= val:
                    return val
                else:
                    print(">>> [ERROR] 입력값이 범위를 벗어났습니다!")
        else:
            print(">>> [ERROR] 정수를 입력해주세요!")
            
def print_fn(fn, x_min, x_max, y_min, y_max, width, heigth):
    
    # x, y의 범위
    x_range = x_max - x_min  
    y_range = y_max - y_min  

    # x축, y축의 간격
    x_interval = round(width / x_range)  
    y_interval = round(heigth / y_range)  

    # 그래프를 저장할 2차원 배열
    graph = [[' '] * width for i in range(heigth)]

    # x = 0 위치 계산
    x_zero = round(-x_min * x_interval)
    # y축 그리기
    if x_zero >= 0 and x_zero < width:
        for i in range(heigth):
            graph[i][x_zero] = '|'
    
    # y축이 그려진 경우
    if '|' in graph[-1] and graph[-1][0] != '|':
        graph[-1][x_zero-1] = 'y'  

    # y = 0 위치 계산
    y_zero = round(-y_min * y_interval)
    # x축 그리기
    if y_zero >= 0 and y_zero < heigth:
        for j in range(width):
            graph[y_zero][j] = '-' 
    
    # x축이 그려진 경우 
    if '-' in graph[y_zero] and graph[y_zero] != graph[-1]:
        graph[y_zero-1][-1] = 'x'  

    # 원점 찍기
    if x_zero >= 0 and x_zero < width and y_zero >= 0 and y_zero < heigth:
        graph[y_zero][x_zero] = 'o'
        graph[y_zero-1][x_zero-1] = '0'
        
    # 함수 찍기
    for i in range(heigth):
        for j in range(width):
            x = (j - x_zero) / x_interval
            y = fn(x)
            if round(y * y_interval) == i - y_zero:
                graph[i][j] = '*'

    # 그래프 출력
    for i in reversed(range(heigth)):
        print(''.join(graph[i]))

def main():
    
    util.print_header("1-5 Printing functions", "2022.10.17", "(c) Lee, Sang-gwon")
    
    fns = ['x - 3', '-x^2 - 3x + 2', 'x^3 - 2x^2 - 5']
    
    for i, fn in enumerate(fns):
        print(f"{i + 1}. {fn}")
        
    fn_sel    = int_get('출력할 함수 번호를 선택하세요 : ', minval=1, maxval=3, default=1)
    x_min     = int_get('x의 최솟값을 입력하세요 :', minval=-15, default=-10)
    x_max     = int_get('x의 최댓값을 입력하세요 :', minval=x_min+3, maxval=15, default=10)
    y_min     = int_get('y의 최솟값을 입력하세요 :', minval=-15, default=-10)
    y_max     = int_get('y의 최댓값을 입력하세요 :', minval=y_min+3, maxval=15, default=10)
    gr_width  = int_get('그래프의 폭을 입력하세요 :', minval=20, default=70)
    gr_heigth = int_get('그래프의 높이를 입력하세요 :', minval=20, default=70)

    if fn_sel == 1:
        print_fn(lambda x: x - 3, x_min, x_max, y_min, y_max, gr_width, gr_heigth)
    elif fn_sel == 2:
        print_fn(lambda x: -x**2 - 3*x + 2, x_min, x_max, y_min, y_max, gr_width, gr_heigth)
    else:
        print_fn(lambda x: x**3 - 2*x**2 - 5, x_min, x_max, y_min, y_max, gr_width, gr_heigth)

if __name__ == '__main__':
    main()
