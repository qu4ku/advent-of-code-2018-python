"""
day 05:
https://adventofcode.com/2018/day/5
"""

import re
from collections import Counter

# Load data
with open('day05-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]
data = data[0]

# First part

# with recursion
# def scan(data):
# 	# print(data)
# 	for i in range(len(data) - 1):
# 		if (data[i] != data[i+1]) and (data[i].lower() == data[i+1].lower())	:		
# 			# print(data[i], data[i+1])
# 			new_data = data[:i] + data[i+2:]
# 			return scan(new_data)	
# 	return data

# data_done = scan(data)
# print(data_done)
# print(len(data_done))


def get_len(data):
	ready = False
	while not ready:
		counter = 0
		for i in range(len(data) - 1):
			if (data[i] != data[i+1]) and (data[i].lower() == data[i+1].lower()):		
				new_data = data[:i] + data[i+2:]
				data = new_data
				counter += 1
				break

		if counter == 0:
			ready = True

	# print(data)
	return len(data)  # 10766


# Second part
def data_without_unit(unit, data):
	i = 0
	while i < len(data):
		# print(i)
		if data[i].lower() == unit:
			data = data[:i] + data[i+1:]
			# print(data)
			i -= 1

		i += 1
	return data

import string

results = []
for letter in string.ascii_lowercase:
	new_data = data_without_unit(letter, data)
	results.append(get_len(new_data))

print(min(results))




