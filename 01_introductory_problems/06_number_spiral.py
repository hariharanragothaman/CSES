import os
import sys
import time


def get_value(y, x):
    maxi = max(x, y)
    square = (maxi - 1) * (maxi - 1)
    if maxi % 2 == 0:
        if x > y:
            print(square + y)
        else:
            print((maxi * maxi) - x + 1)
    else:
        if x > y:
            print((maxi * maxi) - y + 1)
        else:
            print(square + x)


def solve():
    testcases = int(input())
    for _ in range(testcases):
        y, x = input_as_array()
        get_value(y, x)


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
