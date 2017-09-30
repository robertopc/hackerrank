# Lists
# https://www.hackerrank.com/challenges/python-lists

"""
Input:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

Output:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]

"""

if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        row = input().split(' ')
        if row[0] == 'insert':
            ls.insert(int(row[1]), int(row[2]))
        elif row[0] == 'print':
            print(ls)
        elif row[0] == 'remove':
            ls.remove(int(row[1]))
        elif row[0] == 'append':
            ls.append(int(row[1]))
        elif row[0] == 'sort':
            ls.sort()
        elif row[0] == 'pop':
            ls.pop()
        elif row[0] == 'reverse':
            ls.reverse()
