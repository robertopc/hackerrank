# Find the Second Largest Number
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))  # set unique elements to list

    arr.discard(max(arr))  # discard max element
    print(max(arr))
