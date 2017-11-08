# Day 11: 2D Arrays
# https://www.hackerrank.com/challenges/30-2d-arrays/problem

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hourglass = []

for i in range(6):
	for j in range(6):	
		if i < 4 and j < 4:
			hourglass.append(sum([
				arr[i][j], 
				arr[i][j+1],
				arr[i][j+2],
				arr[i+1][j+1],
				arr[i+2][j],
				arr[i+2][j+1],
				arr[i+2][j+2]
			]))
print(max(hourglass))

"""
test 1 input
	1 1 1 0 0 0
	0 1 0 0 0 0
	1 1 1 0 0 0
	0 0 2 4 4 0
	0 0 0 2 0 0
	0 0 1 2 4 0
teste 1 output
	19
"""
