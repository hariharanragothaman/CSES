def gen_permute_iter(arr):
    if len(arr) < 1:
        yield arr
    else:
        for perm in gen_permute_iter(arr[1:]):
            for i in range(len(arr)):
                yield perm[:i] + arr[0:1] + perm[i:]


def create_strings(s):
    """Basically we have to generate all permutations of the strings"""
    n = len(s)

    result = set()
    for c in gen_permute_iter(s):
        result.add(c)
    result = sorted(result)

    print(len(result))
    for r in result:
        print(r)


if __name__ == "__main__":
    s = input()
    create_strings(s)
