# Day 6: Let's Review
# https://www.hackerrank.com/challenges/30-review-loop/problem

T = int(input())

for t in range(0, T):
    S = input()
    even = ''
    odd = ''
    for s in range(0, len(S)):
        if s % 2 == 0:
            even += S[s]
        else:
            odd += S[s]
    print('{} {}'.format(even, odd)
)
