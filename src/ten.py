import os
import re
import sys
import math
import itertools
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_ten_data')

EXPECTED_LINES = 104


def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(int(line.strip()))
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions

def ten_part_one(puzzle_input):
  differences = []
  adapter_list = []
  max_val = 0
  for i in range(len(puzzle_input)):
    if puzzle_input[i] - max_val <= 3:
      # current_jolt = puzzle_input[i]
      if adapter_list != []:
        difference = puzzle_input[i] - adapter_list[-1]
        differences.append(difference)
      else:
        differences.append(puzzle_input[i])
      adapter_list.append(puzzle_input[i])
    max_val = puzzle_input[i]
    
  
  print(max_val)
  print(adapter_list)
  
  differences.append(3)
  
  new_dict = dict()
  for value in differences:
    if value not in new_dict.keys():
      new_dict[value] = 1
    else:
      new_dict[value] = new_dict[value] + 1
  print(new_dict)
  return new_dict[1]*new_dict[3]

def ten_part_two(puzzle_input):
  
  puzzle_input.insert(0, 0)
  puzzle_input.insert(len(puzzle_input), puzzle_input[-1]+3)
  
  diffs = [j-i for i, j in zip(puzzle_input[:-1], puzzle_input[1:])] 
  
  blocks = []
  one_count = 0
  for i in range(len(diffs)):
    if diffs[i] == 1:
      one_count = one_count + 1
    else:
      if(one_count != 0):
        blocks.append(one_count)
      one_count = 0
  multipliers = []
  for ones in blocks:
    if ones != 1:
      if (ones == 2):
        multipliers.append(2)
        
      elif (ones == 3):
        multipliers.append(4)
        
      elif (ones == 4):
        multipliers.append(7)
        
      else:
        exit("PANIC")
  
  return math.prod(multipliers)

    
  

test_input = """16
10
15
5
1
11
7
19
6
12
4"""

test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

test_list = [y for y in (int(x.strip()) for x in test_input.splitlines())]
test_list.sort()
# print(ten_part_one(test_list))
print(ten_part_two(test_list))

test_list2 = [y for y in (int(x.strip()) for x in test_input2.splitlines())]
test_list2.sort()
# print(ten_part_one(test_list2))
print(ten_part_two(test_list2))
#19208

puzzle_input = get_instructions()
puzzle_input.sort()
# print(puzzle_input)
# print(ten_part_one(puzzle_input))
# # 2414
print(ten_part_two(puzzle_input))
