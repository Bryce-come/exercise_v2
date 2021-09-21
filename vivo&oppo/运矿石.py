'''
假设小v挖到了n（n<100）个矿石，每个矿石重量不超过100，为了确保一次性将n个矿石都运送出去，
一旦矿车的车厢重量不一样就需要购买配重砝码。请问小v每次最少需要购买多少重量的砝码呢?
（假设车厢足够放下这些矿石和砝码，砝码重量任选）
输入：3 7 4 11 8 10
输出：1
'''


def solution(stone_list):
    # 不用背包或者动态规划法
    left = stone_list[:len(stone_list) // 2]  # 将矿石分为两组
    right = stone_list[len(stone_list) // 2:]  # 数量差最多是1
    aver = sum(stone_list) / 2  # 平均重量（最终目的是让两组的重量最接近均重，这样二者差值最小，所需的砝码也最小！）
    for i in range(len(left)):
        for j in range(len(right)):
            if abs(sum(left) + right[j] - left[i] - aver) < abs(sum(left) - aver):
                # 如果把右边的任一矿石和左边的交换，使得左边相对于平均重量的差的绝对值变小了，那就交换！
                left.insert(i, right.pop(j))  # 把右边组的那个元素删除并加进左边组
                right.insert(j, left.pop(i + 1))  # 同理把左边组的元素加进右边组，注意是i + 1，因为刚刚多了一个元素
    return abs(sum(left) - sum(right))  # 最后只要返回两组的差的绝对值就可以了


stone_list = [int(i) for i in input().split()]
print(solution(stone_list))
