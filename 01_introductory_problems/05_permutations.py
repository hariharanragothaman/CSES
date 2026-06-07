import os
import sys
import time


def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    elif n == 2 or n == 3:
        print("NO SOLUTION")
        return
    elif n == 4:
        print("2 4 1 3")
        return
    else:
        tmp = n
        # Print all odd numbers first, followed by even numbers
        while n > 0:
            print(n, end=" ")
            n = n - 2
        tmp = tmp - 1
        while tmp > 0:
            print(tmp, end=" ")
            tmp = tmp - 2


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
