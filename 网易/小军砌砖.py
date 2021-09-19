'''
输入描述：两个整数 W 和 H (2 <= W <= 30, 1 <= H <= 10)
输出描述：一个整数，所有可能建墙方式的数量。这个数量可能会大于32位整数的表示范围，请用64位整数
5 2 output 2
9 5 output 14
'''

w, h = map(int, input().split())
state = []


def dfs1(i, now):
    if 1 << w & now != 0:
        state.append(now)
        return
    for x in [2, 3]:
        if i + x > w: continue
        mask = 1 << (i + x)
        dfs1(i + x, now | mask)


dfs1(0, 0)
dp = [[1] * len(state) for _ in range(h)]
for i in range(1, h):
    for j in range(len(state)):
        dp[i][j] = 0
        for k in range(len(state)):
            if state[k] & state[j] != 1 << w: continue
            dp[i][j] += dp[i - 1][k]
res = 0
for i in range(len(state)): res += dp[h - 1][i]
print(res)
