# Day 5: Loops
# https://www.hackerrank.com/challenges/30-loops/problem

n = int(input())

for i in range(0, 10):
    r = n * (i + 1)
    print('{} x {} = {}'.format(n, i+1, r))

