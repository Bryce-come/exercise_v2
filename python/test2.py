import numpy as np

a = np.array([[2, 7, 4, 2],
              [35, 9, 1, 5],
              [22, 12, 3, 2]])
print('a:')
print(a)

# 1按最后一列顺序排序
print('按最后一列顺序排序:')
print(a[np.lexsort(a.T)])
print('')

# 2按最后一列逆序排序
print('按最后一列逆序排序:')
print(a[np.lexsort(-a.T)])
print('')

# 3按第一列顺序排序
print('按第一列顺序排序:')
print(a[np.lexsort(a[:, ::-1].T)])
print('')

# 4按最后一行顺序排序
print('按最后一行顺序排序:')
print(a.T[np.lexsort(a)].T)
print('')

# 5按第行顺序排序
print('按第一行顺序排序:')
print(a.T[np.lexsort(a[::-1, :])].T)