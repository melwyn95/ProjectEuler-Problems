import math, time
start = time.time()
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
print l
N = 28123 + 1 -100
for _ in range(N, N+101):#int(raw_input())):
    n = _#int(raw_input())
    for i in range(l):
        if bin_search(abundant, n-abundant[i], 0, l-1)[0]:
            print n
            break
#print len(abundant)
print time.time() - start




'''

import math#, time
#start = time.time()
N = 10 ** 5 + 1
def divisors(n):
    sqrt = int(math.sqrt(n)) + 1
    div = [1]
    s = 1
    for i in range(2, sqrt):
        if n%i == 0:
            s += (i + n/i)
            div.append(i)
            div.append(n/i)
    return div, s
def bin_search(a, x, l, r):
    if not x:
        return False, -1
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
def closest(a, x, l, r):
    if l <= r:
        mid = (l+r) / 2
        if a[mid] - x <= 10 and a[mid] - x >= 0:
            return True, mid
        else:
            if x > a[mid]:
                return closest(a, x, mid+1, r)
            else:
                return closest(a, x, l, mid-1)
    return False, -1
abundant = []
abundant_sum = []
for i in range(12, N + 1):
    #print i
    div, s = divisors(i)
    if s > i:
        #if i % 2 == 1: #print i
        abundant.append(i)
        abundant_sum.append(s)
l = len(abundant)
for _ in range(int(raw_input())):
    n = int(raw_input())
    b = bin_search(abundant, n, 0, l-1)
    if b[0]:
        index = b[1] - 1
        flag = False
        for i in range(index, -1, -1):
            if bin_search(abundant, (n-abundant[i]), 0, l-1)[0]:
                print 'YES'
                flag = True
                break
        if not flag:
            print 'NO'
    else:
        index = closest(abundant, n, 0, l-1)[1]
        flag = False
        for i in range(index, -1, -1):
            if (n-abundant[i]) < 0: continue
            if bin_search(abundant, (n-abundant[i]), 0, l-1)[0]:
                print 'YES'
                flag = True
                break
        if not flag:
            print 'NO'    

#print len(abundant)
#print time.time() - start



'''
