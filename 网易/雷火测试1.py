'''
15
5
1 1
2 2
3 3
2 1
2 3
'''
import sys
if __name__ == "__main__":
    r = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        ans.append(values)
    print(ans)