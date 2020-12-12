import pytest
import src.twelve as twelve

# python -m pytest ..\tests\test_template.py -s


def test_example_one():
    assert 25 ==  twelve.twelve_part_one(twelve.test_list)

def test_example_two():
    assert 286 ==  twelve.twelve_part_two(twelve.test_list)


def test_part_one():
    assert 2057 ==  twelve.twelve_part_one(twelve.puzzle_input)

def test_part_two():
    assert 71504 ==  twelve.twelve_part_two(twelve.puzzle_input)

