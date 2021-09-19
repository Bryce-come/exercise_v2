'''
2
cabac
a
'''

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        ans.append(line)
ans2 = []
for str1 in ans:
    s1 = list(str1)
    n = len(s1)
    if n == 1:
        ans2.append(str1)
    else:
        try:
            for i in range(n//2 - 1):
                if s1[i] == s1[-i-1]:
                    temp = s1[i]
                    s1[i] = s1[i + 1]
                    s1[i + 1] = temp
                    str2 = ''.join(s1)
                    ans2.append(str2)
        except:
            pass

print(ans2)
for item in ans2:
    n = len(item)
    if n == 1:
        print("NO")
    for i in range(n//2 - 1):
        if item[0] == item[-1]:
            print('NO')
        else:
            print('YES')