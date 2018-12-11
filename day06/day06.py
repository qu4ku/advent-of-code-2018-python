"""
day 06:
https://adventofcode.com/2018/day/6
"""

import re
from collections import Counter

# Load data
with open('day06-input-test.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

cleaned_data = []
for line in data:

	line = [int(x) for x in line.split(', ')]
	cleaned_data.append(line)

def taxicab_dist(v1, v2):
	return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
	
print(cleaned_data)

max_width = sorted(cleaned_data, key=lambda x: x[0], reverse=True)[0][0]
min_width = sorted(cleaned_data, key=lambda x: x[0])[0][0]
max_height = sorted(cleaned_data, key=lambda x: x[1], reverse=True)[0][1]
min_height = sorted(cleaned_data, key=lambda x: x[1])[0][1]
print(max_width, min_width, max_height, min_height)



print(taxicab_dist([0, 0], [1, 1]))
