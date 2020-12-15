import os
import re
import sys
import math
import itertools

def fifteen_part_one(puzzle_input):
  # [turn last called, number of times called]
  number_dict = dict()
  turn = 1
  last_number = 0
  for number in puzzle_input:
    number_dict[number] = [turn, turn,  1]
    turn = turn + 1
    last_number = number
  
  # max_num = 2021 # part 1
  max_num = 30000001 # part 2
  while turn < max_num:
    if number_dict[last_number][2] == 1:
      if 0 not in number_dict.keys():
        number_dict[0] = [turn, turn, 1]
      else:
        number_dict[0] = [turn, number_dict[0][0], number_dict[0][2] + 1]
      last_number = 0
    else:
      last_time = number_dict[last_number][0]
      time_before = number_dict[last_number][1]
      difference = last_time - time_before
      last_number = difference
      if last_number in number_dict.keys():
        number_dict[last_number] = [turn, number_dict[last_number][0], number_dict[last_number][2] + 1]
      else:
        number_dict[last_number] = [turn, turn, 1]
    turn = turn + 1
  return last_number


# puzzle_input = [0,3,6]
puzzle_input = [16,12,1,0,15,7,11]

print(fifteen_part_one(puzzle_input))
# 403 correct

# part 2 
# 6823 correct
