grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)
def solution(i, j):
    r1, r2, c1, c2, d1, d2, d3, d4 = 1, 1, 1, 1, 1, 1, 1, 1
    if i-3 >= 0:
        for k in range(4):
            r1 *= grid[i-k][j]
    if i+3 < 20:
        for k in range(4):
            r2 *= grid[i+k][j]
    if j-3 >= 0:
        for k in range(4):
            c1 *= grid[i][j-k]
    if j+3 < 20:
        for k in range(4):
            c2 *= grid[i][j+k]
    if i-3 >= 0 and j-3 >= 0:
        for k in range(4):
            d1 *= grid[i-k][j-k]
    if i+3 <20 and j+3 <20:
        for k in range(4):
            d2 *= grid[i+k][j+k]
    if i-3 >= 0 and j+3 < 20:
        for k in range(4):
            d3 *= grid[i-k][j+k]
    if i+3 <20 and j-3>=0:
        for k in range(4):
            d4 *= grid[i+k][j-k]
    return max(r1, r2, c1, c2, d1, d2, d3, d4)
m = -1
for i in range(20):
    for j in range(20):
        s = solution(i, j)
        if s > m:
            m = s
print m
