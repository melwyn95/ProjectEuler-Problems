import math
n, k = map(long, raw_input().split())
pent = lambda x : x*(3*x-1)/2
a = [pent(i) for i in range(1, n+1)]
for i in range(k, n):
    minimum = a[i]-a[i-k]
    maximum = a[i]+a[i-k]
    s = (math.sqrt(1+24*maximum)+1)/6
    q = (math.sqrt(1+24*minimum)+1)/6
    if math.ceil(s) == math.floor(s) or math.ceil(q) == math.floor(q):
        print a[i]
