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

    power_mod = [1]
    for i in range(1, n):
        power_mod.append((power_mod[-1] * p) % m)

    # Basically doing hash-values in prefix sum
    hash_values = [0] * (n + 1)
    for i in range(n):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]) % m
    return hash_values

hash_values = compute_hash_faster(s)

def rabin_karp(t):
    pattern_length = len(t)
    pattern_hash = compute_hash_faster(t)
    i = 0
    while i + pattern_length - 1 < n:
        field_hash = (hash_values[i + pattern_length] - hash_values[i] + m) % m
        if field_hash == pattern_hash[-1] * power_mod[i] % m:
            return 'YES'
        i += 1
    return 'NO'


def solve():
    T = int(input())
    while T > 0:
        t = input()
        res = rabin_karp(t)
        print(res)
        T -= 1

solve()