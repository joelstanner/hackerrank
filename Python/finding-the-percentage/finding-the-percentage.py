"""
https://www.hackerrank.com/challenges/finding-the-percentage
Problem Statement:

There is a record of 'n' students, each record having name of student,
percent marks obtained in Maths, Physics and Chemistry. Marks can be floating
values. The user enters an integer 'n' followed by names and marks for the 'n'
students. You are required to save the record in a dictionary data type. The
user then enters name of a student and you are required to print the average
percentage marks obtained by that student, correct to two decimal places.

Input Format:

Integer N followed by name and marks for N students, followed by the name of
the particular student.

Output Format:

Average percentage of marks obtained

Constraints
2 <= N <= 10
0 <= Marks <= 100

Sample Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00

Copyright © 2015 HackerRank.
All Rights Reserved
"""
N = int(input())

student_marks = {}

for _ in range(N):
    line = input()
    name = line.split()[0]
    marks = [float(x) for x in line.split()[1:]]
    student_marks[name] = marks

student = input()
average = sum(student_marks[student]) / len(student_marks[student])

print("{0:.2f}".format(average))
