def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    window = set()
    left = 0
    max_len = 0
    cur_len = 0
    for ch in s:
        # 从前向后删除，直到删除了ch
        while ch in window:
            window.remove(s[left])
            left += 1
            cur_len -= 1
        # 添加ch
        window.add(ch)
        cur_len += 1
        # 更新长度
        max_len = max(max_len, cur_len)
    return max_len


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 2, 3, 2, 2]
    print(lengthOfLongestSubstring(arr))
