"""
day 01:
https://adventofcode.com/2018/day/1
"""

from itertools import cycle


# Load data
with open('day01-input.txt', 'r') as f:
	data = [int(line.strip()) for line in f.readlines()]


# First part
ans = 0
for x in data:
	ans += x
print(ans)  # ans = 497


# Second part
current_frequency = 0
frequencies = [current_frequency]
ans = False
for x in cycle(data):
	current_frequency += x
	if current_frequency not in frequencies:
		frequencies.append(current_frequency)
	else:
		ans = current_frequency
		break
print(ans)  # ans = 558
