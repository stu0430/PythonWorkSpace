from util import util

def make_cipher(plaintext, key):

    ciphertext = ''

    first = ord(' ')
    last = ord('~')

    for ch in plaintext:
        ciphertext += chr((ord(ch) + key - first) % (last - first + 1) + first)
    
    return ciphertext

def main():
    util.print_header('1-2 Caesar cipher', '2022.09.19', '(c) Lee, Sang-Gwon')

    plaintext = input('암호화할 문자을 입력하세요 : ')
    key       = int(input('Caesar Cipher 키값을 입력하세요 : '))
    filename  = input('암호문을 저장할 파일명을 입력하세요 : ')

    ciphertext = make_cipher(plaintext, key)
    print(f'암호화된 문장 : {ciphertext}')

    with open(filename, 'w') as cfile:
        cfile.write(ciphertext)
    print(f'암호문 파일을 저장하였습니다 : {filename}')
    
if __name__ == '__main__':
    main()
