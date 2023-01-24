from util import util
from math import sin, cos, radians

def print_anglefns(fn, fname, start_deg, end_deg, width, length):

    print(' x  ', end='')
    util.char_line('-', width)
    print(' '+fname)

    interval = round((end_deg - start_deg) / length)
    center = int(width / 2) + 1

    for i in range(start_deg, end_deg + interval, interval):
        prtline = [' ' for i in range(width)]
        val = round(fn(radians(i)), 4)
        loc = min(int((val + 1) * width / 2) + 1, width)
        prtline[center - 1] = '|'
        prtline[loc - 1] = '*'
        prtline = ''.join(prtline)
        print(f'{i:0>3} {prtline} {val + 0:>6.3f}')

def main():
    util.print_header('1-4 sine wave print', '2023.01.24', '(c) Lee, Sang-Gwon')
    
    # 필요한 정보 입력
    start_deg = util.int_get('>>> 시작 각도를 입력하세요 : ', minval=0, default=0)
    end_deg   = util.int_get('>>> 종료 각도를 입력하세요 : ', minval=start_deg + 1, default=360)
    width     = util.int_get('>>> 그래프의 폭을 입력하세요 : ', minval=10, default=70)
    length    = util.int_get('>>> 그래프의 길이를 입력하세요 : ', minval=10, default=70)
    fn = util.int_get('>>> 출력할 삼각함수를 선택하세요 (1.sin, 2.cos):', maxval=2, default=1)
        
    if fn == 1:
        print_anglefns(sin, 'sin(x)', start_deg, end_deg, width, length)
    else:
        print_anglefns(cos, 'cos(x)', start_deg, end_deg, width, length)
    
if __name__ == '__main__':
    main()
