with open("test.txt", "r") as file:
	d = file.read().split('\n')
	d = [[int(c) for c in line] for line in d]

for line in d:
	print(line)

def scene_right_row(row, index : int):
	e = row[index]
	score = 0
	for i, elem in enumerate(row[index:len(row)-1]):
		if elem < e:
			score += 1
		elif elem == e:
			score += 1
			return score
		else:
			return score
	return score

print(scene_right_row([1, 5, 3, 4, 2], 0))