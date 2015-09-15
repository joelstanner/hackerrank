"""
https://www.hackerrank.com/challenges/poisonous-plants
Problem Statement

There are N plants in a garden. Each of these plants has been added with some
amount of pesticide. After each day, if any plant has more pesticide than the
plant at its left, being weaker than the left one, it dies. You are given the
initial values of the pesticide in each plant. Print the number of days after
which no plant dies, i.e. the time after which there are no plants with more
pesticide content than the plant to their left.

Input Format

The input consists of an integer N. The next line consists of N integers
describing the array P where P[i] denotes the amount of pesticide in plant i.

Constraints:
    1 ≤ N ≤ 100000
    0 ≤ P[i] ≤ 10^9

Output Format:

Output a single value equal to the number of days after which no plants die.

Sample Input

7
6 5 8 4 7 10 9

5
1 1 1 1 1

5
1 2 3 4 5

Sample Output

2
0
1

Explanation

Initially all plants are alive.
Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}
Plants[k] = (i,j) => jth plant has pesticide amount = i.
After the 1st day, 4 plants remain as plants 3, 5, and 6 die.
Plants = {(6,1), (5,2), (4,4), (9,7)}
After the 2nd day, 3 plants survive as plant 7 dies.
    Plants = {(6,1), (5,2), (4,4)}
After the 3rd day, 3 plants survive and no more plants die.
Plants = {(6,1), (5,2), (4,4)}
After the 2nd day the plants stop dying.
"""
N = input()
PLANTS = [int(x) for x in input().split()]


def check_pesticide_lvl(plants):
    """Input a list of INTs, return 1 if plant deaths, 0 if not.

    Also, remove dead plants from the list of plants.
    """
    died = 0
    kill_list = []

    for i in range(1, len(plants)):
        if plants[i] > plants[i - 1]:
            kill_list.append(i)
            died = 1

    if died:
        for death in kill_list:
            plants[death] = -1
        new_plants = [y for y in plants if y != -1]
        return died, new_plants
    else:
        return 0, plants


def count_days(plants):
    """Return the number of days that plants die"""
    days = 0

    while True:
        plant_died, plants = check_pesticide_lvl(plants)
        if plant_died != 0:
            days += 1
        else:
            break
    return days

print(count_days(PLANTS))
