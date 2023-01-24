import os
import operator
from util import util

def make_cipher(plaintext, key):

    ciphertext = ''

    first = ord(' ')
    last = ord('~')

    for ch in plaintext:
        ciphertext += chr((ord(ch) + key - first) % (last - first + 1) + first)

    return ciphertext

def make_freqlist(input_text):
    alpha_freq = dict()
    
    for i in range(32, 127):
        alpha_freq[chr(i)] = 0
    
    for i in input_text:
        alpha_freq[i] += 1
        
    freq_list = sorted(alpha_freq.items(), key=operator.itemgetter(1), reverse=True)
    
    return freq_list

def main():
    util.print_header('1-3 Caesar Decipher', '2022.09.21', '(c) Lee, Sang-Gwon')
    
    cipher_file = input('>>> 암호문 파일명을 입력하세요 : ')
    
    if not os.path.isfile(cipher_file):
        print('>>> [ERROR] 암호문 파일이 존재하지 않습니다!')
    else:
        with open(cipher_file, 'r') as cfile:
            ciphertext = cfile.readline()
            print(f'암호문 : {ciphertext}')
    
    lst = [' ', 'e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c']
    
    freqlist = make_freqlist(ciphertext)
    
    mfreq_ch = freqlist[0][0]
    
    for i in range(len(lst)):
        diff = ord(mfreq_ch) - ord(lst[i])
        plaintext = make_cipher(ciphertext, -diff)
        print(f'{i + 1}번째 해독문 : {plaintext}')

if __name__ == '__main__':
    main()
