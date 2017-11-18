import math
import time

def seive(n):
    primes = []
    numbers = [True for i in range(n)]
    for i in range(2, int(math.sqrt(n) + 1)):
        if numbers[i]:
            j = 2*i
            while j < n:
                numbers[j] = False
                j += i
    for i, j in enumerate(numbers[2:]):
        if j: primes.append(i+2)
    return primes
def bin_eq(a, l, h, x):
    if l < h:
        m = (l + h) / 2
        if a[m] == x: return m
        else:
            if x < a[m]: return bin_eq(a, l, m-1, x)
            else: return bin_eq(a, m+1, h, x)
    return -1
def bin_lt(a, l, h, x):
    #print l, h, x, a[(l + h) / 2]
    if l <= h:
        m = (l + h) / 2
        if a[m] <= x and a[m+1] > x: return m
        else:
            if x < a[m]: return bin_lt(a, l, m-1, x)
            else: return bin_lt(a, m+1, h, x)

def brute_force_check(n, triples):
    count = 0
    for i in triples:
        if i <= n: count += 1
    return count
primes = seive(100)
print primes
triples = []
for i in primes:
    for j in primes:
        for k in primes:
            x = pow(i, 2) + pow(j, 3) + pow(k, 4)
            #if bin_eq(triples, 0, len(triples), x) == -1:
            #print primes[i] , primes[j], primes[k], x
            triples.append( x )
triples = list(set(triples))
triples.sort()
##for _ in range(int(raw_input())):
##    n = int(raw_input())
##    if n < 28: print 0
##    else:
##        index = bin_lt(triples, 0, len(triples), n)
##        while triples[index] <= n:
##            index += 1
##        print index
##s = time.time()
##for n in range(0, 1000000):
##    if n%1000 == 0: print n
##    brute_force_check(n, triples)
##    print 'Dumb Solution: ',
##    if n < 28: print 0
##    else:
##        index = bin_lt(triples, 0, len(triples), n)
##        while triples[index] <= n: index += 1
##        print index
##    print 'Brute Force Solution: '+str(brute_force_check(n, triples))
##    print '__________________________'
        
##print 'Done', str(time.time() - s)

