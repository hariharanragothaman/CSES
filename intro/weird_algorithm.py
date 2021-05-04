n = int(input())
while n > 1:
    print(n, end=" ")
    tmp = n & 1
    if tmp:
        n = (n * 3) + 1
    else:
        n //= 2
print(1)
