import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


start_time = time.time()


def solve(g, n):
    """
    The actual solution begins here
    c = a + b
    print(c)
    """
    ans = [0] * (n + 1)
    ans[1] = n - 1
    # print("The graph is:", g)

    # Starting post-order traversal
    res_tmp = []
    post_order = []

    stack = [1]
    while stack:
        node = stack.pop()
        res_tmp.append(node)
        if g[node]:
            for nei in g[node]:
                stack.append(nei)
    while res_tmp:
        post_order.append(res_tmp.pop())

    children_count = defaultdict(int)

    for k in post_order:
        if k not in g:
            children_count[k] = 0
        elif k in g:
            cnt = 0
            cnt += len(g[k])
            for child in g[k]:
                cnt += children_count[child]
            children_count[k] = cnt

    for i in range(1, n + 1):
        print(children_count[i], end=" ")


def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    n = int(input())
    arr = input_as_array()
    g = defaultdict(list)

    # Trees are assumed to be directed and rooted here.
    for i, c in enumerate(arr, 2):
        g[c].append(i)
    solve(g, n)


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
