s = input().strip()
n = len(s)


def getnum(s, n):
    for i in range(n // 2, 0, -1):
        c = 0
        for j in range(0, n - i):
            if s[j] != s[j + i]:
                if n - j <= 2 * i:
                    break
                c = 0
            else:
                c += 1
                if c == i:
                    return c * 2
    return 0


print(getnum(s, n))
######################

def decode(stack):
    val1 = stack.pop()
    val2 = stack.pop()
    ch = chr(int(val1 + val2, 16))
    if ch == '%':
        stack = decode(stack)
    else:
        stack.append(ch)
    return stack


def main():
    N = int(input())
    for i in range(N):
        s = str(input())
        stack = []
        for c in s[::-1]:
            if c != '%':
                stack.append(c)
            else:
                stack = decode(stack)
        print("".join(stack[::-1]))


main()
##################
import math


class Solution():
    def f(self, x, a, b):
        a3 = 3 * a
        min_p = min(a3, b)
        base_p = x // 1500 * min_p
        rest = x % 1500
        use_a = math.ceil(rest / 500) * a
        rest_p = min(use_a, b)
        return base_p + rest_p


n = int(input().strip())
sol = Solution()
for i in range(n):
    line = [int(item) for item in input().strip().split()]
    res = sol.f(*line)
    print(res)
# 或者

import math
t = int(input())
for _ in range(t):
    min_money = 0
    a,b,c = list(map(int,input().split()))
    part_1 = (a // 1500) * min(3*b,c)
    part_2 = min(c,math.ceil((a%1500)/500) * b)
    print(part_1 + part_2)

#############

import sys

def min_len(nums, subnums, lengths):

    sub_dict = {}
    for i in range(len(subnums)):
        sub_dict[subnums[i]] = -1

    min_length = len(nums) + 1
    find_num = 0
    pos = 0
    while pos < len(nums):
        if sub_dict.get(nums[pos], -2) != -2:
            if sub_dict[nums[pos]] == -1:
                find_num += 1
            sub_dict[nums[pos]] = pos

        if find_num == len(subnums):
            max_pos = max(sub_dict.values())
            min_pos = min(sub_dict.values())
            length = max_pos - min_pos + 1
            if length < min_length:
                min_length = length
            sub_dict[nums[min_pos]] = -1
            find_num -= 1
        pos += 1

    min_length = min_length if min_length != len(nums) + 1 else 0

    lengths.append(min_length)


total = int(input())
lengths = []
for i in range(total):

    sys.stdin.readline()
    nums = sys.stdin.readline().strip().split()
    nums = list(map(int, nums))
    sys.stdin.readline()
    subnums = sys.stdin.readline().strip().split()
    subnums = list(map(int, subnums))
    min_len(nums, subnums, lengths)
for length in lengths:
    print(length)
