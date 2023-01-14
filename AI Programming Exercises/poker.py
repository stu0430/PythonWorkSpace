import time
import random
from util import util
from operator import itemgetter

SUIT_TUPLE = ("Clubs", "Diamonds", "Hearts", "Spades")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
INIT_SCORE = 100
MAX_ROUND = 5

def createDeck():
    deck = []
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLE):
            card = {'suit': suit, 'rank': rank, 'value': value + 1, 'attr': 'hidden'}
            deck.append(card)

    return deck

def shuffleCards(deck):
    random.shuffle(deck)
    return deck

def getCard(deck, num=None):
    if num is None:
        card = deck.pop()
    else:
        card = deck.pop(num)
    return card

def handCards(deck, playerCards, player):
    playerCards[player].append(getCard(deck))
    return playerCards

def sortCards(cards, sortBy, rev):
    cards.sort(key=itemgetter(sortBy), reverse=rev)
    return cards

def viewCards(playerCards, player):
    for i, card in enumerate(playerCards[player]):
        card['attr'] = 'open'
        print(f"{i + 1}. {card['suit']} {card['rank']}")

def isFlush(cards):
    cards = sortCards(cards, 'suit', True)

    suit = cards[0]['suit']
    isFlush = False
    
    count = 0
    
    for i in range(len(cards)):
        if cards[i]['suit'] == suit:
            count += 1
        else:
            suit = cards[i]['suit']
            count = 1

    if count >= 5:
        isFlush = True
        high = max([card['value'] for card in cards if card['suit'] == suit])

    if isFlush:
        return high
    else:
        return None

def isStraight(cards):
    cards = sortCards(cards, 'value', False)

    count = 0

    isStraight = False

    for i in range(len(cards) - 1):
        if cards[i + 1]['value'] - cards[i]['value'] == 1:
            count += 1

            if count >= 4:
                isStraight = True
                high = cards[i + 1]['value']
        else:
            count = 0

    if isStraight:
        return high
    else:
        return None

def is4Cards(cards):
    is4Cards = False

    array = [0] * 14

    for i in cards:
        array[i['value']] += 1

    for i in array:
        if i == 4:
            is4Cards = True
            high = array.index(i)
            break

    if is4Cards:
        return high
    else:
        return None

def isTriple(cards):
    isTriple = False

    array = [0] * 14

    for i in cards:
        array[i['value']] += 1

    for i in array:
        if i == 3:
            isTriple = True
            high = array.index(i)
            break

    if isTriple:
        return high
    else:
        return None

def is2Pairs(cards):
    pairCount = 0

    is2Pairs = False

    array = [0] * 14

    for i in cards:
        array[i['value']] += 1

    for i in range(len(array)):
        if array[i] == 2:
            pairCount += 1
            high = i

    if pairCount == 2:
        is2Pairs = True

    if is2Pairs:
        return high
    else:
        return None

def is1Pair(cards):
    pairCount = 0

    is1Pair = False

    array = [0] * 14

    for i in cards:
        array[i['value']] += 1

    for i in range(len(array)):
        if array[i] == 2:
            pairCount += 1
            high = i

    if pairCount == 1:
        is1Pair = True

    if is1Pair:
        return high
    else:
        return None

def isHigh(cards):
    cards = sortCards(cards, 'value', True)
    high = cards[0]['value']
    return high

