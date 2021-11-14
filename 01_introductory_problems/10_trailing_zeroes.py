"""
Calculate the number of trailing zeroes in a factorial
"""


"""
Solution approaches:
> Consider prime factors of n! 
- 2's and 5's contribute to zeroes. if we count the number of 2's and 5's we can count zeroes.

- If we can count the number of 5's we should be done - since number of 2's will always be more ni factorial

"""


n = int(input())
count = 0

while n >= 5:
    n //= 5
    count += n
print(count)
