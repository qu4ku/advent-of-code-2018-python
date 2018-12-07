"""
day 04:
https://adventofcode.com/2018/day/4
"""

import re
from collections import Counter

# Load data
with open('day04-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

# First part
data = sorted(data)

# Crate a dictionary of guards pointing to the lists
# of minutes [even index = start, odd index = end]
# format: 'guard': [1, 23, 45, 55]
guards = {}  
for line in data:
	if 'Guard' in line:
		current_guard = re.findall(r'(?<=#)\d+', line)[0]
		guards.setdefault(current_guard, [])
	else:
		time = re.findall(r'(?<=:)\d+', line)[0]
		guards[current_guard].append(time)

summary = []
for guard in guards.items():
	guard_id = guard[0]
	guard_list = [int(x) for x in guard[1]]
	
	if not guard_list:
		continue

	# generate list of particular minutes that guard was asleep
	# format: [(total_minutes, (minute, frequency), guard_id),]
	guard_minute_list = []
	for i in range(0, len(guard_list), 2):
		for minute in range(guard_list[i], guard_list[i+1]):
			guard_minute_list.append(minute)

		total = len(guard_minute_list)
		counter = Counter(guard_minute_list).most_common(1)[0]
		summary.append((total, counter, int(guard_id)))

# sort summary by total
sorted_summary = sorted(summary, reverse=True)
ans = sorted_summary[0][1][0] * sorted_summary[0][2]
print(ans)

# Second part
# sort summary by biggest frequency 
sorted_summary = sorted(summary, reverse=True, key=lambda x: x[1][1])
ans = sorted_summary[0][1][0] * sorted_summary[0][2]
print(ans)
