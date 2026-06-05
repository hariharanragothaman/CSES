import sys

I = lambda: map(int, sys.stdin.readline().split())
n, m = I()

link = [i for i in range(n + 1)]
size = [1] * (n + 1)


def find(x):
    while link[x] != x:
        x = link[x]
    return x


maxsize = 0
comps = n
for _ in " " * m:
    a, b = I()
    rep_a, rep_b = find(a), find(b)
    if rep_a != rep_b:
        comps -= 1
        if size[rep_a] > size[rep_b]:
            rep_a, rep_b = rep_b, rep_a

        link[rep_a] = link[rep_b]
        t = size[rep_b] = size[rep_b] + size[rep_a]

        if t > maxsize:
            maxsize = t
    print(comps, maxsize)
