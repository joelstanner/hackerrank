"""Hackerrank pangrams

A pangram is a sentence that contains all of the letters in the alphabet.
This checks to see if a sentence is a pangram.
"""

S = set(input().lower().replace(" ", ""))
a2z = set("abcdefghijklmnopqrstuvwxyz")

# Use python set comparison to determine the pangramness
if S >= a2z:
    print("pangram")
else:
    print("not pangram")
