import pytest
import src.five as five

# python -m pytest ..\tests\test_template.py -s

puzzle_input = five.get_instructions()
dummy_part_one_dict = dict()
def test_one():
    test0 = "FBFBBFFRLR"
    test1 = "BFFFBBFRRR"
    test2 = "FFFBBBFRRR"
    test3 = "BBFFBBFRLL"
    assert five.get_seat_id(test0, dummy_part_one_dict)[0] == 357
    five.get_seat_id(test1, dummy_part_one_dict)[0] == 567
    five.get_seat_id(test2, dummy_part_one_dict)[0] == 119
    five.get_seat_id(test3, dummy_part_one_dict)[0] == 820

def test_two():
    test_input = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    assert five.five_part_one(test_input)[0] == 820


def test_three():
    assert five.five_part_one(puzzle_input)[0] == 880

def test_four():
    _, all_seats_dict = five.five_part_one(puzzle_input)
    assert five.part_two(all_seats_dict) == 731

