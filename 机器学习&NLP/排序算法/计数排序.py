'''
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
例如：27 33 4 6 87 66 12 231 32 99 47 38
'''


def CountSort(lst):
    n = len(lst)
    num = max(lst)
    count = [0] * (num + 1)
    for i in range(0, n):
        count[lst[i]] += 1
    arr = []
    for i in range(0, num + 1):
        for j in range(0, count[i]):
            arr.append(i)
    return arr


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = CountSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
