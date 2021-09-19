# import time
#
# print(time.time())
# print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))

print("--------------------")
a = [3, 4, 5, 3, 1, 2, 8, 4]

print(sorted(a))
print(sorted(a, reverse=True))

# 可以直接生成一个四则运算器，输入字符串公式
# x = input('输入字符串公式')
#
# print(eval(x))
print("--------------------")
# lambda函数可以接受任意多个参数，然后返回单个表达式的值；
p = lambda x, y: x + y
print(p(4, 6))

num = [1, 2, 3, 4]

a = map(lambda x: x * x, num)
print(a)  # 直接使用print只会显示类型
print(list(a))  # 使用print(list())进行转换之后显示，可以看到具体结果
print("--------------------")
from functools import reduce

chars = ['a', 'p', 'p', 'l', 'e']
a = reduce(lambda x, y: x + y, chars)
print(a)
# 输出：apple
print("--------------------")
# 过滤掉列表中的某些数
nums = [1, 2, 3, 4, 5, 6]
a = filter(lambda x: x % 2 != 0, nums)
print(list(a))
# 输出：

chars = chars = ['apple', 'watermelon', 'pear', 'banana']
a = filter(lambda x: 'w' in x, chars)
print(list(a))
# 输出：['watermelon']
print("--------------------")
# 同时打印序列里的每一个元素和它对应的顺序号
chars = ['apple', 'watermelon', 'pear', 'banana']
for i, j in enumerate(chars):
    print(i, j)
print("--------------------")

print("--------------------")
