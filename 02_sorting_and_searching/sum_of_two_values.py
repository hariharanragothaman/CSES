
def find_two_sum(arr, n, s):
    hashmap = {}
    # Storing all value, and indexes in the hashmap
    for i, c in enumerate(arr):
        hashmap[c] = i

    for i, c in enumerate(arr):
        diff = s - c
        if diff in hashmap and hashmap[diff] != i:
            return i+1, hashmap[diff]+1
    return -1, -1


n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))
a, b = find_two_sum(arr, n, s)
if a == -1 or b == 1:
    print('IMPOSSIBLE')
else:
    print(a, b)