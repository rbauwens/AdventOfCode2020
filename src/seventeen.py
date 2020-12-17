import os
import re
import sys
import math
import itertools

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_seventeen_data')

EXPECTED_LINES = 570

def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append((line.strip()))
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions

def seventeen_part_one(puzzle_input):
  # [0,0] [0,1]
  # [1,0] [1,1]
  new_array = puzzle_input.copy()
  across = len(puzzle_input[0])
  down = len(puzzle_input)
  for i in range(down):
    for j in range(across):
      nbor = get_neighbours(i, j, puzzle_input)
      active_nbo = get_active_nbo(nbor, puzzle_input)
      new_state = get_new_state(active_nbo, puzzle_input[i][j])
      new_array[i][j] = new_state

def get_neighbours(i, j, puzzle_input):
  k = 1
  starting_point = [i, j, k]
  neighbours = []
  nb_list = list(itertools.product([-1,0,1], repeat=3)) 
  for entry in nb_list:
    list_entry = list(entry)
    nbo = [a + b for a, b in zip(list_entry, starting_point)] 
    neighbours.append(nbo)
  neighbours.remove(starting_point)  
  return neighbours

def get_active_nbo(nbor, puzzle_input):
  active_neighbours = []
  across = len(puzzle_input[0])
  down = len(puzzle_input)
  for nbo in nbor:
    if (nbo[0] < 0) or (nbo[1] < 0) or (nbo[2] < 0):
      continue
    elif (nbo[0] > down) or (nbo[1] > across):
      continue
    elif nbo[2] != 1:
      continue
    active_neighbours.append(puzzle_input[nbo[0]][nbo[1]])
  return active_neighbours

def get_new_state(nbor, current_state):
  active_count = nbor.count('#')
  if current_state == '#':
    if (active_count == 2) or (active_count == 3):
      return '#'
  elif current_state == '.':
    if (active_count == 3):
      return '#'
  return '.'
    


test_input = """.#.
..#
###"""

test_list = [list(y) for y in ((x.strip()) for x in test_input.splitlines())]
print(test_list)

print(seventeen_part_one(test_list))
