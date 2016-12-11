''' Source Code GOLD '''
''' Just randomly came up with the idea....
    Tested it .....
    It Worked.....
    Solution Accepted!!!!!!
'''

import math
primes = []
MAX = 1000007
numbers = [True] * MAX
def seive(primes):
    for i in range(2, MAX):
        if numbers[i]:
            primes.append(i)
            j = i * i
            while j < MAX:
                numbers[j] = False
                j += i
    return primes
primes = seive(primes)
#print (len(primes))
#print primes
def isPrime(n):
    d = -1
    lim = int(math.sqrt(n)) + 1
    flag = True
    for i in range(2, lim):
        if n % i == 0:
            d = i
            flag = False
            break
    return (flag, d)
def solve(n, primes):
    current_max = -1
    for i in range(len(primes)):
        if n < primes[i]:
            break
        if n % primes[i] == 0:
            current_max = primes[i]
            while n > 0 and n % primes[i] == 0:
                n /= primes[i]
    #print n, current_max
    while n > 1:
        l = isPrime(n)
        if l[0]:
            current_max = n
            break
        n /= l[1]
    return current_max
primes = seive(primes)
t = int(raw_input())
for _ in range(t):
    n = long(raw_input())
    print solve(n, primes)
