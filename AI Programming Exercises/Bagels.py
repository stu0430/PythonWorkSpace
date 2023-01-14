from random import shuffle
from util import header

MAX_GUESSES = 10
NUM_DIGITS = 3

def getSecretNum():

    numList = list('0123456789')
    shuffle(numList)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numList[i])

    return secretNum

def getGuessNum():
    while True:
        rightNum = True
        getNum = input(f'>>> {str(NUM_DIGITS)}자리 추측 숫자를 입력하세요 : ')

        if len(getNum) != NUM_DIGITS:
            print(f'>>> [ERROR] 자릿수가 {str(NUM_DIGITS)}이 아닙니다.')
            rightNum = False

        if not set(getNum) <= set("0123456789"):
            print('>>> [ERROR] 숫자가 아닌 문자가 있습니다.')
            rightNum = False

        if rightNum:
            break
        
    return getNum

def getGuessResult(secret, guess):

    pico = 0
    fermi = 0

    if secret == guess:
        result = 'Bingo!'

    elif set(secret) & set(guess) == set():
        result = 'Bagels'

    else:
        result = ''

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                fermi += 1
            elif guess[i] in secret:
                pico += 1

        for i in range(pico):
            result += 'Pico '

        for i in range(fermi):
            result += 'Fermi '

    return result

def main():
    header.header_print("2-1 Bagels Game", "2022.10.12", "(c) Lee, Sang-gwon")
    
    print(f'\n>>> {MAX_GUESSES}번의 기회가 주어집니다.')
    secretNum = getSecretNum()
    
    for i in range(MAX_GUESSES):
        guessNum = getGuessNum()
        result = getGuessResult(secretNum, guessNum)
        print(result)
        
        if result == 'Bingo!':
            print('>>> 축하합니다! 프로그램을 마칩니다.')
            break
        else:
            if i < MAX_GUESSES - 1:
                print(f'>>> 이제 {MAX_GUESSES - i - 1}번의 기회가 남았습니다.')
            else:
                print(f'>>> 아쉽네요. 정답은 {secretNum}입니다.')                 

if __name__ == '__main__':
    main()