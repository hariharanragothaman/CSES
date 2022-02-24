#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : array_division.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 23.02.2022
# Last Modified By  : cppygod

import os
from io import BytesIO, IOBase
import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement


# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def check(pivot, arr, n, k):
    cnt = 0
    so_far = 0

    for i in range(n):
        if arr[i] > pivot:
            return False;

        if arr[i] + so_far > pivot:
            so_far = 0
            cnt += 1

        so_far += arr[i]

    if so_far:
        cnt += 1

    return cnt <= k


def solve(arr, n, k):
    low = 0
    high = 10000000000000000000
    
    while low <= high:
        pivot = (low + high) >> 1
        if check(pivot, arr, n, k):
            ans = pivot 
            high = pivot - 1
        else:
            low = pivot + 1

    print(ans)


def main():
    """
    Divide the array into "K" subarrays such that maximum sum of all subarrays is minimum 
    """
    n, k = input_as_array()
    arr = input_as_array()
    solve(arr, n, k)



if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
