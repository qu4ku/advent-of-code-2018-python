"""
day 07:
https://adventofcode.com/2018/day/7
"""

import re

# Load data

with open('day07-input-test.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

steps = []
for line in data:
	a = re.findall(r'(?<=Step )\w', line)[0]
	b = re.findall(r'(?<=step )\w', line)[0]
	step = (a, b)
	steps.append(step)

print(steps)

string = ''.join(steps[0])
print(string)
for step in steps[1:]:
	print(step)
	first = step[0]
	second = step[1]
	if first in string:
		if second not in string:
			string += second
	print(string)
	print()
