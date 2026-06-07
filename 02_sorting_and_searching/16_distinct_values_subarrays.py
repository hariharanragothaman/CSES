#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : subarray_distinct_values.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 24.02.2022
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


def main():
    n, k = input_as_array()
    A = input_as_array()

    left, right = 0, 0
    ctr = Counter()
    mx, cnt = 0, 0
    
    while right < n:
        ctr[A[right]] += 1

        while len(ctr) > k:
            ctr[A[left]] -= 1
            if ctr[A[left]] == 0:
                del ctr[A[left]]
            left += 1

        cnt += right - left + 1
        right += 1

    print(cnt)




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
