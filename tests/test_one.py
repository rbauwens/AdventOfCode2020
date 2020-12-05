import pytest
import src.one as one

# python -m pytest ..\tests\test_template.py -s

example_input = [1721, 979, 366, 299, 675, 1456]
day_one_input = one.get_instructions()


def test_example_part_one():
    assert 514579 == one.dayone_function(example_input)


def test_example_part_two():
    assert 241861950 == one.dayone_function_p2(example_input)


def test_part_one():
    assert 494475 == one.dayone_function(day_one_input)


def test_part_two():
    assert 267520550 == one.dayone_function_p2(day_one_input)
