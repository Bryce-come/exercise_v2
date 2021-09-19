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
from collections import deque
def solution():
    n = int(input().strip())
    y0, x0, y1, x1 = [int(x) for x in input().split(" ")]
    M = []
    step = 0
    flag = 0
    for _ in range(n):
        M.append([x for x in input().strip()])
    print(M)

    que = deque([[x0, y0]])
    M[x0][y0] = "0"
    while que:
        c = len(que)
        step += 1
        for _ in range(c):
            cur_x, cur_y = que.popleft()
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x, next_y = cur_x + a, cur_y + b
                if next_x == x1 and next_y == y1:
                    if M[next_x][next_y] not in "0#@":
                        print(step)
                        flag = 1
                        return
                    else:
                        print(-1)
                        return
                if 0 <= next_x < n and 0 <= next_y < n and M[next_x][next_y] not in "0#@":
                    que.append([next_x, next_y])
                    M[next_x][next_y] = "0"
    if flag == 0:
        print(-1)
solution()