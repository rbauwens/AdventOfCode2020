import os
import re
import sys
import math
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_four_data')
TEST_DATA_FILE = os.path.join(DATA_FOLDER, 'day_four_test_data')
EXPECTED_LINES = 1023



# find how many passwords are valid
def four_part_one(puzzle_input):
    num_new_lines = puzzle_input.count('')
    num_passports = num_new_lines + 1

    #################
    i = 0
    j = 0
    multi_passport_array = []
    while (j < num_passports):
      passport_array = []
      while (i < len(puzzle_input)) and (puzzle_input[i] != ''):
        passport_array.append(puzzle_input[i])
        i = i+1
      multi_passport_array.append(passport_array)
      j = j + 1
      i = i+1
    #################

    multi_passport_dictionary_array = []
    for k in range(len(multi_passport_array)):
      multi_passport_dictionary_array.append(get_dictionary(multi_passport_array[k]))

    num_valid = 0
    for m in range(len(multi_passport_dictionary_array)):
      is_valid = is_valid_passport(multi_passport_dictionary_array[m])
      # print(is_valid)
      if is_valid:
        num_valid = num_valid + 1

    return num_valid
    
def get_dictionary(passport_array):
  passport_dictionary = dict()
  for line in range(len(passport_array)):
    line_array = passport_array[line].split(" ")
    for entry in range(len(line_array)):
      passport_dictionary[line_array[entry].split(":")[0]] = line_array[entry].split(":")[1]
  return passport_dictionary

def is_valid_passport(passport):
  for field in REQUIRED_FIELDS:
    if field not in passport.keys():
      return False
    # comment out next three lines for part 1  
    else:
      if not is_valid(field, passport[field]):
        return False
  return True

def is_valid(field, entry):
  if field == "byr":
    return 1920 <= int(entry) <= 2002
  elif field == "iyr":
    return 2010 <= int(entry) <= 2020
  elif field == "eyr":
    return 2020 <= int(entry) <= 2030
  elif field == "hgt":
    if "cm" in entry:
      return 150 <= int(entry.split("cm")[0]) <= 193
    elif "in" in entry:
      return 59 <= int(entry.split("in")[0]) <= 76
    else:
      return False
  elif field == "hcl":
    if re.match(r"^#[0-9|a-f]{6}$", entry):
        return True
    else:
      return False
  elif field == "ecl":
    return entry in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  elif field == "pid":
    if re.match(r"^[0-9]{9}$", entry):
        return True
    else:
      return False
    
      

  
def four_part_two(puzzle_input):
  return True




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

def get_test_instructions():
    instructions = []
    with open(TEST_DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != 13 + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions

def get_test_instructions_file(file_name):
    instructions = []
    with open(file_name) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    return instructions


test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

# test_part_one = get_test_instructions()
# print(four_part_one(test_part_one))


puzzle_input = get_instructions()
print(four_part_one(puzzle_input))
# 206
#123
# print(four_part_two(test_list))
# print(four_part_two(puzzle_input))

