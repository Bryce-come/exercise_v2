def minmumNumberOfHost(n, startEnd):
    ans = 1
    for i in range(n):
        a, b = startEnd[i][0], startEnd[i][1]
        for j in range(i + 1, n):
            c, d = startEnd[j][0], startEnd[j][1]
            if c > a and c < b:
                ans += 1
    return ans


if __name__ == '__main__':
    n = 2
    startEnd = [[1, 2], [2, 3]]
    print(minmumNumberOfHost(n, startEnd))
