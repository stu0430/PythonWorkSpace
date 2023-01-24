import random
import time
from util import util

NCARDS = 8
INIT_SCORE = 100
SUIT_TUPLE = ('Clubs', 'Diamonds', 'Hearts', 'Spades')  # 값이 큰 순서대로 배치
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

def createDeck():
    deck = []
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLE):
            card = {'suit': suit, 'rank': rank, 'value': value+1}
            deck.append(card)
    return deck

def shuffleCards(deck):
    random.shuffle(deck)
    return deck

def getCards(deck, numCards):
    cardList = []
    for i in range(numCards):
        card = deck.pop()  # 맨 뒤에서 한장 제거
        cardList.append(card)
    return cardList

# 카드 목록을 출력
def printCardList(cardList):
    for i in range(len(cardList)):
        print(f"{i+1}. {cardList[i]['suit']} {cardList[i]['rank']}")

def game1(score):

    print(">>> Higher or Lower 게임(1)을 시작합니다.")
    print(f">>> 현재 점수는 {score}점입니다.")

    deck = createDeck()
    print(">>> 카드를 섞습니다.")
    deck = shuffleCards(deck)
    time.sleep(1)

    print(f">>> {NCARDS}장의 카드를 받습니다.")
    myCardList = getCards(deck, NCARDS)
    time.sleep(1)

    curCard = myCardList.pop()
    print(f">>> 첫번째 카드는 {curCard['suit']}, {curCard['rank']}입니다.")

    for i in range(NCARDS-1):
        while True:
            choice = input("다음 카드 숫자가 더 클지('h'), 작을지('l') 맞춰보세요: ")
            if choice in "hHlL":
                choice = choice.lower()
                break
            else:
                print(">>> [ERROR] 'h' 또는 'l' 중 하나를 입력하세요!!!")

        chStr = 'lower' if choice == 'l' else 'higher'
        print(f">>> 당신은 {chStr}를 선택했습니다.")
        print(">>> 이제 다음 카드를 확인합니다.")
        time.sleep(1)

        nextCard = myCardList.pop()
        print(f">>> 다음 카드는 {nextCard['suit']}, {nextCard['rank']}입니다.")

        if (choice == 'l' and nextCard['value'] < curCard['value']) or \
           (choice == 'h' and nextCard['value'] > curCard['value']):
            print(">>> 당신의 예측이 맞았습니다! 20점을 획득합니다.")
            score += 20
        else:
            print(">>> 당신의 예측이 틀렸습니다! 15점을 잃습니다.")
            score -= 15

        curCard = nextCard

        if i < NCARDS-2:
            print(f">>> 당신의 현재 점수는 {score}점입니다.")
            time.sleep(1)
        else:
            print(f">>> 게임이 끝났습니다. 당신의 최종 점수는 {score}점입니다.")

    return score

def game2(score):

    print(">>> Higher or Lower 게임(2)을 시작합니다.")
    print(f">>> 현재 점수는 {score}점입니다.")

    deck = createDeck()
    print(">>> 카드를 섞습니다.")
    deck = shuffleCards(deck)
    time.sleep(1)

    print(f">>> 당신에게 {NCARDS}장의 카드를 나누어줍니다.")
    myCardList = getCards(deck, NCARDS)
    time.sleep(1)

    print(f">>> 딜러에게 {NCARDS}장의 카드를 나누어줍니다.")
    dealerCardList = getCards(deck, NCARDS)
    time.sleep(1)

    for i in range(NCARDS):

        print(">>> 당신의 현재 카드는 다음과 같습니다.")
        printCardList(myCardList)

        while True:

            if len(myCardList) >= 2:
                choice = input("선택할 카드 번호를 입력하세요: ")
                if str(1) <= choice <= str(len(myCardList)):
                    choice = int(choice)
                    break
                else:
                    print(">>> [ERROR] 목록의 번호를 정확히 입력하세요!!!")
            else:
                choice = 1
                break

        myCard = myCardList.pop(choice-1)
        print(f">>> 당신의 카드는 {myCard['suit']}, {myCard['rank']}입니다.")

        dealerCard = dealerCardList.pop()
        print(f">>> 딜러의 카드는 {dealerCard['suit']}, {dealerCard['rank']}입니다.")

        time.sleep(1)

        if myCard['value'] > dealerCard['value']:
            print(">>> 당신의 카드 숫자가 딜러의 카드 숫자보다 큽니다! 20점을 획득합니다.")
            score += 20
        elif myCard['value'] < dealerCard['value']:
            print(">>> 당신의 카드 숫자가 딜러의 카드 숫자보다 작습니다! 20점을 잃습니다.")
            score -= 20
        elif SUIT_TUPLE.index(myCard['suit']) > SUIT_TUPLE.index(dealerCard['suit']):
            print(">>> 당신과 딜러의 카드 숫자가 같지만 당신 카드가 suit에서 앞섭니다! 20점을 획득합니다.")
            score += 20
        else:
            print(">>> 당신과 딜러의 카드 숫자가 같지만 당신 카드가 suit에서 뒤집니다! 20점을 잃습니다.")
            score -= 20

        if i < NCARDS-1:
            print(f">>> 당신의 현재 점수는 {score}점입니다.")
            time.sleep(1)
        else:
            print(f">>> 게임이 끝났습니다. 당신의 최종 점수는 {score}점입니다.")

    return score

def main():
    util.print_header("2-2 Higher or Lower", "2022.09.27", "(c) Lee, Sang-gwon")

    score = INIT_SCORE

    while True:
        game_num = util.int_get('>>> 게임 유형을 선택하세요(1.개인게임, 2.딜러대결, 3.종료):', minval=1, maxval=3, default=1)

        if game_num == 1:
            score = game1(score)
        elif game_num == 2:
            score = game2(score)
        else:
            print(f">>> 당신의 최종 점수는 {score}점입니다. 게임을 종료합니다.\n")
            break

if __name__ == '__main__':
    main()
