import os
import re
import sys
import math
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_six_data')
TEST_DATA_FILE = os.path.join(DATA_FOLDER, 'day_six_test_data')
EXPECTED_LINES = 2283


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

    return instructions


# find how many passwords are valid
def six_part_one(puzzle_input, part_two=True):
    num_new_lines = puzzle_input.count('')
    num_groups = num_new_lines + 1

    #################
    i = 0
    j = 0
    multi_group_array = []
    while (j < num_groups):
      group_array = []
      while (i < len(puzzle_input)) and (puzzle_input[i] != ''):
        group_array.append(puzzle_input[i])
        i = i+1
      multi_group_array.append(group_array)
      j = j + 1
      i = i+1
    #################

    yes_answers = 0
    for group in range(len(multi_group_array)):
      if part_two:
        group_yes = get_number_of_all_yes(multi_group_array[group])
      else:
        group_yes = get_number_of_yes(multi_group_array[group])
      yes_answers = yes_answers + group_yes
    
    return yes_answers


# for part 1
def get_number_of_yes(group_entry):
  list_of_yes_answers = []
  for i in range(len(group_entry)):
    for j in range(len(group_entry[i])):
      if group_entry[i][j] not in list_of_yes_answers:
        list_of_yes_answers.append(group_entry[i][j])
  return len(list_of_yes_answers)


# for part 2
def get_number_of_all_yes(group_entry):
  # fill a list based on the first person
  list_of_yes_answers = []
  for k in range(len(group_entry[0])):
    list_of_yes_answers.append(group_entry[0][k])

  final_list_of_yes_answers = list_of_yes_answers.copy()

  # now go through the rest and remove entries that aren't in all of them
  for i in range(1, len(group_entry)):
    list_of_yes_answers = final_list_of_yes_answers.copy()
    for j in range(len(list_of_yes_answers)):
      if list_of_yes_answers[j] not in group_entry[i]:
        final_list_of_yes_answers.remove(list_of_yes_answers[j])
  return len(final_list_of_yes_answers)
    


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

test_input2 = """hlqbanmtjy
tdrvxcajgnfpoke
jtiunkpsroa"""


test_list = [y for y in (x.strip() for x in test_input.splitlines())]
print(six_part_one(test_list))
#11 for p1, #6 for p2

test_list2 = [y for y in (x.strip() for x in test_input2.splitlines())]
print(six_part_one(test_list2))

puzzle_input = get_instructions()
print(six_part_one(puzzle_input))
#7120
#3570


