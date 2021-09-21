'''
有n个盒子排成了一行，每个盒子上面有一个数字a[i]，表示在该盒子上的人最多能向右移动a[i]个盒子
（比如当前所在盒子上的数字是3，则表示可以一次向右前进1个盒子，2个盒子或者3个盒子）。
输入 ：2 2 3 0 4 => 表示现在有5个盒子，上面的数字分别是2, 2, 3, 0, 4。
输出：跳法2的步骤数最少，所以输出最少步数：2。
跳法1：盒子1 -> 盒子2 -> 盒子3 -> 盒子5，共3下
跳法2：盒子1 -> 盒子3 -> 盒子5，共2下
'''


def solution(step_list):
    n = len(step_list)
    max_num = 0
    cnt = 0
    end = 0
    for i in range(n - 1):
        if i <= max_num:
            max_num = max(max_num, i + step_list[i])
            # if max_num>=n-1
            if i == end:
                end = max_num
                cnt = cnt + 1
    return cnt if max_num >= n - 1 else -1


step_list = [int(i) for i in input().split()]
print(solution(step_list))
