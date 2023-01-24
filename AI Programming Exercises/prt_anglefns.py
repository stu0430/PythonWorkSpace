from util import util
from math import sin, cos, radians

# sin, cos 값 출력 함수
def print_graph(fn, width, start_deg): 
    # 각도 출력
    print("%0.3d" % start_deg, end='')
    
    # 좌우측 공백
    left_half = round((width - 1) / 2)
    right_half = width - left_half
    
    # 각도를 통한 sin 값 계산
    if fn == 'sin':
        value = round(sin(radians(start_deg)), 3)
    # 각도를 통한 cos 값 계산
    elif fn == 'cos':
        value = round(cos(radians(start_deg)), 3)
    # sin, cos 값의 위치
    loc = round(((value + 1) * (width // 2)))
    
    # sin, cos 값이 양수일 때
    if value > 0:
        util.char_line(' ', left_half)
        print('|', end='')
        util.char_line(' ', loc - 1 - left_half - 1)
        print('*', end='')
        util.char_line(' ', width - loc + 2)
    
    # sin, cos 값이 음수일 때    
    elif value < 0:
        util.char_line(' ', loc)
        print('*', end='')
        util.char_line(' ', left_half - loc - 1)
        print('|', end='')
        util.char_line(' ', right_half)
        
    # sin, cos 값이 0일 때
    else :
        if str(value)[0] == '-':
            util.char_line(' ', left_half)
            print('*', end='')
            util.char_line(' ', right_half)
        else:
            util.char_line(' ', left_half)
            print('*', end='')
            util.char_line(' ', right_half + 1)
    
    # 각도에 따른 sin, cos 값 출력
    print("%.3f" % value)

# 사인파, 코사인파 전체 출력 함수
def print_anglefns(fn, start_deg, end_deg, width, length):
    for i in range(length):
        if start_deg  == end_deg:
            break
        else:
            print_graph(fn, width, start_deg)
            start_deg += 10

def main():
    util.print_header('1-4 sine wave print', '2022.09.21', '(c) Lee, Sang-Gwon')
    
    # 필요한 정보 입력
    start_deg = int(input('시작 각도를 입력하세요 : '))
    end_deg = int(input('종료 각도를 입력하세요 : '))
    width = int(input('그래프의 폭을 입력하세요 : '))
    length = int(input('그래프의 길이를 입력하세요 : '))
    fn = input('sin과 cos 중 그래프를 그릴 유형을 입력하세요 : ')
    
    # 사인파, 코사인파 출력          
    print(' x', end=' ')
    util.char_line('-', width)
    print(f' {fn}(x)')
    print_anglefns(fn, start_deg, end_deg, width, length)
    
if __name__ == '__main__':
    main()
