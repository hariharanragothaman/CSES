#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : counting_bits.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 22.02.2022
# Last Modified By  : cppygod

from io import BytesIO, IOBase
import os, sys, math, cmath, time, collections
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
    two = 2
    ans = 0
    N = n
    while n != 0:
        ans += int(N / two) * (two >> 1)
        if((N & (two - 1)) > (two >> 1) - 1):
            ans += (N&(two - 1)) - (two >> 1) + 1
        two <<= 1;
        n >>= 1;
    print(ans)


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
