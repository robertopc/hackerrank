# Print Function
# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    o = ''
    for i in range(n):
        o += str(i+1)
    print(o)
