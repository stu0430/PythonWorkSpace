import sys
from util import util

EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')

def getNewBoard():
    board = {}

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            board[(col, row)] = EMPTY_SPACE

    return board

def displayBoard(board):
    tileChars = []

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            tileChars.append(board[(col, row)])

    print('''
           1234567
          +-------+
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          +-------+'''.format(*tileChars))

def askForPlayerChoice(playerTile, board):

    while True:
        print(f'Player {playerTile}: 1부터 {BOARD_WIDTH}까지, 또는 "Q"를 입력하세요')
        response = input('>>> ').upper().strip()

        if response == 'Q':
            print('>>> 게임을 종료합니다.')
            sys.exit()

        elif response not in COLUMN_LABELS:
            print('>>> 잘못 입력했습니다. 다시 입력해 주세요.')
            continue

        col = int(response) - 1

        if board[col, 0] != EMPTY_SPACE:
            print('>>> 해당 열은 가득 찼습니다. 다시 입력해 주세요.')
            continue

        for row in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(col, row)] == EMPTY_SPACE:
                return col, row

def isWinner(playerTile, board):
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            tile1 = board[(col, row)]
            tile2 = board[(col + 1, row)]
            tile3 = board[(col + 2, row)]
            tile4 = board[(col + 3, row)]

            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH):
            tile1 = board[(col, row)]
            tile2 = board[(col, row + 1)]
            tile3 = board[(col, row + 2)]
            tile4 = board[(col, row + 3)]

            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for row in range(BOARD_HEIGHT - 3):
       for col in range(BOARD_WIDTH - 3):
           tile1 = board[(col, row)]
           tile2 = board[(col + 1, row + 1)]
           tile3 = board[(col + 2, row + 2)]
           tile4 = board[(col + 3, row + 3)]

           if tile1 == tile2 == tile3 == tile4 == playerTile:
               return True

    for row in range(BOARD_HEIGHT - 3):
       for col in range(BOARD_WIDTH - 1, 2, -1):
           tile1 = board[(col, row)]
           tile2 = board[(col - 1, row + 1)]
           tile3 = board[(col - 2, row + 2)]
           tile4 = board[(col - 3, row + 3)]

           if tile1 == tile2 == tile3 == tile4 == playerTile:
               return True

    return False

def isFull(board):
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT):
            if board[(col, row)] == EMPTY_SPACE:
                return False

    return True

def main():
    util.print_header('Four in a row', '2023.01.24', '(c) Lee, Sang-gwon')
    
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:
        displayBoard(gameBoard)

        playerMove = askForPlayerChoice(playerTurn, gameBoard)

        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print(f'>>> Player {playerTurn}가 이겼습니다!')
            break

        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print(f'>>> 비겼습니다!')
            break

        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O

        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X

if __name__ == '__main__':
    main()