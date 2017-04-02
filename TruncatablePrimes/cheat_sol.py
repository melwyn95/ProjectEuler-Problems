t = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
n = int(raw_input())
s = 0
for i in t:
    if i < n:
        s += i
    else:
        break
print s
