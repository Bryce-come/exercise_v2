'''
输入描述：
第一行包含一个正整数 n(1<=n<=20)，表示工作数量。
接下来 n 行，每行包含两个整数，分别表示第 i 项工作的 deadline 和 cost。
输出描述：
一个数字，表示钱老板最少需要推迟几天才能完成所有工作。

输入：
3
3 3
8 1
3 2
输出：
2
'''
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
cache = {}


def dfs(d, k):
    if k in cache:
        return cache[k]
    if k == (1 << n) - 1:
        return 0
    res = 1e9
    for i in range(n):
        if 1 << i & k != 0:  # 左移操作, 2的幂有关
            continue
        res = min(res, dfs(d + a[i][1], k | 1 << i) + max(0, a[i][1] + d - a[i][0]))
    cache[k] = res
    return res


print(dfs(0, 0))
