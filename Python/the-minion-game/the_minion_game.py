"""
https://www.hackerrank.com/challenges/the-minion-game
Problem Statement:

Kevin and Stuart want to play the 'The Minion Game'.
Bob is the match referee. Bob's task is to declare the winner and ensure that
no rules are broken.
Stuart is Player 1 and Kevin is Player 2.

About Game

Rules
The game is a two player game. Players are given a string S.
Both the players have to make words using the letters of string S.
Player 1 has to make words starting with consonants.
Player 2 has to make words starting with vowels.
Game ends when both players have made all possible substrings.

Scoring:
A player gets +1 Point for each occurence of the word in the string S.
Example:
If string S = BANANA
Word made by Player 2 = ANA
'ANA' is occuring twice in 'BANANA'. Hence, Player 2 will get 2 Points.

Your task is to help Bob.

Input Format:

Single line containing string S.
Note: String S contains only capital alphabets [A-Z].

Constraints

0 < len(S) ≤ 10^6

Output Format

Print the name of the winner along with the total score.

If the game is draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
Note :
I would like to suggest mentioning that the vowels here are defined as AEIOU
(since Y is sometimes considered a vowel, but not in this problem).

Copyright © 2015 HackerRank.
All Rights Reserved
"""
S = input()
player1 = player2 = 0
str_len = len(S)

# Triangular number is total possible points e.g. 4+3+2+1 = 10
# See wikipedia for Triangular number formula
triangular_number = (str_len * (str_len + 1) // 2)

# Each index position is subtracted from total string length if it's a vowel,
# then summed for total score
player2 = sum([(str_len - pos) for pos, char in enumerate(S)
               if char in 'AEOIU'])
player1 = triangular_number - player2

if player1 > player2:
    print("Stuart {}".format(player1))
elif player2 > player1:
    print("Kevin {}".format(player2))
else:
    print("Draw")
