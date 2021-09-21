# 冒泡排序
'''
 * 排序法    平均时间    最差情形        稳定度 额外空间     备注
 * 冒泡     O(n2)     O(n2)     稳定    O(1)    n小时较好
 * 选择      O(n2)     O(n2)  不稳定   O(1)   n小时较好
 * 插入      O(n2)     O(n2)       稳定     O(1)    大部分已排序时较好
 * 基数      O(logRB)  O(logRB)    稳定      O(n)
 * 快速     O(nlogn)  O(n2)     不稳定 O(nlogn)    n大时较好
 * 归并      O(nlogn)  O(nlogn)  稳定      O(1)    n大时较好
 * 堆      O(nlogn)  O(nlogn)    不稳定 O(1)    n大时较好
'''
def BubbleSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = BubbleSort(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
