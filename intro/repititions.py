"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T.
Your task is to find the longest repetition in the sequence.
This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints

    1≤n≤106


Example

Input:
ATTCGGGA

Output:
3
"""


# maximum repeating substring that contains only one character

s = input()
n = len(s)

count = 1
prev = s[0]
temp = []

i = 0
while i < n - 1:
    if s[i] == s[i + 1]:
        count += 1
    else:
        temp.append(count)
        count = 1
    i += 1
temp.append(count)
print(max(temp))
