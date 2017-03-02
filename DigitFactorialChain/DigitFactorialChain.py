import time
start = time.time()
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
MAX = 2177281
numbers = [-1 for i in range(MAX+1)]
chain_list = [[] for i in range(61)]
def digit_factorial_sum(n):
    if n == 0:
        return 1
    ret = 0
    while n > 0:
        ret += factorial[n%10]
        n /= 10
    return ret
def solution(n, l):
    if numbers[n] == -1:
        numbers[n] = 0
        l.append(n)
        return solution(digit_factorial_sum(n), l)
    elif numbers[n] == 0:
        l.append(n)
        return True, l
    else:
        l.append(numbers[n])
        return False, l
for k in range(1000001):
    if numbers[k] == -1:
        l = solution(k, list())
        if l[0]:
            repeating = []
            non_repeating = []
            for i, j in enumerate(l[1]):
                if l[1].count(j) == 2:
                    repeating = l[1][i:]
                    non_repeating = l[1][:i]
                    break
            length_cycle = len(repeating)
            for m in repeating[:length_cycle-1]:
                numbers[m] = length_cycle - 1
            length = len(non_repeating) - 1
            while length >= 0:
                numbers[non_repeating[length]] = length_cycle
                length_cycle += 1
                length -= 1
            
        else:
            _list = l[1]
##            print "False->", _list
            lenght_list = len(_list)
            length_cycle = _list[lenght_list-1]
##            print "length_cycle: ", length_cycle
##            _list.pop(lenght_list-1)
            lenght_list -= 1
            for o in _list[:lenght_list]:
                numbers[o] = length_cycle + lenght_list
                lenght_list -= 1
    chain_list[numbers[k]-1].append(k)
##    print k, numbers[k], l[1]
for _ in range(int(raw_input())):
    n, l = map(int, raw_input().split())
    flag = True
    for i in chain_list[l-1]:
        if i <= n:
            flag = False
            print i,
    if flag:
        print -1
    else:
        print 

