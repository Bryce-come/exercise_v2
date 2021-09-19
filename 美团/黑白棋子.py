a = eval(input())
b = eval(input())

for x, y in b:
    x -= 1
    y -= 1
    if x > 0:
        a[x - 1][y] = 1 - a[x - 1][y]
    if x < 3:
        a[x + 1][y] = 1 - a[x + 1][y]
    if y > 0:
        a[x][y - 1] = 1 - a[x][y - 1]
    if y < 3:
        a[x][y + 1] = 1 - a[x][y + 1]

print(str(a).replace(" ", ""))