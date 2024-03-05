#! /bin/python
import argparse

parser=argparse.ArgumentParser(
    description='''Provide the size of the square board you want and the number of times the knight can move.
      The scrypt will show what squares the knight can move to in the given number of moves.''',
    epilog="""epilog""")
parser.add_argument('--foo', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args=parser.parse_args()

import sys

if len(sys.argv) > 3:
    print("Too many arguements.")

board_size = 11
waves = 1
if len(sys.argv) > 1:
    board_size = int(sys.argv[1])
if len(sys.argv) > 2:
    waves = int(sys.argv[2])

board = [['_' for i in range(board_size)] for j in range(board_size)]
marks = []
start_pos = (board_size//2, board_size//2)
board[start_pos[0]][start_pos[1]] = 'O'

def PrintBoard():
    for i in range(len(board)):
        print(board[i], '\n')

def MarkDestinations(origin_pos):
    row = origin_pos[0]
    column = origin_pos[1]
    destinations = [(row-2, column-1), (row-2, column+1), 
                    (row+2, column-1), (row+2, column+1), 
                    (row-1, column-2), (row+1, column-2), 
                    (row-1, column+2), (row+1, column+2)
    ]
    for dest_pos in destinations:
        dest_row, dest_column = dest_pos
        if 0 <= dest_row < len(board) and 0 <= dest_column < len(board[0]):
            board[dest_row][dest_column] = 'X'    
            #AddMarks(dest_pos)

#def AddMarks(new_pos):
#    new = True
#    for pos in marks:
#        if new_pos == pos:
#            new = False
#    if new:
#        marks.append(new_pos)

def FindMarks():
    marks = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'X' or board[i][j] == 'O':
                pos = (i,j)
                marks.append(pos)
    return(marks)

def SpreadMarks():
    marks = FindMarks()
    for pos in marks:
        MarkDestinations(pos)
        

PrintBoard()
for i in range(waves):
    print("Wave Number: ", i+1)
    SpreadMarks()
    PrintBoard()

