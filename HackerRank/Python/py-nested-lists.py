# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  09/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/nested-list/problem
# Description:  Solution to "Python Nested Lists"
# Licence:      CC BY 4.0
# =====================================================================

def penultimate_grade(sg):
    grades = sorted(list(set([grade[1] for grade in sg])), reverse=True)
    return grades[-2]

def students_by_grade(sg, g):
    return sorted([stud[0] for stud in sg if stud[1] == g])


if __name__ == '__main__':
    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])

    penult = penultimate_grade(student_grades)
    students = students_by_grade(student_grades, penult)

    for s in students:
        print(s)