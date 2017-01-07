def path(pattern, i, j, MAX):
    if i == MAX - 1:
        return pattern[i][j]
    else:
        return pattern[i][j] + max(path(pattern, i+1, j, MAX), path(pattern, i+1, j+1, MAX))
t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    pattern = []
    for __ in range(n):
        pattern.append(map(int, raw_input().split(" ")))
    print path(pattern, 0, 0, n)
