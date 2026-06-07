"""
File    : 01_word_combinations.py
Problem : Word Combinations
Section : String Algorithms
Status  : SOLVED
Approach: DP on prefix length + trie for word lookup
Alt     : 01_word_combinations_alt_backtracking.py
Note    : Contest-optimized inline trie. See trie.py for reusable class version.
"""

MOD = 10**9 + 7

def solve() -> None:
    s = input().strip()
    k = int(input())
    trie = [{}]
    end = [False]

    for _ in range(k):
        word = input().strip()
        node = 0

        for ch in word:
            if ch not in trie[node]:
                trie[node][ch] = len(trie)
                trie.append({})
                end.append(False)

            node = trie[node][ch]

        end[node] = True

    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        node = 0

        for j in range(i, n):
            ch = s[j]

            if ch not in trie[node]:
                break

            node = trie[node][ch]

            if end[node]:
                dp[i] = (dp[i] + dp[j + 1]) % MOD

    print(dp[0])

def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    solve()

    if os.path.exists("data.in"):
        sys.stdout.write(f"\nTime Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()

if __name__ == "__main__":
    main()
