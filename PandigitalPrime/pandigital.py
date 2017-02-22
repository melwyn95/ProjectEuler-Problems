import math
def num(l):
    if l == None:
        return 0
    n = 0
    for i in range(len(l)):
        n *= 10
        n += l[i]
    return n
def is_prime(n):
    sqrt = int(math.sqrt(n) + 1)
    for i in range(2, sqrt):
        if n%i == 0:
            return False
    return True
def new_tree(n, q, so_far):
    so_far.append(n)
    if len(q) == 1:
        return so_far
    q.remove(n)
    for number in q:
        ret_num = num(new_tree(number, list(q), list(so_far)))
        if ret_num%2 > 0:
            permutations.append(ret_num)
def generate_tree():
    for j in range(3, 10):
        for i in range(1, j+1):
            new_tree(i, list(digits[:j]), list([]))
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = []
def main():
    generate_tree()
    primes = primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    prime_permutations = []
    for permutation in permutations:
        i = 0
        flag = True
        while i < 27:
            if permutation%primes[i] == 0:
                flag = False
                break
            else:
                i += 1
        if flag and is_prime(permutation):
            prime_permutations.append(permutation)
    T = int(raw_input())
    for i in range(T):
        n = int(raw_input())
        a = -1
        for i in prime_permutations:
            if i <= n:
                a = i
            else:
                break
        print a
main()
