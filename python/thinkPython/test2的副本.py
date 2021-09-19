import os

# 返回当前工作目录
print(os.getcwd())

# 返回指定路径下的文件和目录信息
lst = os.listdir('../算法刷题')
print(lst)

# 创建目录
# os.mkdir('newdir')

# 创建多级目录
# os.makedirs('A/B/C')

# 删除目录
# os.rmdir('newdir ')

# 移除多及目录
os.removedirs('A/B/c')

# 设置当前路径
os.chdir('')
