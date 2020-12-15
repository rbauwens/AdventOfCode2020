import pytest
import src.fourteen as fourteen

# python -m pytest ..\tests\test_template.py -s

def test_part_one_prep():
  mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
  assert "000000000000000000000000000001001001" == fourteen.get_value(mask, "000000000000000000000000000000001011")
  assert "000000000000000000000000000001100101" == fourteen.get_value(mask, "000000000000000000000000000001100101")
  assert "000000000000000000000000000001000000" == fourteen.get_value(mask, "000000000000000000000000000000000000")


def test_part_one_example():
  assert 165 == fourteen.fourteen_part_one(fourteen.test_list)


def test_part_one_example():
  assert 208 == fourteen.fourteen_part_two(fourteen.test_list2)

def test_part_two_prep():
  expected_array = [26, 27, 58, 59]
  assert expected_array.sort() == fourteen.get_addr_value("000000000000000000000000000000X1001X", "000000000000000000000000000000101010").sort()

  expected_array = [16, 17, 18, 19, 24, 25, 26, 27]
  assert expected_array.sort() == fourteen.get_addr_value("00000000000000000000000000000000X0XX", "000000000000000000000000000000011010").sort()

def test_part_one():
  assert 9628746976360 ==  fourteen.fourteen_part_one(fourteen.puzzle_input)

def test_part_two():
  assert 4574598714592 ==  fourteen.fourteen_part_two(fourteen.puzzle_input)

