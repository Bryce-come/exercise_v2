def subsequence(n, array):
    max = 0
    for i in range(n):
        for j in range(i + 2, n):
            sum = array[i] + array[j]
            max = max if max > sum else sum
    return max


if __name__ == '__main__':
    n = 3
    array = [1, 2, 3]
    print(subsequence(n, array))
