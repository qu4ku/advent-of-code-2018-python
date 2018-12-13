"""
day 06:
https://adventofcode.com/2018/day/6
"""


# Load data

with open('day06-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

cleaned_data = []
for line in data:
	line = [int(x) for x in line.split(', ')]
	cleaned_data.append(line)

def taxicab_dist(v1, v2):
	return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])


max_width = sorted(cleaned_data, key=lambda x: x[0], reverse=True)[0][0]
min_width = sorted(cleaned_data, key=lambda x: x[0])[0][0]
max_height = sorted(cleaned_data, key=lambda x: x[1], reverse=True)[0][1]
min_height = sorted(cleaned_data, key=lambda x: x[1])[0][1]


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


def solve_first_part():
	bank_small = calculate_area(10)
	bank_big = calculate_area(20)

	max_area = 0
	for key in bank_small:
		if bank_small[key] == bank_big[key]:
			if max_area < bank_small[key]:
				max_area = bank_small[key]

	return max_area

print(solve_first_part())



# Second part
def calculate_total_distance(target, points):
	total_distance = 0
	for point in points:
		total_distance += taxicab_dist(target, point)

	return total_distance

def solve_second_part():
	counter = 0
	for width in range(0, max_width):
		for height in range(0, max_height):
			target = [width, height]
			total_distance = calculate_total_distance(target, cleaned_data)
			if total_distance < 10000:
				counter += 1

	return counter

print(solve_second_part())