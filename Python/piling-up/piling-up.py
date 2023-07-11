"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example:
blocks = [1, 2, 3, 8, 7]

Result: No

After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.

blocks = [1, 2, 3, 7, 8]

Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format:

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints:

1 <= T <= 5
1 <= n <= 10**5
1 <= sideLength <= 2**31



Output Format:

For each test case, output a single line containing either Yes or No.
"""

def check_stack_possibility(blocks):
    n = len(blocks)
    left = 0
    right = n - 1
    prev_cube = 0

    while left <= right:
        if blocks[left] >= blocks[right]:
            if blocks[left] >= prev_cube:
                prev_cube = blocks[left]
                left += 1
            else:
                return "No"
        else:
            if blocks[right] >= prev_cube:
                prev_cube = blocks[right]
                right -= 1
            else:
                return "No"

    return "Yes"


# Get the number of test cases
T = int(input())

for _ in range(T):
    # Get the number of cubes and their side lengths
    n = int(input())
    blocks = list(map(int, input().split()))

    # Check if it is possible to stack the cubes
    result = check_stack_possibility(blocks)
    print(result)
