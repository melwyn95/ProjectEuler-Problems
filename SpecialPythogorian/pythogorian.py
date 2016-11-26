import math
t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    maximum = -1
    for a in range(1, n/2):
        b = (n ** 2 - 2 * a * n) / (2 * n - 2 * a)
        c = n - a - b
        if a > b and c > b:
            if a ** 2 + b ** 2 == c ** 2:
                m = a * b * c
                if m > maximum:
                    maximum = m
    print maximum
