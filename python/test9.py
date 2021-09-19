'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
'''
import sys


n = int(sys.stdin.readline().strip())
q1 = []
for i in range(n):
    line = sys.stdin.readline().strip()
    q1.append(line)

for item in q1:
    if 'o' in item or 'y' in item or 'e' in item or 'a' in item or 's' in item:
        item.replace('y', '1')
        print(item)
    else:
        print("整数")