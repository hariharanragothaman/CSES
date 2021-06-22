"""
n applicants and m free apartments
Distribute m such that, as many applicants get it.

Each applicant has a desired size - so they will accept any apartment whose size is close enough to the desired size
if the desired size is x, applicant will accept [x-k, x+k] range
print the number of applicants who will get an apartment

Example:
    4, 3, 5
    k = 5
    There are 3 free apartments
    60, 45, 80, 60 - desire

    45, 60, 60, 80 - sorting the desires
    30, 60, 75 - apt size - sort it too

"""

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