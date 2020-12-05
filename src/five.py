import os
import sys
import math
import re
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_five_data')
EXPECTED_LINES = 867


def five_part_one(puzzle_input):
    all_seats = dict()
    highest_id = 0
    for i in range(len(puzzle_input)):
        seat_code = puzzle_input[i]
        id, all_seats = get_seat_id(seat_code, all_seats)
        if id > highest_id:
            highest_id = id
    return highest_id, all_seats


def get_seat_id(seat_code, all_seats):
    # sanity checks
    assert len(seat_code) == 10
    assert re.match(r"^[B|F]{7}[R|L]{3}$", seat_code) is not None

    # calculate row
    row_options = [0, 127]
    for instruction in range(0, 7):
        row_options = update_row_options(row_options, seat_code[instruction])
    assert row_options[0] == row_options[1]
    row = row_options[0]    
    if row not in all_seats.keys():
        all_seats[row] = []
    
    # calculate seat
    seat_options = [0, 7]
    for instruction in range(7, 10):
        seat_options = update_row_options(seat_options, seat_code[instruction])
    assert seat_options[0] == seat_options[1]
    seat = seat_options[0]
    all_seats[row].append(seat)

    return ((row * 8) + seat), all_seats


def update_row_options(row_options, instruction):
    if (instruction == "F") or (instruction == "L"):
        row_options[1] = math.floor((((row_options[1] - row_options[0]) / 2) + row_options[0]))
    elif (instruction == "B") or (instruction == "R"):
        row_options[0] = math.ceil((((row_options[1] - row_options[0]) / 2) + row_options[0]))
    else:
        exit("unknown row option")
    return row_options


def part_two(all_seats):
    
    missing_rows = []
    possible_rows = []
    for i in range(0, 128):
        if i not in all_seats.keys():
            missing_rows.append(i)
        elif len(all_seats[i]) != 8:
            possible_rows.append(i)
    
    for row in possible_rows:
        if ((row-1) in missing_rows):
            continue
        elif ((row+1) in missing_rows):
            continue
        else:
            my_row = row
            break
    for j in range(0,8):
        if j not in all_seats[row]:
            my_seat = j
    print("my seat is {}, seat {}".format(my_row, my_seat))
    return (my_row * 8) + my_seat
        

def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions


# test_input = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
# five_part_one(test_input)


puzzle_input = get_instructions()
highest_id, all_seats_dict = five_part_one(puzzle_input)
print(highest_id)
#880

print(part_two(all_seats_dict))
#731