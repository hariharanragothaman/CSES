"""
Given a string and patterns, check for each pattern if it appears in string.

    1. String Hashing
    2. KMP

We have 5 * (10**5) queries and length of the string is - (10**5) length
The time complexity is O(m*n) where there are O(m+n) text comparisons
"""

from functools import reduce

def rabin_karp(s, t):
    if len(s) > len(t):
        return -1

    base = 26

    # Base hash codes computing for 's' and 't'
    t_hash = reduce(lambda h, c: h * base + ord(c), t[: len(s)], 0)
    s_hash = reduce(lambda h, c: h * base + ord(c), s, 0)

    power_s = base ** max(len(s) - 1, 0)  # base ^ |s-1|

    for i in range(len(s), len(t)):
        # Check for hashcode and actual string to avoid collision
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)

        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    return -1

if __name__ == '__main__':
    text = input()
    k = int(input())
    i = 0
    while i < k:
        pattern = input()
        result = rabin_karp(pattern, text)
        if result != -1:
            print('YES')
        else:
            print('NO')
        i += 1