# Day 3: Intro to Conditional Statements
# https://www.hackerrank.com/challenges/30-conditional-statements/problem

N = int(input())

if N % 2 == 1:
    print('Weird')
elif N in range(2, 5+1): # plus one to include 5
    print('Not Weird')
elif N in range(6, 20+1): # plus one to include 20
    print('Weird')
elif N > 20:
    print('Not Weird')
