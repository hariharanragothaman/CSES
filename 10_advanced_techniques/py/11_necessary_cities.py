"""
File    : 11_necessary_cities.py
Problem : Necessary Cities
Section : Advanced Techniques
Status  : UNSOLVED (placeholder)
"""

import os
import sys
import time


def solve():
    # TODO: not solved
    pass


def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    solve()
    debug("-")

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
