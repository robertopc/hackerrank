# Python If-Else

https://www.hackerrank.com/challenges/py-if-else/problem

# Submit

```python
def isodd(n):
    return True if n % 2 == 1 else False

if __name__ == '__main__':
    n = int(input())
    if isodd(n) :
        print('Weird')
    elif not isodd(n) and n in range(2,5):
        print('Not Weird')
    elif not isodd(n) and n in range(6,20):
        print('Weird')
    elif not isodd(n) and n > 20:
        print('Not Weird')
    else:
        print('Weird')
```