# 점수 계산 함수
def ranking(playerCards, player):
    
    if isFlush(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 플러시입니다.")
        rankScore = 6
        highScore = isFlush(playerCards[player])
        
    elif isStraight(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 스트레이트입니다.")
        rankScore = 5
        highScore = isStraight(playerCards[player])
        
    elif is4Cards(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 포카드입니다.")
        rankScore = 4
        highScore = is4Cards(playerCards[player])
        
    elif isTriple(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 트리플입니다.")
        rankScore = 3
        highScore = isTriple(playerCards[player])
            
    elif is2Pairs(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 2페어입니다.")
        rankScore = 2
        highScore = is2Pairs(playerCards[player])
        
    elif is1Pair(playerCards[player]) is not None:
        print(f">>> {player}의 카드는 1페어입니다.")
        rankScore = 1
        highScore = is1Pair(playerCards[player])
        
    else:
        print(f">>> {player}의 카드는 하이 카드입니다.")
        rankScore = 0
        highScore = isHigh(playerCards[player])
        
    return rankScore, highScore

def poker(score):
    
    deck = createDeck()
    print(">>> 카드를 섞습니다.")
    deck = shuffleCards(deck)
    time.sleep(1)
    
    playerCards = {'player' : [], 'dealer' : []}

    print(">>> 플레이어에게 2장의 카드를 나누어줍니다.")
    for i in range(2):
        handCards(deck, playerCards, 'player')
        playerCards['player'][i]['attr'] = 'open'
    time.sleep(1)

    print(">>> 딜러에게 2장의 카드를 나누어줍니다.")
    for i in range(2):
        handCards(deck, playerCards, 'dealer')
        playerCards['dealer'][i]['attr'] = 'open'
    time.sleep(1)

    print(">>> 플레이어의 카드를 확인합니다.")
    time.sleep(1)
    viewCards(playerCards, 'player')

    print(">>> 딜러의 카드를 확인합니다.")
    time.sleep(1)
    viewCards(playerCards, 'dealer')

    goCount = 0
    
    while True:
        
        choice = util.getChar(">>> Drop(d) 또는 Go(g)를 선택하세요 : ", "DdGg")

        if choice == 'g':
            goCount += 1
            print(">>> Go를 선택하셨습니다.")
            
            if goCount == 6:
                print(">>> 플레이어의 카드를 공개합니다.")
                viewCards(playerCards, 'player')
                time.sleep(1)
                playerRankScore, playerHighScore = ranking(playerCards, 'player')
                
                print(">>> 딜러의 카드를 공개합니다.")
                viewCards(playerCards, 'dealer')
                time.sleep(1)
                dealerRankScore, dealerHighScore = ranking(playerCards, 'dealer')
                
                time.sleep(1)

                if playerRankScore > dealerRankScore:
                    print(">>> 플레이어의 승리입니다. 100점을 획득합니다.")
                    score += 100

                elif playerRankScore < dealerRankScore:
                    print(">>> 딜러의 승리입니다. 100점을 잃습니다.")
                    score -= 100

                else:
                    if playerHighScore > dealerHighScore:
                        print(">>> 플레이어의 승리입니다. 100점을 획득합니다.")
                        score += 100

                    elif playerHighScore < dealerHighScore:
                        print(">>> 딜러의 승리입니다. 100점을 잃습니다.")
                        score -= 100

                    else:
                        print(">>> 무승부입니다.")
                        
                break
                        
            else:
                print(">>> 플레이어에게 1장의 카드를 나누어줍니다.")
                handCards(deck, playerCards, 'player')
                time.sleep(1)
                
                print(f">>> 받은 카드는 {playerCards['player'][-1]['suit']} {playerCards['player'][-1]['rank']} 입니다.")
                
                print(">>> 딜러에게 1장의 카드를 나누어줍니다.")
                handCards(deck, playerCards, 'dealer')
                time.sleep(1)
            
        else:
            print(">>> Drop을 선택하셨습니다.")
            print(f">>> {10 * (goCount + 1)}점을 잃습니다.")
            score -= 10 * (goCount + 1)
            break
        
    return score

def main():
    util.print_header("2-3 Poker game", "2022.11.04", "(c) Lee, Sang-gwon")
    
    score = INIT_SCORE
    gameRound = MAX_ROUND

    while True:
        menuSel = util.int_get('메뉴를 선택하세요(1.게임 시작  2.종료):', minval=1, maxval=2, default=1)

        if menuSel == 1:
            for i in range(gameRound):
                print(f">>> {i + 1}번째 게임을 시작합니다.")
                score = poker(score)
                print(f">>> 현재 점수는 {score}점입니다.\n")
        else:
            print(f">>> 당신의 최종 점수는 {score}점입니다. 게임을 종료합니다.")
            break
        
if __name__ == "__main__":
    main()