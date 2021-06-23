from typing import List
from itertools import chain, combinations
from bisect import bisect_left
from collections import defaultdict


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_subsets_sum(A: List) -> List:
    subset_sum = [0]
    for c in powerset(A):
        if c:
            subset_sum.append(sum(list(c)))
    return subset_sum


def binary_search(array, val):
    index = bisect_left(array, val)
    if index != len(array) and array[index] == val:
        return index
    else:
        return -1


def meet_in_the_middle(arr, n, target) -> int:
    pivot = n >> 1
    arr1 = arr[:pivot]
    arr2 = arr[pivot:]
    first_subset_sum = get_subsets_sum(arr1)
    second_subset_sum = get_subsets_sum(arr2)

    count = 0
    hmap = defaultdict(int)

    for c in first_subset_sum:
        hmap[c] += 1

    for c in second_subset_sum:
        count += hmap.get(target-c, 0)

    print(count)


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    meet_in_the_middle(arr, n, k)
