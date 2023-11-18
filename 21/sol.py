from collections import defaultdict
import re
from collections import deque

OPERATORS = {
    '+' : lambda x, y : x + y,
    '-' : lambda x, y : x - y,
    '*' : lambda x, y : x * y,
    '/' : lambda x, y : x / y,
}
INVERSE = {
    '+' : lambda x, y : x - y,
    '-' : lambda x, y : x + y,
    '*' : lambda x, y : x / y,
    '/' : lambda x, y : x * y,
}

TREE = defaultdict()
with open("input.txt", "r") as file:
    for line in file.readlines():
        p1, p2 = line.split(':')
        if len(p2.split()) == 1:
            TREE[p1] = float(p2)
        else:
            op1, op, op2 = p2.split()
            TREE[p1] = (op1, op, op2)

def calc_at(at : str, tree):
    if isinstance(tree[at], float):
        return tree[at]

    op1, op, op2 = tree[at]
    op = OPERATORS[op]
    return op(calc_at(op1, tree), calc_at(op2, tree))

def get_path(node, tree):
    Q = deque([('root', [],)])
    while Q:
        at, path = Q.pop()
        if at == node:
            return path
        if not isinstance(tree[at], float):
            left, op, right = tree[at]
            Q.append((left, path+[right]))
            Q.append((right, path+[left]))
    assert False

def back_track(node, tree):
    path = get_path(node, tree)
    left, op, right = tree['root']
    known = path[0]
    at = left if known == right else right
    value = calc_at(known, tree)
    i = 1

    while at != 'humn':
        left, op, right = tree[at]
        inv = INVERSE[op]
        known = path[i]
        i += 1
        if known == left:
            at = right
            known_val = calc_at(known, tree)
            # Handle non commutative operators
            if op == '/':
                value = known_val / value
            elif op == '-':
                value = known_val - value
            else:
                value = inv(value, known_val)
        if known == right:
            at = left
            value = inv(value, calc_at(known, tree))
    
    return value
        
print(int(calc_at('root', TREE)))
value = back_track('humn', TREE)
print(int(value))

TREE['humn'] = value
left, op, right = TREE['root']
TREE['root'] = (left, '-',  right)
assert calc_at('root', TREE) == 0