n = int(input())

if n == 1:
    print(1)
elif n == 4:
    res = [2, 4, 1, 3]
    print(*(res))
elif n < 5:
    print("NO SOLUTION")
elif n >= 5:
    # Print all odd numbers in decreasing order, then all even numbers in decreasing order
    even, odd = [], []
    for i in range(n, 0, -1):
        if i & 1:
            odd.append(i)
        else:
            even.append(i)
    print(*(odd + even))
