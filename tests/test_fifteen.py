import pytest
import src.fifteen as fifteen

# python -m pytest ..\tests\test_template.py -s


def test_example_one():
    assert 436 ==  fifteen.fifteen_part_one([0,3,6])
    assert 1 ==  fifteen.fifteen_part_one([1,3,2])
    assert 10 ==  fifteen.fifteen_part_one([2,1,3])
    assert 27 ==  fifteen.fifteen_part_one([1,2,3])
    assert 78 ==  fifteen.fifteen_part_one([2,3,1])
    assert 438 ==  fifteen.fifteen_part_one([3,2,1])
    assert 1836 ==  fifteen.fifteen_part_one([3,1,2])


# Given the starting numbers 1,3,2, the 2020th number spoken is 1.
# Given the starting numbers 2,1,3, the 2020th number spoken is 10.
# Given the starting numbers 1,2,3, the 2020th number spoken is 27.
# Given the starting numbers 2,3,1, the 2020th number spoken is 78.
# Given the starting numbers 3,2,1, the 2020th number spoken is 438.
# Given the starting numbers 3,1,2, the 2020th number spoken is 1836.