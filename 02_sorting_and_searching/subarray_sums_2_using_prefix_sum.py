"""
To count the number of subarrays having a definite sum

Constraints:
The numbers are all +ve - 1 to 2*10^5

"""

"""
Solution thoughts:
We can have a map that keeps track of the prefix sums. At each index $i$, we can
count the number of prefixes with sum equal to $\texttt{prefixSum}[i] - x$. This
will ensure that we can remove a prefix from our current prefix to build a
subarray with sum $x$. After every iteration, we just add our new prefix sum to
the map.


"""

from collections import Counter

def count_subarrays_with_target_sum(arr, n, target):
    result_count = 0
    prefix_sum = 0
    hmap = Counter()
    hmap[0] = 1

    for c in arr:
        prefix_sum += c
        result_count += hmap[prefix_sum - target]
        hmap[prefix_sum] += 1
    print(result_count)


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    count_subarrays_with_target_sum(arr, n, target)
