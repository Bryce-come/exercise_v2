def maxLengthArray(arr):
    if arr == '':
        return 0
    n = len(arr)
    max = 0
    the_set = set()
    for i in range(n):
        while arr[i] in the_set:
            the_set.remove(arr[i])
        the_set.add(arr[i])
        m = len(the_set)
        max = max if max > m else m
    return max



if __name__ == '__main__':
    arr = [1, 2, 3, 1, 2, 3, 2, 2]
    print(maxLengthArray(arr))

