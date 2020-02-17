
def solve(x, y, acc, s_acc):
    try:
        return s_acc[str(x) + "_" + str(y)]
    except:
        pass

    if x < 0 or y < 0: return 0
    if x == 0 and y == 0: return 1
    # down
    down = solve(x-1, y, acc + 1, s_acc)
    # right
    right = solve(x, y-1, acc + 1, s_acc)

    return down + right

MOD = (10 ** 9) + 7

solution_cache = {}

for row in range(1, 501):
    for col in range(1, 501):
        n = solve(row, col, 0, solution_cache)
        solution_cache[str(row) + "_" + str(col)] = n

for T in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    print solution_cache[str(n) + "_" + str(m)] % MOD
