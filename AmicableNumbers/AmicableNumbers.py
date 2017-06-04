import time

n = 100000 + 7
numbers = [1 for i in range(n)]
amicable = []

for i in range(2, (n/2) + 1):
    for j in range(2*i, n, i):
        numbers[j] += i

for i in range(100, n):
    b = numbers[i]
    if numbers[i] < n and numbers[b] == i and i != b:
        amicable.append(i)

numbers = [0 for i in range(n)]
for i in amicable:
    numbers[i] = i

answer = [numbers[0]]

for i in range(1, len(numbers)):
    answer.append(answer[i-1]+numbers[i-1])

for _ in range(int(raw_input())):
    print answer[int(raw_input())]
