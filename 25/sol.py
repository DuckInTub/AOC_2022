from functools import reduce

def add_snafu(s1, s2):
    n_to_snafu = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    max_len = max(len(s1), len(s2))
    s1, s2 = s1.rjust(max_len, "0"), s2.rjust(max_len, "0")
    assert len(s1) == len(s2)
    carry = 0
    ret = ""
    for d1, d2 in zip(reversed(s1), reversed(s2)):
        d1, d2 = snafu_to_dec(d1), snafu_to_dec(d2)
        n = d1 + d2 + carry
        digit = ((n + 2) % 5) - 2
        carry = (n - digit) // 5
        ret += n_to_snafu[digit]
    if carry != 0:
        ret += n_to_snafu[carry]
    ret = ret[::-1]
    assert snafu_to_dec(s1) + snafu_to_dec(s2) == snafu_to_dec(ret)
    return ret

def snafu_to_dec(ss):
    if not ss:
        return 0
    sm = 0
    for i, c in enumerate(reversed(ss)):
        sm += ("=-012".index(c)-2)*5**i
    return sm


with open("input.txt", "r") as file:
    nums = file.read().splitlines()
    sm = reduce(add_snafu, nums)
    print(f"Sum is: {sm}")