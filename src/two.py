import os
import sys
import math
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_two_data')
EXPECTED_LINES = 1000

# find how many passwords are valid
def daytwo_function(puzzle_input):
    valid = 0
    # for key in dictionary:
    for i in range(len(puzzle_input)):
      entry = puzzle_input[i]
      print(entry)
      min_num, max_num, letter, password = get_policy(entry)
      # print(min_num, max_num, letter)
      count = password.count(letter)
      print(count)
      if ((min_num <= count) and (count <= max_num)):
        print("valid")
        valid = valid + 1
    return valid


def daytwo_parttwo(puzzle_input):
  valid = 0
  for i in range(len(puzzle_input)):
    entry = puzzle_input[i]
    print(entry)
    pos1, pos2, letter, password = get_policy(entry)
    
    if ((password[pos1 - 1] == letter) and (password[pos2 - 1] != letter)) or ((password[pos1 - 1] != letter) and (password[pos2 - 1] == letter)):
      print("valid")
      valid = valid + 1
  return valid


def get_policy(line):
  password = line.split(":")[1]
  key = line.split(":")[0]
  letter = key.split(" ")[1]
  policy = key.split(" ")[0]
  min_value = policy.split("-")[0]
  max_value = policy.split("-")[1]
  return int(min_value), int(max_value), letter, password.strip()



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





puzzle_input = get_instructions()
# print("answer = ", daytwo_function(puzzle_input))


test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

test_list = [y for y in (x.strip() for x in test_input.splitlines()) if y]
print(test_list)


# print(daytwo_parttwo(test_list))

print("answer: ", daytwo_parttwo(puzzle_input))