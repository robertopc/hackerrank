# Day 10: Binary Numbers
# https://www.hackerrank.com/challenges/30-binary-numbers/problem

def dec2bin(n):
	"Convert decimal to binary"
	mods = []
	while n > 0:
		mods.append(n % 2)
		n = n // 2
	mods.reverse()
	return int(''.join(map(str, mods)))
n = int(input().strip())
b = str(dec2bin(n))
c = 0
cmax = 0
for i in range(0, len(b)):
	if b[i] == '1':
		c = c + 1
		if c > cmax:
			cmax = c
	else:
		c = 0
print(cmax)
