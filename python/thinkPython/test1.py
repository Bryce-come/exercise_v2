# fin = open('words.txt')
#
# for line in fin:
#     # 去掉转义字符
#     word = line.strip()
#     print(word)

print('-----------')
# x = 5
#
#
# def func_a():
#
#     return x
#
#
# def func_b():
#     global x
#     x = x + 1
#     return x
#
# print(func_a())
#
# print(func_b())
print('------------')
# a = 3
#
# b = 66
#
# a, b = b, a
# print(a, b)
print('----------')

# s = 'abc'
# t = [1, 2, 3]
# zip(s, t)
# print(zip())
# for item in zip(s, t):
#     print(item)
print('-------------')
# import string
#
# print(string.punctuation)
# import os
#
# print(os.path.abspath('words.txt'))

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])  # 显示对象
# [640, 480]是窗口大小，单位像素
screen.fill([255, 255, 255])  # 用白色填充窗口背景
pygame.draw.rect(screen, [255, 0, 0], [150, 200, 300, 200], 0)  # 画一个矩形
'''
第一个参数：在哪个表面（surface/screen）画圆
第二个参数： 用什么颜色，[255, 0, 0]为红色
第三个： 矩形的位置和大小(left, top, width, height)这是四个参数
分别是 左上角的坐标，宽和高
第四个： 线宽 如果参数值为0，那么表示圆是完全填充的
'''
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
