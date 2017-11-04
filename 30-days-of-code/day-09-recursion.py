# Day 9: Recursion
# https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    # Complete this function
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input())
    result = factorial(n)
    print(result)

