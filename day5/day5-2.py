import numpy as np

IGNORE_DIAGONALS = False

with open("day5/day5.txt") as f:
	data = f.readlines()

array = np.zeros((1000, 1000))

for i in range(len(data)):
	points = data[i].split(' -> ')
	point1 = points[0].split(',')
	point2 = points[1].replace('\n', '').split(',')
	point1 = [int(x) for x in point1]
	point2 = [int(x) for x in point2]

	if point1[0] != point2[0] and point1[1] != point2[1] and IGNORE_DIAGONALS:
		continue

	points_list = []

	if point1[0] != point2[0]:

		# sort point1 and point2 so that point1 is always the one with the lowest x
		if point1[0] > point2[0]:
			point1, point2 = point2, point1

		# create the points in points_list with the y value empty for later
		for x in range(point1[0], point2[0] + 1):
			points_list.append([x, ''])

		if point1[1] > point2[1]:
			for i in range(len(points_list)):
				points_list[i][1] = point1[1] - i

		if point1[1] < point2[1]:
			for i in range(len(points_list)):
				points_list[i][1] = point1[1] + i

		if point1[1] == point2[1]:
			for i in range(len(points_list)):
				points_list[i][1] = point1[1]

	else:

		# sort point1 and point2 so that point1 is always the one with the lowest y
		if point1[1] > point2[1]:
			point1, point2 = point2, point1

		# create the points in points_list with the x value empty for later
		for y in range(point1[1], point2[1] + 1):
			points_list.append(['', y])

		if point1[0] > point2[0]:
			for i in range(len(points_list)):
				points_list[i][0] = point1[0] - i

		if point1[0] < point2[0]:
			for i in range(len(points_list)):
				points_list[i][0] = point1[0] + i

		if point1[0] == point2[0]:
			for i in range(len(points_list)):
				points_list[i][0] = point1[0]

	for point in points_list:
		array[point[0]][point[1]] = array[point[0]][point[1]] + 1

count = 0
for row in array:
	for item in row:
		if item > 1:
			count += 1

print(f'Total Overlaps: {count}')