s = input()
n = len(s)

count = 1
prev = s[0]
temp = []

i = 0
while i < n - 1:
    if s[i] == s[i + 1]:
        count += 1
    else:
        temp.append(count)
        count = 1
    i += 1
temp.append(count)
print(max(temp))
