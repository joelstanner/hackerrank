"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta

Input Format

The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

(chatGPT)
"""

# Get the number of students
N = int(input())

# Create a nested list to store the names and grades
students = []

# Populate the nested list
for _ in range(N):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Find the second lowest grade
grades = set([student[1] for student in students])
second_lowest_grade = sorted(grades)[1]

# Get the names of students with the second lowest grade
names = [student[0] for student in students if student[1] == second_lowest_grade]
names.sort()  # Sort the names alphabetically

# Print the names of students with the second lowest grade
for name in names:
    print(name)
