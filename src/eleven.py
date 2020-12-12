import os
import re
import sys
import math
import itertools
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_eleven_data')

EXPECTED_LINES = 90

def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    for i in range(len(instructions)):
        instructions[i] = list(instructions[i])

    return instructions

# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
        

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
answer = """
##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
test_input = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

def eleven_part_one(puzzle_input, part_two = False):
    count = 0
    different = True
    
    new_layout = []
    x = len(puzzle_input)
        
    for i in range(x):
        new_line = (puzzle_input[i]).copy()
        new_layout.append(new_line)

    while different == True:
        new_layout, different = update(new_layout, part_two)
        # print("NEW: {}".format(listToString(new_layout[4])))
        count = count + 1
        
    
    
    occupied = 0
    for i in range(x):
        occupied = occupied + new_layout[i].count('#')
    return occupied
    
    

def update(puzzle_input, part_two = False):
    new_layout = []
    
    x = len(puzzle_input[0])
    y = len(puzzle_input)
    
    for i in range(y):
        new_line = (puzzle_input[i]).copy()
        new_layout.append(new_line)
    different = False
    for i in range(y):
        for j in range(x):
            if part_two:
                adj = get_adjacent_part_two(i, j, puzzle_input)
            else:
                adj = get_eight_adjacent(i, j, puzzle_input)
            seat = puzzle_input[i][j]
            if part_two:
                new_seat = get_new_seat_part_two(seat, adj)
            else:
                new_seat = get_new_seat(seat, adj)
            new_layout[i][j] = new_seat
            if new_seat != seat:
                different = True
        # print("OLD: {}".format(listToString(puzzle_input[i])))
        # print("NEW: {}".format(listToString(new_layout[i])))
        # print("ANS: {}".format(listToString(answer_list_p2[i])))
        # assert new_layout[i].sort() == answer_list_p2[i].sort()
    
    # print("################")
    # for i in range(x):
    #     print("NEW: {}".format(listToString(new_layout[i])))        
    return new_layout, different
    
def get_new_seat(seat, adj):
    new_seat = seat
    if (seat == 'L') and (adj.count('#') == 0):
        new_seat = '#'
    elif (seat == '#') and (adj.count('#') >= 4):
        new_seat = 'L'
    return new_seat

def get_new_seat_part_two(seat, adj):
    new_seat = seat
    if (seat == 'L') and (adj.count('#') == 0):
        new_seat = '#'
    elif (seat == '#') and (adj.count('#') >= 5):
        new_seat = 'L'
    return new_seat


def get_adjacent_part_two(x, y, puzzle_input):
    adjacents = []
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    # print("width: {}, height: {}".format(width, height))
    # print("x: {}, y: {}".format(x, y))
    if x != 0:
        # row up
        s = puzzle_input[x-1][y]
        a = x-2
        while (s == '.') and (a >= 0):
            s = puzzle_input[a][y]
            a = a - 1
        adjacents.append(s)
        if y != 0:
            s = puzzle_input[x-1][y-1]
            a = x-2
            b = y-2
            while (s == '.') and (a >= 0) and (b >= 0):
                s = puzzle_input[a][b]
                a = a - 1
                b = b - 1
            adjacents.append(s)
        if y != width-1:
            s = puzzle_input[x-1][y+1]
            a = x-2
            b = y+2
            while (s == '.') and (a >= 0) and (b <= (width - 1)):
                s = puzzle_input[a][b]
                a = a - 1
                b = b + 1
            adjacents.append(s)
            
    
    if y != 0:
        s = puzzle_input[x][y-1]
        b = y-2
        while (s == '.') and (b >= 0):
            s = puzzle_input[x][b]
            b = b - 1
        adjacents.append(s)
    if y != width-1:
        s = puzzle_input[x][y+1]
        b = y+2
        while (s == '.') and (b <= (width -1)):
            s = puzzle_input[x][b]
            b = b + 1
        adjacents.append(s)
        
    
    if x != height-1:
        s = puzzle_input[x+1][y]
        a = x+2
        while (s == '.') and (a <= (height - 1)):
            s = puzzle_input[a][y]
            a = a + 1
        adjacents.append(s)
        if y != 0:
            s = puzzle_input[x+1][y-1]
            a = x+2
            b = y-2
            while (s == '.') and (a <= (height-1)) and (b >= 0):
                s = puzzle_input[a][b]
                a = a + 1
                b = b - 1
            adjacents.append(s)
        if y != width-1:
            s = puzzle_input[x+1][y+1]
            a = x+2
            b = y+2
            while (s == '.') and (a <= (height-1)) and (b <= (width-1)):
                s = puzzle_input[a][b]
                a = a + 1
                b = b + 1
            adjacents.append(s)
            
    
    return adjacents


def get_eight_adjacent(x, y, puzzle_input):
    adjacents = []
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    # print("width: {}, height: {}".format(width, height))
    # print("x: {}, y: {}".format(x, y))
    if x != 0:
        adjacents.append(puzzle_input[x-1][y])
        if y != 0:
            adjacents.append(puzzle_input[x-1][y-1])
        if y != width-1:
            adjacents.append(puzzle_input[x-1][y+1])
    
    if y != 0:
        adjacents.append(puzzle_input[x][y-1])
    if y != width-1:
        adjacents.append(puzzle_input[x][y+1])
    
    if x != height-1:
        adjacents.append(puzzle_input[x+1][y])
        if y != 0:
            adjacents.append(puzzle_input[x+1][y-1])
        if y != width-1:
            adjacents.append(puzzle_input[x+1][y+1])
    
    return adjacents
        




test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

answer = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

answer_p2 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""


test_list = [list(y) for y in ((x.strip()) for x in test_input.splitlines())]
answer_list = [list(y) for y in ((x.strip()) for x in answer.splitlines())]
answer_list_p2 = [list(y) for y in ((x.strip()) for x in answer_p2.splitlines())]
# print(test_list)
# print(eleven_part_one(test_list))

puzzle_input = get_instructions()
# print(eleven_part_one(puzzle_input))
#2108

print(eleven_part_one(test_list, part_two=True))
print(eleven_part_one(puzzle_input, part_two=True))
#1897