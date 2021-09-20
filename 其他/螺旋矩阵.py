def Spiralmatrix(Dimension):
    # 定义一个二维矩阵
    array_lists = [[0 for j in range(Dimension)] for i in range(Dimension)]
    # 定义开始的值
    num = 1
    # 开始螺旋赋值
    for i in range(Dimension // 2 + 1):  # 0 1 2
        # 上边赋值
        for j in range(i, Dimension - i):
            array_lists[i][j] = num
            num += 1
        # 右边赋值
        for j in range(i + 1, Dimension - i):
            array_lists[j][Dimension - i - 1] = num
            num += 1
        # 下边赋值
        for j in range(Dimension - i - 2, i, -1):
            array_lists[Dimension - i - 1][j] = num
            num += 1
        # 左边赋值
        for j in range(Dimension - i - 1, i, -1):
            array_lists[j][i] = num
            num += 1
    # 打印结果
    for i in array_lists:
        for j in i:
            print(j, end='\t')
        print()


if __name__ == "__main__":
    # num = int(input('please input num: '))
    num = 4
    Spiralmatrix(num)
