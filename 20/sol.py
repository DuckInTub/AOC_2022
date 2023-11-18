from copy import deepcopy

with open("input.txt", "r") as file:
    data = list(map(int, file.read().split("\n")))
    data = list(enumerate(data))

def solve(mix, mix_tms):
    mix = deepcopy(mix)
    for _ in range(mix_tms):
        for i in range(len(mix)):
            for j in range(len(mix)):
                if mix[j][0] == i:
                    ind, n = j, mix[j][1]
                    break
            new_ind = (ind + n + len(mix) - 1) % (len(mix) - 1)
            mix.insert(new_ind, mix.pop(ind))
    
    return mix
    



part1 = list(map(lambda x : x[1], solve(data, 1)))
print(sum(part1[(part1.index(0) + i*10**3) % len(part1)] for i in range(1, 4)))

data = list(map(lambda x : (x[0], x[1]*811589153), data))
part2 = list(map(lambda x : x[1], solve(data, 10)))
print(sum(part2[(part2.index(0) + i*10**3) % len(part2)] for i in range(1, 4)))