import pytest
import os
import src.four as four

# python -m pytest ..\tests\test_template.py -s

# day_four_input = four.get_instructions()
# test_part_one = four.get_test_instructions()


# def test_example_part_one():
#   test_data = four.get_test_instructions()
#   assert 2 == four.four_part_one(test_data)
    


# def test_part_one():
#     assert 206 == four.four_part_one(day_four_input)


def test_valid():
  assert True == four.is_valid("byr", "2002")
  assert False == four.is_valid("byr", "2003")
  
  assert True == four.is_valid("hgt", "60in")
  assert True == four.is_valid("hgt", "190cm")
  assert False == four.is_valid("hgt", "190in")
  assert False == four.is_valid("hgt", "190")

  assert True == four.is_valid("hcl", "#123abc")
  assert False == four.is_valid("hcl", "#123abz")
  assert False == four.is_valid("hcl", "123abc")

  assert True == four.is_valid("ecl", "brn")
  assert False == four.is_valid("ecl", "wat")

  assert True == four.is_valid("pid", "000000001")
  assert False == four.is_valid("pid", "0123456789")


def test_example_valid():
  
  DATA_FILE = os.path.join(four.DATA_FOLDER, 'four_valid')
  test_data = four.get_test_instructions_file(DATA_FILE)
  assert 4 == four.four_part_one(test_data)


def test_example_invalid():
  
  DATA_FILE = os.path.join(four.DATA_FOLDER, 'four_invalid')
  test_data = four.get_test_instructions_file(DATA_FILE)
  assert 0 == four.four_part_one(test_data)


def test_example_part_two():
  test_data = four.get_instructions()
  assert 123 == four.four_part_one(test_data)
