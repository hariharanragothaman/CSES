"""
Gray code is a list of 2**n bit strings of length n, where any 2 successive strings differ exactly by 1 bit.
That is - their hamming distance is 1

Task is to create gray code of given length n

5

...> This is generating all the subsets
000
001
010
011
100
101

...> We need to print it like this
000
001
010
011
101
100


# Solution thoughts:
result          X                  Y
0 0 0         0 0 1           0 0 1 (1)
0 0 1         0 1 0           0 1 0 (2)
0 1 1         0 0 1           0 1 1 (3)
0 1 0         1 0 0           1 0 0 (4)
1 1 0         0 0 1           1 0 1 (5)
1 1 1         0 1 0           1 1 0 (6)
1 0 1         0 0 1           1 1 1 (7)
1 0 0


So the keypoint is to generate X sequence. Here is the trick, actually X is lowest one-bit of Y (natural number set).
According to bit-manipulation, we can get lowest one-bit of number by
X = Y & -Y


Awesome! Why does X = Y & -Y give us the lowest bit? Here is an explanation:

~Y inverts all bits. Also
~Y = -Y - 1 (widely used - hello Python's negative list indexes).
-Y = ~Y + 1 This will give us an idea of what -Y looks like in bin

0000000000000101 = Y
1111111111111010 = ~Y
1111111111111011 = ~Y + 1 = -Y

0000000000000001 = Y & -Y
"""


def generate_gray_code(n):
    res = [0]
    for i in range(1, 2 ** n):
        res.append(res[-1] ^ (i & -i))
    return res


if __name__ == "__main__":
    n = int(input())
    result = generate_gray_code(n)
    # print(result)
    _f = "0" + str(n) + "b"
    for c in result:
        c = format(c, _f)
        print(c)
