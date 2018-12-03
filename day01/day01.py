"""
day 01:
https://adventofcode.com/2018/day/1
"""

with open('day01-input.txt', 'r') as f:
	input_list = [int(x) for x in f.readlines() if x != '\n']

total = 0
for x in input_list:
	total += x
print(total)
