import os
import re
import sys
import math
import itertools
import sympy as sym
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_thirteen_data')

EXPECTED_LINES = 2


def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append((line.strip()))
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions


def thirteen_part_one(puzzle_input):
  time = int(puzzle_input[0])
  buses = puzzle_input[1].split(',')
  
  available_buses = []
  for i in range(len(buses)):
    if buses[i] != 'x':
      available_buses.append(buses[i])

  available_buses = [y for y in ((int(x)) for x in available_buses)]
  bus_dict = dict()

  for j in range(len(available_buses)):
    bus = available_buses[j]
    mult = 1
    got_it = False
    while not got_it:
      next_time = bus * mult
      if next_time >= time:
        bus_dict[bus] = next_time
        got_it = True
      mult = mult + 1
  
  next_bus = min(bus_dict.values())
  difference = next_bus - time

  bus_id = [name for name, age in bus_dict.items() if age == next_bus][0]
  return bus_id * difference


  
def thirteen_part_two(puzzle_input):
  
  buses = puzzle_input[1].split(',')
  
  available_buses = []
  for i in range(len(buses)):
    if buses[i] != 'x':
      available_buses.append(buses[i])

  available_buses = [y for y in ((int(x)) for x in available_buses)]
  max_bus = max(available_buses)
  min_bus = min(available_buses)
  print(max_bus, min_bus)
  
  mult = 1
  possibles = []
  while len(possibles) == 0:
    next_time = max_bus * mult
    if next_time == 1068785:
      print("stop")
    div = float((next_time - 4) / min_bus)
    if int(div) == div:
      my_sum = float(((min_bus * div) + 1) / 13)
      if int(my_sum) == my_sum:
        my_sum = float(((min_bus * div) + 6) / 31)
        if int(my_sum) == my_sum:
          my_sum = float(((min_bus * div) + 7) / 19)
          if int(my_sum) == my_sum:
            possibles.append(div)                        
          
    mult = mult + 1
  print(possibles)
  print(7 * div)
  print(1068781)


def thirteen_part_two_bash(puzzle_input):
  
  buses = puzzle_input[1].split(',')
  bus_dict = dict()
  available_buses = []
  for i in range(len(buses)):
    if buses[i] != 'x':
      available_buses.append(buses[i])
      bus_dict[int(buses[i])] = int(i)

  print(available_buses)
  print(bus_dict)
  
  available_buses = [y for y in ((int(x)) for x in available_buses)]
  max_bus = max(available_buses)
  # min_bus = min(available_buses)
  min_bus = 29
  print(max_bus, min_bus)
  max_adj = bus_dict[max_bus]

  # mult = 121506682868
  mult = 2146718506871
  possibles = []
  while len(possibles) == 0:
    if mult == 2052434903390104:
      print("STOPPING NOW")
      return
    next_time = max_bus * mult
    div = float((next_time - max_adj) / min_bus)
    if int(div) == div:
      my_sum = float(((min_bus * div) + 29) / 653)
      if int(my_sum) == my_sum:
        my_sum = float(((min_bus * div) + 19) / 41)    
        if int(my_sum) == my_sum:
          my_sum = float(((min_bus * div) + 23) / 37)  
          if int(my_sum) == my_sum:
            my_sum = float(((min_bus * div) + 52) / 23)
            if int(my_sum) == my_sum:
              my_sum = float(((min_bus * div) + 46) / 17)
              if int(my_sum) == my_sum:
                my_sum = float(((min_bus * div) + 42) / 13)    
                if int(my_sum) == my_sum: 
                  my_sum = float(((min_bus * div) + 79) / 19)
                  if int(my_sum) == my_sum: 
                    possibles.append(div)                        
          
    mult = mult + 1
  print(possibles)
  print(min_bus * div)
    
def lcm(a,b):
  return a*b/(math.gcd(a,b))



