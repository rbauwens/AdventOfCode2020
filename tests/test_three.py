import pytest
import src.three as three

# python -m pytest ..\tests\test_template.py -s

day_three_input = three.get_instructions()


def test_example_part_one():
    assert 7 == three.three_part_one(three.test_list, 3, 1)


def test_part_one():
    assert 151 == three.three_part_one(day_three_input, 3, 1)


def test_example_part_two():
    assert 336 == three.three_part_two(three.test_list)


def test_part_two():
    assert 7540141059 == three.three_part_two(day_three_input)

