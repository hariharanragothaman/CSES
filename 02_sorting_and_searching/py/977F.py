#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 977F.py
# Author            : cppygod
# Date              : 01.07.2022
# Last Modified Date: 01.07.2022
# Last Modified By  : cppygod

"""
செயல் பேசும் ஆழம் இங்கே சொற்கள் பேசுமா?

Focus, Determination and Sheer-Will

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect, bisect_left, bisect_right
from functools import reduce

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

def debug():
    if os.path.exists("data.in"):
        print("*" * 10)

def debug3():
    if os.path.exists("data.in"):
        print("-" * 10)

def debug2(value):
    if os.path.exists('data.in'):
        print(value)

start_time = time.time()


def solve(A, n):
    count = Counter()
    for x in reversed(A):
        count[x] = 1 + count[x+1]
    
    m = max(count.values())
    for k, v in count.items():
        if v == m:
            break 

    todo = k
    ans = []
    for i, x in enumerate(A,1):
        if x==todo:
            todo += 1
            ans.append(i)
 
    print(len(ans))
    print(" ".join(map(str, ans)))

def main():
    n = int(input())
    A = input_as_array()
    solve(A, n)
    debug()


if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
