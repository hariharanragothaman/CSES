import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))

start_time = time.time()


def solve(arr, n, x):
    hashmap = []
    # Store the location in hashmap
    for i, c in enumerate(arr):
        hashmap.append((c, i))
    hashmap.sort()

    for i in range(n):
        left = 0
        right = n - 1
        while left != right:
            target = x - hashmap[i][0]
            if left != i and right != i and hashmap[left][0] + hashmap[right][0] == target:
                print(hashmap[i][1]+1, hashmap[left][1]+1, hashmap[right][1]+1, sep=" ")
                return
            if hashmap[left][0] + hashmap[right][0] < target:
                left += 1
            else:
                right -= 1
    print("IMPOSSIBLE")


def main():
    n, x = map(int, input().split())
    arr = input_as_array()
    solve(arr, n, x)


if __name__ == "__main__":
    LOCAL = False

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("../io/data.in", "r")
        sys.stdout = open("../io/data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()