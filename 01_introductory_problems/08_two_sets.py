"""

Your task is to divide the numbers into 2 sets of equal sum
arr = [1, 2, 3, 4, 5, 6 ,7]

Some thoughts:
4
1 2 3 4
# I think we can take the greedy approach?
1 4
2 3

1 2 3 4 5 6 7
- 14

1 2 3 4 5 6 7 8  sum = 18 for each set

8 + 5 + 2 + 3
1 + 4 + 6 + 7

8 + 7 + 3 = 18
1 + 2 + 4 + 5 + 6 = 18

"""

n = int(input())
s = (n * (n + 1)) // 2
if s & 1:
    print("NO")
else:
    print("YES")
    s1 = s2 = set()
    target_set_sum = s // 2
    tmp = 0
    for i in range(n, -1, -1):
        if tmp + i == target_set_sum:
            s1.add(i)
            break
        elif tmp + i < target_set_sum:
            tmp += i
            s1.add(i)
        elif tmp + i > target_set_sum:
            continue
    print(len(s1))
    print(*s1)
    s2 = {c for c in range(1, n + 1) if c not in s1}
    print(len(s2))
    print(*s2)
