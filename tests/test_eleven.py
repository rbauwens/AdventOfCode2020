import pytest
import src.eleven as eleven

# python -m pytest ..\tests\test_template.py -s


# day_one_input = eleven.get_instructions()


# """
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

def test_example_part_two():
    x = 10
    y = 10
    assert list(eleven.get_eight_adjacent(0, 0, eleven.test_list)).sort() == list(['.', 'L', 'L']).sort()
    assert list(eleven.get_eight_adjacent(x-1, 0, eleven.test_list)).sort() == list(['.', '.', 'L']).sort()
    assert list(eleven.get_eight_adjacent(0, y-1, eleven.test_list)).sort() == list(['L', 'L', 'L']).sort()
    assert list(eleven.get_eight_adjacent(x-1, y-1, eleven.test_list)).sort() == list(['.', 'L', 'L']).sort()
    
    assert list(eleven.get_eight_adjacent(0, 1, eleven.test_list)).sort() == list(['L', 'L', 'L','L', 'L']).sort()
    assert list(eleven.get_eight_adjacent(1, 1, eleven.test_list)).sort() == list(['L', 'L', 'L','L', 'L', 'L', '.', '.']).sort()

def test_example_two():
    puzzle_input = eleven.test_list
    new_layout = puzzle_input.copy()
    x = len(puzzle_input[0])
    y = len(puzzle_input)
    
    for i in range(x):
        for j in range(y):
            adj = eleven.get_eight_adjacent(i, j, puzzle_input)
            seat = puzzle_input[i][j]
            new_layout[i][j] = eleven.get_new_seat(seat, adj)
    
    answer = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
    answer_list = [list(y) for y in ((x.strip()) for x in answer.splitlines())]
    
    for i in range(x):
        for j in range(y):
            assert answer_list[i][j] == new_layout[i][j]