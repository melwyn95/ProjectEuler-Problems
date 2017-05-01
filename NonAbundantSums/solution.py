import math, time
#start = time.time()
N = 10 ** 5 + 7
def divisors(n):
    sqrt = int(math.sqrt(n)) + 1
    s = 1
    for i in range(2, sqrt):
        if n%i == 0:
            if i == n/i:
                s += i
            else:
                s += (i + n/i)
    return s
def bin_search(a, x, l, r):
    if l <= r:
        mid = (l+r) / 2
        if a[mid] == x:
            return True, mid
        else:
            if x > a[mid]:
                return bin_search(a, x, mid+1, r)
            else:
                return bin_search(a, x, l, mid-1)
    return False, -1
abundant = []
abundant_sum = []
for i in range(12, N + 1):
    #print i
    s = divisors(i)
    if s > i:
        #if i % 2 == 1: #print i
        abundant.append(i)
        abundant_sum.append(s)
l = len(abundant)
for _ in range(int(raw_input())):
    n = int(raw_input())
    flag = True
    for i in range(l):
        if bin_search(abundant, n-abundant[i], 0, l-1)[0]:
            print 'YES'
            flag = False
            break
    if flag: print 'NO'
#print len(abundant)
#print time.time() - start
