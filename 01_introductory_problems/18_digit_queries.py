"""
Given an infinite string

123456789101112131415161718192021....

Solution thoughts:
length 1 digit:  1 to 9 -> 9 numbers => 9 digits total
length 2 digits: 10 to 99 -> 90 numbers => 180 digits total
length 3 digits: 100 to 999 -> 900 numbers => 2700 digits total
length 4 digits: 1000 to 9999 -> 9000 numbers => 36000 digits total
etc
The number of digits per group (9, 180, 2700, 36000, etc) are easy to compute.
Skip these groups of equal-length numbers until you reach the right group (the remaining k falls into it).
Then just compute the right number inside the group and get the right digit from it.
"""

for _ in range(int(input())):
    k = int(input())

    length = 1
    while k > 9 * 10**(length-1) * length:
        k -= 9 * 10**(length-1) * length
        length += 1
    q, r = divmod(k-1, length)
    print(str(10**(length-1) + q) [r])