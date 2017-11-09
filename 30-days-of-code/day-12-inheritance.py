# Day 12: Inheritance
# https://www.hackerrank.com/challenges/30-inheritance/problem 

'''
input
	Heraldo Memelli 8135627
	2
	100 80
output
	Name: Memelli, Heraldo
	ID: 8135627
	Grade: O
'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	#   Class Constructor
	#   
	#   Parameters:
	#   firstName - A string denoting the Person's first name.
	#   lastName - A string denoting the Person's last name.
	#   id - An integer denoting the Person's ID number.
	#   scores - An array of integers denoting the Person's test scores.
	#
	# Write your constructor here
	def __init__(self, firstName, lastName, idNumber, scores):
		Person.__init__(self, firstName, lastName, idNumber)
		self.scores = scores

	#   Function Name: calculate
	#   Return: A character denoting the grade.
	#
	# Write your function here
	def calculate(self):
		average = sum(self.scores) / len(self.scores)

		if average < 40:
			return "T"
		elif average >= 40 and average < 55:
			return "D"
		elif average >= 55 and average < 70:
			return "P"
		elif average >= 70 and average < 80:
			return "A"
		elif average >= 80 and average < 90:
			return "E"
		elif average >= 90 and average <= 100:
			return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
