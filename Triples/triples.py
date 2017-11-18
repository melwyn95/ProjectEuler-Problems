for T in range(int(raw_input())):
    p, q, r = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    C = map(int, raw_input().split())
    A_B = []
    for b in B:
        row = []
        for a in A:
            if b >= a:
                row.append(a+b)
        A_B.append(row)
    B_C = []
    for b in B:
        row = []    
        for c in C:
            if b >= c:
                row.append(b+c)
        B_C.append(row)
    ans = 0
    for i in range(len(B)):
        for j in A_B[i]:
            for k in B_C[i]:
                ans = (ans + j*k) % 1000000007
    print ans
