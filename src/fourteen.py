import os
import re
import sys
import math
import itertools
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_fourteen_data')

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

def get_value(mask, bit_value):
  computed_value = list(bit_value)
  
  for bit in range(len(bit_value)):
    if mask[bit] == 'X':
      continue
    else:
      computed_value[bit] = mask[bit]
  return ''.join(computed_value)


def fourteen_part_one(puzzle_input):
    mask = ''
    new_dict = dict()
    
    for line in puzzle_input:
        if "mask" in line:
            mask = line[7:]
        else:
            if "mem" not in line:
                return("don't understand this line: {}".format(line))
            matches = re.match("mem\[(\d+)\] = (\d+)", line).groups()
            if len(matches) != 2:
                exit("couldn't read instruction {}".format(line))
            mem_addr = int(matches[0])
            new_value = int(matches[1])
            bit_value = '{0:b}'.format(new_value)
            bit_value = bit_value.zfill(36)
            computed_value = get_value(mask, bit_value)
            new_dict[mem_addr] = computed_value
        
    final_sum = 0
    for i in new_dict.keys():
      final_sum = final_sum + int(new_dict[i], 2)
    return final_sum



def get_addr_value(mask, bit_addr):
  """
  If the bitmask bit is 0, the corresponding memory address bit is unchanged.
  If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
  If the bitmask bit is X, the corresponding memory address bit is floating.
  """
  computed_value = list(bit_addr)
  
  for bit in range(len(bit_addr)):
    if mask[bit] == '0':
      continue
    elif mask[bit] == '1':
      computed_value[bit] = mask[bit]
    else:
      # floating case
      computed_value[bit] = 'X'
  memory_addresses = []
  num_x = computed_value.count('X')
  
  num_copies = 2 ** num_x
  
  indices = [i for i, x in enumerate(computed_value) if x == "X"]
  for index in indices:
    if len(memory_addresses) == 0:
      new_array = computed_value.copy()
      new_array[index] = '0'
      memory_addresses.append(new_array)
      new_array = computed_value.copy()
      new_array[index] = '1'
      memory_addresses.append(new_array)
    else:
      new_memory_addresses = memory_addresses.copy()
      for array in memory_addresses:
        array[index] = '0'
        new_array = array.copy()
        new_array[index] = '1'
        
        new_memory_addresses.append(new_array)
      memory_addresses = new_memory_addresses
  assert len(memory_addresses) == num_copies    
  
  memory_strings = []
  for array in memory_addresses:
    new_array_string = ''.join(array)        
    memory_strings.append(int(new_array_string, 2))
  
  return memory_strings

def fourteen_part_two(puzzle_input):
    mask = ''
    new_dict = dict()
    for line in puzzle_input:
        if "mask" in line:
            mask = line[7:]
        else:
            if "mem" not in line:
                return("don't understand this line: {}".format(line))
            matches = re.match("mem\[(\d+)\] = (\d+)", line).groups()
            if len(matches) != 2:
                exit("couldn't read instruction {}".format(line))
            mem_addr = int(matches[0])
            new_value = int(matches[1])
            
            bit_addr = '{0:b}'.format(mem_addr)
            bit_addr = bit_addr.zfill(36)
            computed_addresses = get_addr_value(mask, bit_addr)
            for address in computed_addresses:
              new_dict[address] = new_value
    
    final_sum = 0
    for i in new_dict.keys():
      final_sum = final_sum + new_dict[i]
    return final_sum
    



test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

test_list = [y for y in ((x.strip()) for x in test_input.splitlines())]
# print(fourteen_part_one(test_list))
#165

test_input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
test_list2 = [y for y in ((x.strip()) for x in test_input2.splitlines())]
print(fourteen_part_two(test_list2))
# print(get_addr_value("000000000000000000000000000000X1001X", "000000000000000000000000000000101010"))
# print(get_addr_value("00000000000000000000000000000000X0XX", "000000000000000000000000000000011010"))

puzzle_input = get_instructions()
print(fourteen_part_one(puzzle_input))
#9628746976360 correct
print(fourteen_part_two(puzzle_input))
#4574598714592 correct
