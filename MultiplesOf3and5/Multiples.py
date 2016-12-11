t = int(raw_input())
for _ in range(t):
    n = long(raw_input()) - 1
    answer = ((n // 3 * (n // 3 + 1)) // 2 ) * 3
    answer += ((n // 5 * (n // 5 + 1)) // 2 ) * 5
    answer -= ((n // 15 * (n // 15 + 1)) // 2 ) * 15
    print answer
