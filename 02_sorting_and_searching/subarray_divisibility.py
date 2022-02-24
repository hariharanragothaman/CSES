#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : subarray_divisibility.py
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
    n = int(input())
    A = input_as_array()

    hmap = defaultdict(int)


    PS = [0] * n
    PS[0] = A[0]
    for i in range(1, n):
        PS[i] = PS[i-1] + A[i]
    
    hmap[0] = 1
    cnt = 0

    """
    (Sj - Si ) % n = 0
    https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/413234/DETAILED-WHITEBOARD!-BEATS-100-(Do-you-really-want-to-understand-It)
    if ri and rj are equal 
    What's ri and rj?

    ri = Si % n
    rj = Sj % n

    if ri == rj 
    
    We know that: (a+b) % k  = ((a%k) + (b%k)) % k

    So - (Sj - Si) % n  = ( (Sj %n) - (Si %n) ) % n
                        if ri = rj --> this will become zero

    So we need to count how many times the same remainder is coming...
    """
    for c in PS:
        val = c % n 
        
        # To account for negative numbers add n 
        if val < 0:
            val += n

        # The number I need to increment the counter with is:
        # The frequency of the remainder in it's previous step

        # This is "smartly" seeing if I have seen the remainder previously.
        if val in hmap:
            cnt += hmap[val]
        hmap[val] += 1

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
