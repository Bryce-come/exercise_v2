'''
输入2个正整数，空格分隔，第一个代表人数N，第二个代表M：
输出一个int数组，每个数据表示原来在队列中的位置用空格隔开，表示出列顺序：
输入举例：6 3
输出举例：3 6 4 2 5 1
解释：6个人排成一排，原始位置编号即为1-6。最终输出3 6 4 2 5 1表示的是原来编号为3的第一个出列，编号为1的最后一个出列。
使用队列可以将复杂度降到Ｏ(1).
'''


def solution(N, M):
    from collections import deque
    que = deque(list(range(1, N + 1)))
    i = 0
    while que:
        i += 1
        if i % M == 0:  # 如果是M的倍数，移出队列并打印
            print(que.popleft(), end=" ")
        else:  # 否则把队首放到队尾
            que.append(que.popleft())


N, M = [int(i) for i in input().split()]
solution(N, M)
