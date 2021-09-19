def islandPerimeter(grid):
    # write code here
    m = len(grid[0])
    n = len(grid)
    ans = 0
    kk = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                ans += 1  # ans 代表一共有多少个陆地
                try:
                    if grid[i + 1][j]:
                        kk += 1
                except:
                    pass
                try:
                    if grid[i - 1][j] and i - 1 >= 0:
                        kk += 1
                except:
                    pass
                try:
                    if grid[i][j + 1]:
                        kk += 1
                except:
                    pass
                try:
                    if grid[i][j - 1] and j - 1 >= 0:
                        kk += 1
                except:
                    pass
    return ans * 4 - kk


# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0]]
grid = [[1]]
print(islandPerimeter(grid))
