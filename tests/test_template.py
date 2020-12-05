import pytest
import src.one as one

# python -m pytest ..\tests\test_template.py -s

example_input = [1721, 979, 366, 299, 675, 1456]
day_one_input = one.get_instructions()


def test_example_part_one():
    assert 514579 == one.dayone_function(example_input)

