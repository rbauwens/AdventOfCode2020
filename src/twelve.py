import os
import re
import sys
import math
import itertools
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_twelve_data')

EXPECTED_LINES = 774


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

def twelve_part_one(puzzle_input):
    direction = "E"
    directions = ['E', 'S', 'W', 'N']
    # [N/S, E/W]
    starting_point = [0, 0]
    for i in range(len(puzzle_input)):
      move = puzzle_input[i][0]
      amount = int(puzzle_input[i][1:])
      
      if move == 'F':
        if direction == 'E':
          starting_point[1] = starting_point[1] + amount
        elif direction == 'W':
          starting_point[1] = starting_point[1] - amount
        elif direction == 'N':
          starting_point[0] = starting_point[0] + amount
        elif direction == 'S':
          starting_point[0] = starting_point[0] - amount
   
      elif move == 'E':
        starting_point[1] = starting_point[1] + amount
      elif move == 'W':
        starting_point[1] = starting_point[1] - amount
      elif move == 'N':
        starting_point[0] = starting_point[0] + amount
      elif move == 'S':
        starting_point[0] = starting_point[0] - amount
      
      elif (move == 'L') or (move == 'R'):
        number_of_turns = int(amount/90)
        current_direction = directions.index(direction)
        
        if move == 'L':
          new_direction = directions[(current_direction - number_of_turns) % 4]
        if move == 'R':
          new_direction = directions[(current_direction + number_of_turns) % 4]
        # print(new_direction)
        direction = new_direction
        
      # print(starting_point)
    return abs(starting_point[0]) + abs(starting_point[1])


def twelve_part_two(puzzle_input):
    direction = "E"
    directions = ['E', 'S', 'W', 'N']
    # [N/S, E/W]
    starting_point = [0, 0]
    waypoint = [1, 10]
    for i in range(len(puzzle_input)):
      move = puzzle_input[i][0]
      amount = int(puzzle_input[i][1:])
      
      if move == 'F':
        starting_point[0] = starting_point[0] + (waypoint[0] * amount)
        starting_point[1] = starting_point[1] + (waypoint[1] * amount)
         
      elif move == 'E':
        waypoint[1] = waypoint[1] + amount
      elif move == 'W':
        waypoint[1] = waypoint[1] - amount
      elif move == 'N':
        waypoint[0] = waypoint[0] + amount
      elif move == 'S':
        waypoint[0] = waypoint[0] - amount
      
      elif (move == 'R'):
        # move waypoint
        number_of_turns = int(amount/90)
        print(number_of_turns)
        for j in range(number_of_turns):
          new_waypoint = [0,0]
          new_waypoint[1] = waypoint[0]
          new_waypoint[0] = -waypoint[1]
          waypoint = new_waypoint
      elif (move == 'L'):
        # move waypoint
        number_of_turns = int(amount/90)
        print(number_of_turns)
        for j in range(number_of_turns):
          new_waypoint = [0,0]
          new_waypoint[1] = -waypoint[0]
          new_waypoint[0] = waypoint[1]
          waypoint = new_waypoint
      
        
    return abs(starting_point[0]) + abs(starting_point[1])





test_input = """F10
N3
F7
R90
F11"""


test_list = [y for y in ((x.strip()) for x in test_input.splitlines())]
# print(twelve_part_one(test_list)) #25
# print(twelve_part_two(test_list)) #286

puzzle_input = get_instructions()
# print(twelve_part_one(puzzle_input))
#2057
print(twelve_part_two(puzzle_input))

#71504