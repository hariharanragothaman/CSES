#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : towers.py
# Author            : cppygod
# Date              : 01.07.2022
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
    debug2([A, n])
    cnt = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            stack = []
            visited.add(i)
            stack.append(A[i])
            for i in range(i+1, n):
                if i not in visited:
                    if A[i] < stack[-1]:
                        stack.append(A[i])
                        visited.add(i)
            cnt += 1
    print(cnt)

def solve2(A, n):
    stack= []

    for i in range(n):
        low, high = 0, len(stack)
        while low < high:
            middle = (low + high) >> 1
            if stack[middle] > A[i]:
                high = middle 
            else:
                low = middle + 1

        if low == len(stack):
            stack.append(A[i])
        else:
            stack[low] = A[i]
    
    print(len(stack))

def solve3(A, n):
    stack = []
    for i in range(n):
        pos = bisect(stack, A[i])
        if pos == len(stack):
            stack.append(A[i])
        stack[pos] = A[i]
    print(len(stack))


def main():
    n = int(input())
    A = input_as_array()
    solve3(A, n)
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
