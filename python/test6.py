# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
import sys
import re


def calcuNums(nums1, nums2):
    n = len(nums2)
    for i in range(n):
        nums1.append(nums2[i])
    return nums1


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    nums1 = list(map(int, line1.split(",")))

    line2 = sys.stdin.readline().strip()
    nums2 = list(map(int, line2.split(",")))
    nums3 = calcuNums(nums1, nums2)
    nums4 = sorted(nums3)
    str1 = str(nums4)
    str2 = re.sub(" ", "", str1)
    str3 = re.sub("\[||\]", "", str2)
    print(str3)
