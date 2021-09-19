import sys


def maxi(a, b):
    if a <= b:
        a = b
    return a


def calcuNums(text1, text2):
    n2 = len(text2)
    max = 0
    for i in range(n2):
        for j in range(i, n2):
            str = text2[i:j+1]
            if str in text1:
                n = len(str)
                max = maxi(max, n)

    return max


if __name__ == '__main__':
    # line = sys.stdin.readline().strip()
    # a = line.split(",")
    # text1 = a[0]
    # text2 = a[1]
    text1 = "abc"
    text2 = "def"
    print(calcuNums(text1, text2))
