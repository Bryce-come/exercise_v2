'''
回文字符串就是正读和反读都一样的字符串，如“viv”、“nexen”、“12321”、“qqq”、“翻身把身翻” 等。
给定一个非空字符串 str，在最多可以删除一个字符的情况下请编程判定其能否成为回文字符串；如果可以则输出首次删除一个字符所能得到的回文字符串，如果不行则输出字符串 "false" 。

输入：abda

输出：ada
'''


def isHuiWen(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    word = input()
    wordNum = len(word)
    flag = False
    wordCopy = word[1:]
    if isHuiWen(word):
        print(wordCopy)
        flag = True
    else:
        for i in range(1, wordNum):
            wordCopy = word[:i] + word[i + 1:]  # 把i这个位置的字符扣掉
            if isHuiWen(wordCopy):
                print(wordCopy)
                flag = True
                break
    if not flag:
        print("false")
