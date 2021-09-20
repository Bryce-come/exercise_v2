'''
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
例如：27 33 4 6 87 66 12 231 32 99 47 38
'''


def InsertSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = target  # 把target插到空位
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = InsertSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
