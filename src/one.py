import os
import sys
import math
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_one_data')
EXPECTED_LINES = 200
# find 2 enteries that sum to 2020 then multiply the 2 numbers together


def dayone_function(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (array[i] + array[j] == 2020):
                return array[i] * array[j]


def dayone_function_p2(array):
  for i in range(len(array)):
      for j in range(len(array)):
        for k in range(len(array)):
          if (array[i] + array[j] + array[k] == 2020):
              return array[i] * array[j] * array[k]


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


dayone_partone_input = get_instructions()
print(dayone_function(dayone_partone_input))

print(dayone_function_p2(dayone_partone_input))
