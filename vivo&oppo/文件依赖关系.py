'''
输入例子1:
"1,2,-1,1"

输出例子1:
"2,1,0,3"
'''

import heapq


class Solution:
    def compileSeq(self, input):
        # write code here
        nums = [int(x) for x in input.split(",")]
        n = len(nums)
        in_degree = [0] * n
        relation = [set() for _ in range(n)]
        res = []
        que = []

        for i in range(n):
            if nums[i] != -1:
                in_degree[i] += 1
                relation[nums[i]].add(i)

        for i in range(n):
            if in_degree[i] == 0:
                que.append(i)

        while que:
            cur = que[0]
            que = que[1:]
            res.append(cur)
            for idx in relation[cur]:
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    heapq.heappush(que, idx)
        string = ",".join([str(x) for x in res])
        return string


if __name__ == "__main__":
    sol = Solution()
    print(sol.compileSeq("1,2,-1,1"))
