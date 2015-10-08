"""https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

You are given N mobile numbers. Sort them in ascending order after which print
them in standard format.

+91 xxxxx xxxxx

The given mobile numbers may have +91 or 91 or 0 written before the actual 10
digit number. Alternatively, there maynot be any prefix at all.


Input Format

An integer N followed by N mobile numbers.

Output Format

N mobile numbers printed in different lines in the required format.


Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230


Concept

Like most other programming languages, python has the concept of closures. Just
extending it gives us decorators, which is an invaluable asset. You can learn
about decorators in 12 easy steps from here.
To solve the above question, make a list of the mobile numbers and pass it to a
function which sorts the array in ascending order. Make a decorator which
standardizes mobile numbers and apply it to the function. Simple, Isn't it!
"""

NUMBER_OF_ITEMS = int(input())
NUMBERS = []

for _ in range(NUMBER_OF_ITEMS):
    NUMBERS.append(input())


class PhoneNum:
    """Decorator constructor that standardizes mobile numbers.

    The last 10 digits of the number are all we are worried about,
    so we will truncate any of the first characters (sometimes there
    may be a '+' sign for example) and keep only the last 10.
    Standardizes the output with a '+' sign and the passed in prefix.
    """

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapped_func(num_list):
            for i in range(len(num_list)):
                # truncate number, keeping only last 10 digits
                num_list[i] = num_list[i][-10:len(num_list[i]) + 1]
                # format the number to a standardized string "+91 xxxxx xxxxx"
                num_list[i] = (
                    "+" + self.prefix + " " + num_list[i][:5] + " "
                    + num_list[i][5:])
            func(num_list)
        return wrapped_func


def phone_num(prefix):
    def decorator(func):
        return PhoneNum(prefix)
    return decorator

@phone_num('91')
def sorter(num_list):
    """Sort a phone number list, standardize the formatting, and print it."""
    num_list.sort()
    for num in num_list:
        print(num)


sorter(NUMBERS)
