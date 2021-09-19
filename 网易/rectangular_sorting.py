'''
矩阵排序
每组输入两行输入
第一行是一个整数N （0 < N <= 100)
第二行是2*N个整数，分别是每个矩形的宽W和高H，(0 < W,H <= 100)

每组数据输出一行，2*N个整数，分别是排序后的每个矩形的宽W和高H
'''


def minWH(w1, h1):
    return w1 / h1 if w1 / h1 < h1 / w1 else h1 / w1


n = int(input(''))
rec = input('')
reclist = rec.split()
w1 = []
h1 = []
for i in range(0, n):
    w1.append(int(reclist[i * 2]))
    h1.append(int(reclist[i * 2 + 1]))

for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if w1[j] * h1[j] > w1[j + 1] * h1[j + 1]:
            w1[j], w1[j + 1] = w1[j + 1], w1[j]
            h1[j], h1[j + 1] = h1[j + 1], h1[j]

        elif w1[j] * h1[j] == w1[j + 1] * h1[j + 1]:
            if minWH(w1[j], h1[j]) < minWH(w1[j + 1], h1[j + 1]):
                w1[j], w1[j + 1] = w1[j + 1], w1[j]
                h1[j], h1[j + 1] = h1[j + 1], h1[j]

            else:
                if w1[j] > h1[j]:
                    w1[j], w1[j + 1] = w1[j + 1], w1[j]
                    h1[j], h1[j + 1] = h1[j + 1], h1[j]
for i in range(0, n):
    print('%d %d ' % (w1[i], h1[i]), end=' ')
