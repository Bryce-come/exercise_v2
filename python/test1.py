'''样例输入
5
NLXY299 1561 02:11
KZHJ784 994 06:18
KRYH108 1883 12:57
TWNT020 1659 16:06
MKBS722 758 16:21
样例输出
758 16:21 MKBS722
994 06:18 KZHJ784
1561 02:11 NLXY299
1659 16:06 TWNT020
1883 12:57 KRYH108
02:11 1561 NLXY299
06:18 994 KZHJ784
12:57 1883 KRYH108
16:06 1659 TWNT020
16:21 758 MKBS722
提示
1<=n<=400'''
import numpy as np

Q = int(input())  # 先输入一个数字代表需要输入几行，比如Q=4，那么就需要再输入4行数据
q1 = []
for i in range(Q):
    q1.append(list(map(str, input().split())))
a = np.array(q1)
a1 = a[np.lexsort(a.T)]

def func1(Q, arr, m, n):
    for i in range(Q):
        temp = arr[i][m]
        arr[i][m] = arr[i][n]
        arr[i][n] = temp
    return arr

def fun2c(Q, arr, k):# 转int
    for i in range(Q):
        int(arr[i][k])
    return arr




c = func1(Q, a, 1, 2)
d = func1(Q, c, 0, 2)

print(d)
b = func1(Q, a1, 0, 2)
print(b)