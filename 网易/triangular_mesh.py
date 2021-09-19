'''
给定一个N个顶点，M个三角形组成的平面连通三角网格，需要你调整所有三角形索引的顶点顺序，
使得所有三角形都和输入的第一个三角形具有相同的朝向，并且在每个三角形内部，序号最小的顶点放在首位。

输入：
6 4
3 2 4
1 3 2
3 6 5
5 3 4

输出：
2 4 3
1 2 3
3 5 6
3 4 5

'''


class Triangle(object):
    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C

    # edge(0~2): AB BC CA
    # edgeinv(0~2) BA CB AC
    def edge(self, ii):
        if ii == 0:
            return (self.A, self.B)
        elif ii == 1:
            return (self.B, self.C)
        else:
            return (self.C, self.A)

    def edgeinv(self, ii):
        if ii == 0:
            return (self.B, self.A)
        elif ii == 1:
            return (self.C, self.B)
        else:
            return (self.A, self.C)

    def reorder(self, order):
        # put minimum first and reorder
        A, B, C = self.A, self.B, self.C
        if A < B and A < C:
            return (A, B, C) if order == 1 else (A, C, B)
        elif B < A and B < C:
            return (B, C, A) if order == 1 else (B, A, C)
        else:
            return (C, A, B) if order == 1 else (C, B, A)


def IsConnect(Tr1, Tr2):
    ## -1: connet and order inverse
    ## not connect
    ## 1 : connet and order is the same
    for i in range(3):
        for j in range(3):
            if Tr1.edge(i) == Tr2.edge(j):
                return 1
            if Tr1.edge(i) == Tr2.edgeinv(j):
                return -1
    return 0


line1 = input()
N, M = int(line1.split()[0]), int(line1.split()[1])
Triangles = []

for idx in range(M):
    line = input()
    ss = line.split()
    A, B, C = int(ss[0]), int(ss[1]), int(ss[2])
    Triangles.append(Triangle(A, B, C))

###  1: known right  0: unknown -1: known,  need inverse
order = [0 for i in range(M)]
order[0] = 1
temp = [0]
newtemp = []

while 0 in order:
    for i in [i for i in range(M) if order[i] == 0]:  # for unknown order
        for j in temp:
            connectij = IsConnect(Triangles[i], Triangles[j])
            if connectij != 0:
                # find connected triangle
                order[i] = -1 * order[j] * connectij
                newtemp.append(i)
                break
    temp = newtemp
    newtemp = []

for i in range(M):
    v1, v2, v3 = Triangles[i].reorder(order[i])
    print(v1, v2, v3)
