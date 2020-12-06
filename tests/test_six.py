import pytest
import os
import src.six as six

# python -m pytest ..\tests\test_template.py -s

# day_six_input = six.get_instructions()
# test_part_one = six.get_test_instructions()



def test_part_one_example():
  assert 11 == six.six_part_one(six.test_list, part_two=False)


def test_part_one():
  puzzle_input = six.get_instructions()
  assert 7120 == six.six_part_one(puzzle_input, part_two=False)

def test_part_two_example_one():
  assert 6 == six.six_part_one(six.test_list)


def test_part_two_example_two():
  assert 4 == six.six_part_one(six.test_list2)


def test_part_two():
  puzzle_input = six.get_instructions()
  assert 3570 == six.six_part_one(puzzle_input)


