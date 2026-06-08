n, m, k = map(int, input().split())
desired_apt_size = list(map(int, input().split()))
apt_size = list(map(int, input().split()))

desired_apt_size.sort()
apt_size.sort()
result_count = 0

i = j = 0
while i < len(desired_apt_size) and j < len(apt_size):
    if desired_apt_size[i] - k > apt_size[j]:
        j += 1
    elif desired_apt_size[i] + k < apt_size[j]:
        i += 1
    else:
        i += 1
        j += 1
        result_count += 1

print(result_count)