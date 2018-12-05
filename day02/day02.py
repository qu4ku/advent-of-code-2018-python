"""
day 01:
https://adventofcode.com/2018/day/1
"""

from collections import Counter


# Load data
with open('day02-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

# First part
twos = 0
threes = 0


for id_num in data:
	if 2 in Counter(id_num).values():
		twos += 1
	if 3 in Counter(id_num).values():
		threes += 1
checksum = twos * threes
print(checksum)  # 8715


# Second part
ids_len = len(data)
id_len = len(data[0])
for i in range(ids_len):
	for j in range(i + 1, ids_len):
		same_letters = ''
		for k in range(len(data[i])):
			if data[i][k] == data[j][k]:
				same_letters += data[i][k]
		good_answer = len(same_letters) == id_len - 1
		if good_answer:
			print(same_letters)  # fvstwblgqkhpuixdrnevmaycd
			break  


