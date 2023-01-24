import random, sys
import keyboard, time
from util import util

BLANK = '  '

def getNewBoard():
    board = [[row + col * 4 for col in range(4)] for row in range(1, 5)]

    board[3][3] = BLANK

    return board

def displayBoard(board):

    board = list(map(list, zip(*board)))
    labels = [str(element).rjust(2) for array in board for element in array]

    print('''
          +------+------+------+------+
          |      |      |      |      |
          |  {}  |  {}  |  {}  |  {}  |
          |      |      |      |      |
          +------+------+------+------+
          |      |      |      |      |
          |  {}  |  {}  |  {}  |  {}  |
          |      |      |      |      |
          +------+------+------+------+
          |      |      |      |      |
          |  {}  |  {}  |  {}  |  {}  |
          |      |      |      |      |
          +------+------+------+------+
          |      |      |      |      |
          |  {}  |  {}  |  {}  |  {}  |
          |      |      |      |      |
          +------+------+------+------+
          '''.format(*labels))

def findBlankSpace(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == BLANK:
                return row, col

def askForPlayerMove(board):
    blankX, blankY = findBlankSpace(board)
    response = None

    print('>>> 방향키 또는 "Q"를 입력하세요 : ', end='')

    while True:

        if keyboard.is_pressed('up'):
            if blankY != 3:
                response = 'U'
                time.sleep(0.2)
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('down'):
            if blankY != 0:
                response = 'D'
                time.sleep(0.2)
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('left'):
            if blankX != 3:
                response = 'L'
                time.sleep(0.2)
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('right'):
            if blankX != 0:
                response = 'R'
                time.sleep(0.2)
            else:
                print('잘못된 이동입니다!')
                break

        elif keyboard.is_pressed('q'):
            sys.exit()

        if response != None:
            print(response)
            break

    return response

def makeMove(board, move):
    b_x, b_y = findBlankSpace(board)

    if move == 'U':
        board[b_x][b_y], board[b_x][b_y + 1] = board[b_x][b_y + 1], board[b_x][b_y]
    if move == 'D':
        board[b_x][b_y], board[b_x][b_y - 1] = board[b_x][b_y - 1], board[b_x][b_y]
    if move == 'L':
        board[b_x][b_y], board[b_x + 1][b_y] = board[b_x + 1][b_y], board[b_x][b_y]
    if move == 'R':
        board[b_x][b_y], board[b_x - 1][b_y] = board[b_x - 1][b_y], board[b_x][b_y]

def makeRandomMove(board):
    blank_x, blank_y = findBlankSpace(board)

    valid_moves = []

    if blank_y != 3:
        valid_moves.append('U')
    if blank_y != 0:
        valid_moves.append('D')
    if blank_x != 3:
        valid_moves.append('L')
    if blank_x != 0:
        valid_moves.append('R')

    makeMove(board, random.choice(valid_moves))

def getNewPuzzle(moves=200):
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)

    return board

def main():
    util.print_header('Slide Puzzle', '2023.01.24', '(c) Lee, Sang-gwon')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)

        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            displayBoard(gameBoard)
            print('퍼즐이 완성되었습니다!')
            sys.exit()

if __name__ == '__main__':
    main()