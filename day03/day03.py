"""
day 03:
https://adventofcode.com/2018/day/3
"""

# Load data
with open('day03-input.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

# First part
def parse_data(data):
	"""Takes list of strings and convert it to list of dicts"""
	data_list = []
	for line in data:
		nr, _, lt, wh = line.split()
		nr = int(nr[1:])
		l, t = [int(x.replace(':', '')) for x in lt.split(',')]
		w, h = [int(x) for x in wh.split('x')]
		data_list.append({
			'left': l,
			'top': t,
			'width': w,
			'height': h,
		}) 
	return data_list


def propagate_fabric(size, data):
	fabric = []
	row = [0 for x in range(size)]
	for x in range(size):
		fabric.append(row.copy())

	for item in data:
		for x in range(item['left'], item['left'] + item['width']):
			for y in range(item['top'], item['top'] + item['height']):
				fabric[y][x] += 1
	return fabric


def how_many_double_covered(fabric):
	inch_counter = 0
	size = len(fabric)
	for x in range(size):
		for y in range(size):
			if fabric[x][y] > 1:
				inch_counter += 1
	return inch_counter


data = parse_data(data)
fabric = propagate_fabric(1000, data)
print(how_many_double_covered(fabric))  # 110546


# Second part
for i, item in enumerate(data):
	flag = True
	for x in range(item['left'], item['left'] + item['width']):
		for y in range(item['top'], item['top'] + item['height']):
			if fabric[y][x] != 1:
				flag = False
				break
	if flag:
		print(i + 1)  # 819