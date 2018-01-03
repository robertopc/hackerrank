# Lists (Alternative solution)
# https://www.hackerrank.com/challenges/python-lists
# Alternative solution with human interaction

"""
Sample Input:
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

Sample Output:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]

"""

def get_input():
    while True:
        try:
            number = int(input('\tInput a integer: '))
            break
        except ValueError:
            print('Error: Please input a integer.\n')
            continue
    return number


if __name__ == '__main__':
    N = int(input('How many operations will happens? '))
    ls = []
    operations = (
        'insert', 'print', 'remove', 'append',
        'sort', 'pop', 'reverse'
    )
    operations_list = '''
    Operations:

    1. insert
    2. print
    3. remove
    4. append
    5. sort
    6. pop
    7. reverse
    '''
    for i in range(N):
        print('\nOperation {}/{}'.format(i + 1, N))
        while True:
            try:
                print(operations_list)
                operation_index = int(input('Input the number of the operation: '))
                if operation_index not in range(1, 7 + 1):
                    raise ValueError()
                break
            except ValueError:
                print('Error: Input a number between 1 and 7.')
        operation = operations[operation_index - 1]
        if operation == 'insert':
            index = int(input('\tWhat index? '))
            value = get_input()
            ls.insert(index, value)
        elif operation == 'print':
            print(ls)
        elif operation == 'remove':
            value = get_input()
            if value in ls:
                ls.remove(value)
        elif operation == 'append':
            value = get_input()
            ls.append(value)
        elif operation == 'sort':
            ls.sort()
        elif operation == 'pop' and len(ls) > 0:
            ls.pop()
        elif operation == 'reverse':
            ls.reverse()
