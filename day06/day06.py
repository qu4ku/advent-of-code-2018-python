"""
day 06:
https://adventofcode.com/2018/day/6
"""

import re
from collections import Counter

# Load data
# with open('day06-input-test.txt', 'r') as f:
with open('day06-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

cleaned_data = []
for line in data:

	line = [int(x) for x in line.split(', ')]
	cleaned_data.append(line)

def taxicab_dist(v1, v2):
	return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
	
# print(cleaned_data)

max_width = sorted(cleaned_data, key=lambda x: x[0], reverse=True)[0][0]
min_width = sorted(cleaned_data, key=lambda x: x[0])[0][0]
max_height = sorted(cleaned_data, key=lambda x: x[1], reverse=True)[0][1]
min_height = sorted(cleaned_data, key=lambda x: x[1])[0][1]
# print(max_width, min_width, max_height, min_height)

def calculate_area(area):
	bank = {}

	for width in range(0 - area, max_width + area):
		for height in range(0 - area, max_height + area):
			min_dist = 999999999
			min_points = []
			for point in cleaned_data:

				target = [width, height]
				dist = taxicab_dist(target, point)
				if dist == min_dist:
					min_points.append(point)
				elif dist < min_dist:
					min_points = [point]
					min_dist = dist
			
			if len(min_points) == 1:  # skip if multiple points
				min_point = min_points[0]
				bank[str(min_point)] = bank.setdefault(str(min_point), 0) + 1
	return bank

bank_small = calculate_area(10)
bank_big = calculate_area(20)

max_area = 0
for key in bank_small:
	if bank_small[key] == bank_big[key]:
		if max_area < bank_small[key]:
			max_area = bank_small[key]
print(max_area)
