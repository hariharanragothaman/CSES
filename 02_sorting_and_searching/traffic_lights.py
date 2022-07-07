#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : traffic_lights.py
# Author            : cppygod
# Date              : 06.07.2022
# Last Modified Date: 07.07.2022
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
def input_as_array():
    return list(map(int, input().split()))
 
 
def debug():
    if os.path.exists("data.in"):
        print("*" * 10)
 
 
def debug3():
    if os.path.exists("data.in"):
        print("-" * 10)
 
 
def debug2(value):
    if os.path.exists("data.in"):
        print(value)
 
 
start_time = time.time()
 
 
def solve(x, n, P):
    stack = [0, x]
    ctr = defaultdict(int)
    ctr[0] = 1
    ctr[x] = 1
 
    for i in range(n):
        idx = bisect(stack, P[i])
        left_dist = P[i] - stack[idx - 1]
        right_dist = stack[idx] - P[i]
        ctr[left_dist] += 1
        ctr[right_dist] += 1
 
        total = left_dist + right_dist
        if ctr[total] >= 1:
            ctr[total] -= 1
        if ctr[total] <= 0:
            del ctr[total]
 
        print(max(ctr.keys()), end=" ")
        stack.insert(idx, P[i])
 
def main():
    x, n = input_as_array()
    P = input_as_array()
    solve(x, n, P)
 
 
if __name__ == "__main__":
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")
 
    testcases = 1
    for i in range(testcases):
        main()
 
    # If it's local - Print this O/P
    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
