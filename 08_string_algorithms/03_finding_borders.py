# To find the border of a string - that is a prefix and also a suffix

p = 53
m = 10 ** 9 + 9

s = input()
n = len(s)

# Pre-computing powers
power_mod = [1]
for i in range(1, n):
    power_mod.append((power_mod[-1] * p) % m)


def compute_hash_faster(s):
    n = len(s)
    p = 53
    m = 10 ** 9 + 9

    # Pre-computing the powers of 31
    power_mod = [1]
    for i in range(1, n):
        power_mod.append((power_mod[-1] * p) % m)

    # Basically doing hash-values in prefix sum
    hash_values = [0] * (n + 1)
    for i in range(n):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]) % m
    return hash_values


def finding_borders(s, n):
    hvalues = compute_hash_faster(s)
    result = []

    for border in range(1, n):
        i = 0
        field_hash = (hvalues[i + border] + m - hvalues[i]) % m
        field_hash = (field_hash * power_mod[n-i-1]) % m
        # print(f"The string is: {s[i:i+border]} and field hash is: {field_hash}")

        i = n-border
        field_hash2 = (hvalues[i + border] + m - hvalues[i]) % m
        field_hash2 = (field_hash2 * power_mod[n-i-1]) % m
        # print(f"The string is: {s[n-border:]} and field hash is: {field_hash2}")

        if field_hash2 == field_hash:
            result.append(border)
    print(*result)


    """
    # Bruteforce Style - that involves slicing everytime
    res = []
    for border in range(1, n):
        leftBorder = s[:border]
        rightBorder = s[n-border:]
        if leftBorder == rightBorder:
            res.append(len(leftBorder))
    print(*res)
    """

finding_borders(s, n)