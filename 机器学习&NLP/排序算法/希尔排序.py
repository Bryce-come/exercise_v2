'''
选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
例如：27 33 4 6 87 66 12 231 32 99 47 38
'''


def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]  # 记录要出入的数
            while (j >= 0 and arr[j] > temp):  # 从后向前，找打比其小的数的位置
                arr[j + d] = arr[j]  # 向后挪动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = ShellSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
