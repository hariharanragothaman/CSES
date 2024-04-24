import os
import sys
import time


def solve():
    n = int(input())
    A = input_as_array()
    n = len(A)

    ans = 0

    for i in range(1, n):
        if A[i] < A[i-1]:
            tmp = abs(A[i] - A[i-1])
            A[i] += tmp
            ans += tmp

    print(ans)


def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    solve()
    debug('-')

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()


# region debug

def input_as_array() -> list[int]:
    return list(map(int, input().split()))


def debug(char) -> None:
    if os.path.exists("data.in"):
        print(char * 25)


def debug2(value) -> None:
    if os.path.exists("data.in"):
        print(value)


# endregion


if __name__ == "__main__":
    main()
