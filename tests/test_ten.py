import pytest
import src.ten as ten

# python -m pytest ..\tests\test_template.py -s

example_input = [1721, 979, 366, 299, 675, 1456]
day_one_input = ten.get_instructions()




def test_example_part_two():
    test_list = [y for y in (int(x.strip()) for x in ten.test_input.splitlines())]
    test_list.sort()
    assert 8 == ten.ten_part_two(test_list)


def test_example_part_two_b():
    test_list = [y for y in (int(x.strip()) for x in ten.test_input2.splitlines())]
    test_list.sort()
    assert 19208 == ten.ten_part_two(test_list)


def test_part_one():
    puzzle_input = ten.get_instructions()
    puzzle_input.sort()
    assert 2414 == ten.ten_part_one(puzzle_input)



def test_part_two():
    puzzle_input = ten.get_instructions()
    puzzle_input.sort()
    assert 21156911906816 == ten.ten_part_two(puzzle_input)
