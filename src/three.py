import os
import sys
import math
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_three_data')
EXPECTED_LINES = 323

# find how many passwords are valid
def three_part_one(puzzle_input, right, down):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    # print(width, height)
    start_point = puzzle_input[0][0]
    
    marker_right = 0
    marker_down = 0
    opens = 0
    trees = 0
    steps = 0
    while (marker_down < (height-1)):
      steps = steps + 1
      marker_right = (marker_right + right) % width
      marker_down = marker_down + down
      hit = puzzle_input[marker_down][marker_right]
      if (hit == '.'):
        # print("O")
        opens = opens + 1
      if (hit == '#'):
        # print("X")
        trees = trees + 1

    assert opens + trees == steps
    # print("opens: {}".format(opens))
    # print("trees: {}".format(trees))
    return trees
    
def three_part_two(puzzle_input):
  # Right 1, down 1.
  a = three_part_one(puzzle_input, 1, 1)
  # Right 3, down 1. 
  b = three_part_one(puzzle_input, 3, 1)
  # Right 5, down 1.
  c = three_part_one(puzzle_input, 5, 1)
  # Right 7, down 1.
  d = three_part_one(puzzle_input, 7, 1)
  # Right 1, down 2.
  e = three_part_one(puzzle_input, 1, 2)
  print(a, b, c, d, e)
  return (a*b*c*d*e)
    




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





test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

test_list = [y for y in (x.strip() for x in test_input.splitlines()) if y]
print(three_part_one(test_list, 3, 1))


puzzle_input = get_instructions()
print(three_part_one(puzzle_input, 3, 1))

print(three_part_two(test_list))
print(three_part_two(puzzle_input))