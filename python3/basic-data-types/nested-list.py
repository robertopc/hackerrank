# Nested List
# https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        students.append([name, score])
    grades2 = []
    for grade in grades:
        if grade != min(grades):
            grades2.append(grade)
    seconds = []
    for student in students:
        if student[1] == min(grades2):
            seconds.append(student[0])
    print('\n'.join(sorted(seconds)))
