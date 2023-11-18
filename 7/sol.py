with open("input.txt", "r") as file:
	lines = file.read().split("\n")
	lines = list(filter(lambda x : x != "$ ls", lines))
	lines = list(map(lambda x : x.split(' '), lines))

from collections import defaultdict
sizes = defaultdict(int)
path = []

for line in lines:
	if line[0] == '$' and line[-1] != '..':
		path.append(line[-1])
		
	elif line[0] == '$' and line[-1] == '..':
		path.pop()

	elif line[0] != 'dir':
		size = int(line[0])
		for i, folder in enumerate(path):
			parent_path = '\\'.join(path[:i+1])
			sizes[parent_path] += size

# Part one
total = 0
for size in sizes.values():
	if size <= 100_000:
		total += size
		
print(total)

# Part two
used = sizes['/']
max_used = 70_000_000 - 30_000_000
need_to_free = used - max_used
smallest = used
for size in sizes.values():
	if size >= need_to_free and size < smallest:
		smallest = size

print(smallest)