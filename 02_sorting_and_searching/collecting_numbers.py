import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


start_time = time.time()


def solve(arr, n):
    """
    The actual solution begins here
    c = a + b
    print(c)
    """
    cnt = 1
    position = [0] * (n + 1)
    for i, c in enumerate(arr):
        position[c] = i

    for i in range(1, n):
        if position[i + 1] < position[i]:
            cnt += 1
    print(cnt)


def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    n = int(input())
    arr = input_as_array()
    solve(arr, n)


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
