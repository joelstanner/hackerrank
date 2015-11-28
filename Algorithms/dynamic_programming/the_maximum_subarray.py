"""https://www.hackerrank.com/challenges/maxsubarray
Problem Statement

Given an array A={a1,a2,…,aN} of N elements, find the maximum possible sum of a
1. Contiguous subarray
2. Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer T. T cases follow.
Each test case begins with an integer N. In the next line, N integers follow
representing the elements of array A.

Constraints:

1≤T≤10
1≤N≤10^5
−10^4≤ai≤10^4
The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and
non-contiguous subarray. At least one integer should be selected and put into
the subarrays (this may be required in cases where all elements are negative).

Sample Input

2
4
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output

10 10
10 11

Explanation

In the first case:
The max sum for both contiguous and non-contiguous elements is the sum of ALL
the elements (as they are all positive).

In the second case:
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
For the max sum of a not-necessarily-contiguous group of elements, simply add
all the positive elements.
"""
def add_positives(array):
    if max(array) < 0:
        return max(array)
    return sum(num for num in array if num > 0)


def max_subarray(array):
    max_end_here = max_so_far = array[0]
    for num in array[1:]:
        max_end_here = max(num, max_end_here + num)
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far


def main():
    for _ in range(T):
        arr_size = input()
        arr = [int(x) for x in input().split()]
        ap = add_positives(arr)
        ms = max_subarray(arr)
        print(ms, ap)

if __name__ == '__main__':
    T = int(input())
    main()
