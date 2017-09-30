# Loops
# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if i > 0:
            print(i*i)
        else:
            print(i)
