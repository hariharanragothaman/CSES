import os
import sys
import time


def solve():
    S = input()
    cnt = 1
    n = len(S)
    max_cnt = 1

    for i in range(1, n):
        if S[i] == S[i - 1]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1

    print(max_cnt)


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
