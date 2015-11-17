"""
https://www.hackerrank.com/challenges/angry-professor
Problem Statement

The professor is conducting a course on Discrete Mathematics to a class of N
students. He is angry at the lack of their discipline, and he decides to cancel
class if there are fewer than K students present after the class starts.

Given the arrival time of each student, your task is to find out if the class
gets cancelled or not.

Input Format

The first line of input contains T, the number of test cases. Each test case
contains two lines.
The first line of each test case contains two space-separated integers, N and K.
The next line contains N space-separated integers, a1,a2,…,aN, representing the
arrival time of each student.

If the arrival time of a given student is a non-positive integer (ai≤0), then
the student enters before the class starts. If the arrival time of a given
student is a positive integer (ai>0), the student enters after the class has
started.

Output Format

For each test case, print "YES" (without quotes) if the class gets cancelled.
Otherwise, print "NO" (without quotes).

Constraints

1≤T≤10
1≤N≤1000
1≤K≤N
−100≤ai≤100,where i∈[1,N]
Note
If a student enters the class exactly when it starts (ai=0), the student is
considered to have entered before the class has started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output

YES
NO

Explanation

For the first test case, K=3. The professor wants at least 3 students to be in
class, but there are only 2 who have arrived on time (−3 and −1). Hence, the
class gets cancelled.

For the second test case, K=2. The professor wants at least 2 students to be in
class, and there are 2 who have arrived on time (0 and −1). Hence, the class
does not get cancelled.

Copyright © 2015 HackerRank.
All Rights Reserved
"""
T = int(input())


def cancel_class(class_size, cutoff, arrival_times):
    """Determines if a class is canceled or not

    Returns 'YES' if a class is canceled, otherwise 'NO'.

    Args:
        class_size: Integer representing number of enrolled students.
        cutoff: Integer representing number of students class needs to not
            be canceled.
        arrival_times: A list of integers representing when a student arrived.
            Negative numbers and 0 represent an early student.
    """
    lates = sum(1 for num in arrival_times if num > 0)
    present = class_size - lates
    if present < cutoff:
        return "YES"
    return "NO"


def parse_input():
    """Parse the test cases"""
    for _ in range(T):
        line1 = [int(x) for x in input().split()]
        line2 = [int(x) for x in input().split()]
        N, K = line1[0], line1[1]
        cancel = cancel_class(N, K, line2)
        print(cancel)

if __name__ == '__main__':
    parse_input()
