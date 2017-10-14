# Day 8: Dictionaries and Maps
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

entries = int(input())
phoneBook = {}

for n in range(0, entries):
	entrie = input().split()
	phoneBook[entrie[0]] = entrie[1]
while True:
	entrie = input()
	if not entrie:
		break
	elif entrie in phoneBook:
		print('{}={}'.format(entrie, phoneBook[entrie]))
	else:
		print('Not found')


