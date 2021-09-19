'''
第一行表示矩阵大小 n，5 <n < 10000
第二行表示起点和终点的坐标
第三行起是一个用矩阵表示的游戏地图，其中#或者@表示障碍物，其他字母、非0数字、以及符号+、-、* 等等均表示普通可达格子，共有 n 行  n 列

输出最优路径的长度；若无法到达，则输出-1

输入：
15
0 7 7 7
*5#++B+B+++++$3
55#+++++++###$$
###$++++++#+*#+
++$@$+++$$$3+#+
+++$$+++$+4###+
A++++###$@+$++A
+++++#++$#$$+++
A++++#+5+#+++++
+++$$#$++#++++A
+++$+@$###+++++
+###4+$+++$$+++
+#+3$$$+++$##++
+#*+#++++++#$$+
$####+++++++$##
3$+++B++B++++#5

输出：
13
'''


def dfs(x, y, grid, endx, endy, visited, count):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] in "#@" \
            or (visited[x][y] != 0 and visited[x][y] <= count):
        return
    visited[x][y] = count
    if x == endx and y == endy:
        return
    dfs(x, y + 1, grid, endx, endy, visited, count + 1)
    dfs(x, y - 1, grid, endx, endy, visited, count + 1)
    dfs(x - 1, y, grid, endx, endy, visited, count + 1)
    dfs(x + 1, y, grid, endx, endy, visited, count + 1)


if __name__ == "__main__":
    n = int(input())
    [starty, startx, endy, endx] = list(map(int, input().split()))
    road = []
    for i in range(n):
        road.append(list(input()))
    visited = [[0] * n for _ in range(n)]
    print(visited)
    dfs(startx, starty, road, endx, endy, visited, 1)
    print(visited[endx][endy] - 1)
