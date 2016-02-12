"""
https://www.hackerrank.com/contests/worldcodesprint/challenges/bear-and-cryptography
Limak is a little bear who likes school. Today was his first lesson in
cryptography, and the teacher assigned some difficult homework—to find any
number with exactly K divisors. Limak wants to go the extra mile and find the
biggest possible number; however, his teacher explained that there are
arbitrarily large numbers with this property.

To give this little bear a more achievable challenge, the teacher advised him
to consider only numbers not greater than N. What is the biggest number Limak
can find?

Input Format

The first line contains an integer T denoting number of test cases.
The T subsequent lines of test cases each contain two space-separated integers,
N and K.

Constraints
1≤T≤50
1≤N≤1012
1≤K≤40
Output Format

For each test case, print the biggest number Limak finds on its own line.
Print −1 if no such number meets the given conditions.

Sample Input

3
15 3
15 4
15 5

Sample Output

9
15
-1
"""

from functools import reduce
from operator import mul
from pyprind import ProgBar


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


def count_factors(factors_list):
    factor_counts = []
    factor_set = list(set(factors_list))
    for f in factor_set:
        factor_counts.append(factors_list.count(f))
    factor_counts = [x + 1 for x in factor_counts]

    try:
        return reduce(mul, factor_counts)
    except TypeError:
        return 0


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def make_factors_list(num=10 ** 6):
    """Create a list of the total number of factors a number has

    Input is the number to count to (over 1,000,000 can get slow).
    Useful for inspecting trends.
    Returns a list where the index number is equivilent to the actual number
    """
    factors_list = []
    bar = ProgBar(num)
    for i in range(num):
        factors_list.append(count_factors(prime_factors(i)))
        bar.update()
    return factors_list


def make_index_list(factors_list, start=2, end=40):
    """Construct a list of index positions.

    Index position represents first seen factorial count for a given number.
    For example, i[23] == 4194304 (2**22). The first time we see a number with
    23 factorials is 23.
    """
    factors_count = []
    for i in range(start, end):
        temp_list = [x for x in factors_list if factors_list[x] == i]
        factors_count[i] = len(temp_list)
    return factors_count