def thirteen_part_two_lcm(puzzle_input):
  
  buses = puzzle_input[1].split(',')
  bus_dict = dict()
  available_buses = []
  for i in range(len(buses)):
    if buses[i] != 'x':
      available_buses.append(buses[i])
      bus_dict[int(buses[i])] = int(i)
  print(bus_dict)
  return
  
  available_buses = [y for y in ((int(x)) for x in available_buses)]
  for i in range(121506682868):
    sum = float(((29*i)+60)/823)
    if int(sum) == sum:
      sum = float(((29*i)+29)/653)
      if int(sum) == sum:
        sum = float(((29*i)+23)/37)
        if int(sum) == sum:
          sum = float(((29*i)+19)/41)
          if int(sum) == sum:
            sum = float(((29*i)+52)/23)
            if int(sum) == sum:
              sum = float(((29*i)+79)/19)
              if int(sum) == sum:
                sum = float(((29*i)+37)/19)
                if int(sum) == sum:
                  sum = float(((29*i)+42)/13)
                  if int(sum) == sum:
                    sum = float(((29*i)+46)/17)
                    if int(sum) == sum:
                      print(i)
                      print(sum)
                      return
        
        


  

test_input = """939
7,13,x,x,59,x,31,19"""


test_list = [y for y in ((x.strip()) for x in test_input.splitlines())]
# print(thirteen_part_one(test_list))
# print(thirteen_part_two(test_list))


puzzle_input = get_instructions()
# print(thirteen_part_one(puzzle_input))
#4938
# print(thirteen_part_two_bash(puzzle_input))
print(thirteen_part_two_lcm(puzzle_input))

# Python 3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    print(a_i)
    print(p)
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
 

# n = [3, 5, 7]
# a = [2, 3, 2]

# # {29: 0, 41: 19, 37: 23, 653: 29, 13: 42, 17: 46, 23: 52, 823: 60, 19: 79}
n = [29, 41, 37, 653, 13, 17, 23, 823, 19]
a = [0, 19, 23, 29, 42, 46, 52, 60, 79]
# print(chinese_remainder(n, a))

# # 2052434903390758 too high
# print(29*79)
# print((41*79) + 19)


# modular inverse
def inverse_mod(a,b):
    x = a
    y = b
    oldolds = 1
    olds = 0
    oldoldt = 0
    oldt = 1
    while y != 0:
        q = x // y
        r = x % y
        x = y
        y = r
        s = oldolds - q * olds
        t = oldoldt - q * oldt
        oldolds = olds
        oldoldt = oldt
        olds = s
        oldt = t
    return oldolds
# The chinese remainder theorem
def chi_rem_thm(mn,an):
    m = 1
    Mn = []
    yn = []
    for k in range(0, len(mn)):
         m  = m * mn[k]
    
    for  k in range (0, len(mn)):
        Mk = m / mn[k]
        Mn.append(Mk)
        yk = inverse_mod(Mn[k],mn[k]) % mn[k]
        yn.append(yk)
    x = 0
    for  k in range (0, len(yn)):
        x = x + an[k] * Mn[k] * yn[k]
    while x >= m:
        x = x - m
    return x
  # test
# print(chi_rem_thm([1,2],[4,3]))
# print(chi_rem_thm(n,a))

# x = a mod not
# 1 = 4 mod 1
# 1 = 3 mod 2

# t = 0 mod 29
# t = 19 mod 41
# t = 23 mod 37
# a = chi_rem_thm([29,41,37, 653, 13, 17, 23, 19],[0,19,23, 29, 42, 46, 52, 79])
# a = chi_rem_thm([29,653,823,41,37, 13,17],[0,29, 60,19,23, 42,46])
# print("###")
# print(a)
# print("###")
a = chi_rem_thm([29, 41, 37, 653, 13, 17, 23, 823, 19],[0, 20, 24, 30, 43, 47, 53, 61, 80])
a = 5303804508512
print("###")
print(a)
print("###")

print(float(a / 29))
print(float((a - 19) / 41))
print(float((a - 23) / 37))
print(float((a - 29) / 653))
print(float((a - 42) / 13))
print(float((a - 46) / 17))
print(float((a - 52) / 23))
print(float((a - 60) / 823))
print(float((a - 79) / 19))

# too high
# 2052434903390758
# 2052434903390104.0

# wrong 
# 5303804508512

#too low
# 2146718506871

for i in range(2146718506871, 2052434903390104):
  possibles = []
  sum1 = float((i-60) / 823)
  sum2 = float((i-29) / 653)
  if (sum1 == int(sum1)) and (sum2 == int(sum2)):
    possibles.append(i)

print(possibles)


