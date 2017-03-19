import math
for _ in range(int(raw_input())):
    n = int(raw_input())
    a = 1 + 8 * n
    s = int(math.sqrt(a))
    if s**2 != a:
        print -1
    else:
        print s/2
