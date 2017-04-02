import math, time
def seive(n):
    #n = 1000000 + 7
    num = [True] * n
    num[0] = num[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if num[i]:
            j = 2*i
            while j < n:
                num[j] = False
                j += i
    primes = []
    for i in range(n):
        if num[i]: primes.append(i)
    return primes
def bin_search(a, n, l, h):
    if l <= h:
        m = (l+h)/2
        if a[m] == n:
            return True
        else:
            if n < a[m]:
                return bin_search(a, n, l, m-1)
            else:
                return bin_search(a, n, m+1, h)
    return False
def r_l_digits(n, primes, l):
    d = []
    while n > 0:
        if not bin_search(primes, n, 0, l-1):
            return False
        d.append(n % 10)
        n /= 10
    return True
def l_r_digits(n, primes, l):
    no_d = -1
    t = n
    while t > 0:
        no_d += 1
        t /= 10
    den = 10 ** no_d
    while n > 0:
        if not bin_search(primes, n, 0, l-1):
            return False
        n -= (n/den)*den
        den /= 10
    return True
def is_trunc(n, primes, l):
    r_l = r_l_digits(n, primes, l)
    l_r = l_r_digits(n, primes, l)
    return r_l and l_r
start = time.time()
n = 1000000#int(raw_input())
primes = seive(n)
l = len(primes)
s = 0
for i in range(10, n):
    if is_trunc(i, primes, l):
        print i
        s += i
print s
print time.time()-start
#print is_trunc(3797, primes, l)
