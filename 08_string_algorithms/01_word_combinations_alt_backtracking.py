"""
File    : 01_word_combinations.py
Problem : Word Combinations
Section : String Algorithms
Status  : UNSOLVED (placeholder)
"""

import os
import sys
import time

cnt = 0
MOD = 10**9 + 7

def backtrack(s, words, state, current):
    global cnt

    # Checking if it's valid
    if current == s:
        cnt += 1
        return 
    
    # Prune the state if it's not valid 
    if not s.startswith(current):
        return 

    # Get the candidates
    for w in words:
        if s.startswith(current + w):
            state.append(w)
            backtrack(s, words, state, current + w)
            state.remove(w)

def solve():
    s = input()
    k = int(input())
    words = [input() for _ in range(k)]
    backtrack(s, words, [], '')
    print(cnt % MOD)

def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    solve()

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()


if __name__ == "__main__":
    main()
