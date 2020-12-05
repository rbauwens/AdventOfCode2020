import pytest
import src.two as two

# python -m pytest ..\tests\test_template.py -s

day_two_input = two.get_instructions()

test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

test_list = [y for y in (x.strip() for x in test_input.splitlines()) if y]

def test_example_part_one():
    assert 2 == two.daytwo_function(test_list)


def test_example_part_two():
    assert 515 == two.daytwo_function(day_two_input)


def test_part_two():
    assert 1 == two.daytwo_parttwo(test_list)


def test_part_two():
    assert 711 == two.daytwo_parttwo(day_two_input)

