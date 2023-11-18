def change(stacks, instruction):
	a = instruction[0]
	b = instruction[1] - 1
	c = instruction[2] - 1
	moving = stacks[b][::-1][:a]
	to = stacks[c] + moving
	frm = stacks[b][:-a]
	stacks[b] = frm; stacks[c] = to
	return stacks

from functools import reduce

d = ['ZN', 'MCD', 'P']
inst = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
inst.insert(0, d)
print(inst)

print("".join(stack[-1] for stack in reduce(change, inst)))