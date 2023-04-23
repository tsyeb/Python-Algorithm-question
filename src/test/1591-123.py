# 前缀和  二分法定位

def check(n):

    if one_ls[n] <= aim_L:
        return True
    else:
        return False


aim_L,aim_R = map(int, input().split())
one_ls = [1]
two_ls = [1]
i = 1
while i < 10000000:
    i += 1
    one_ls.append(one_ls[-1] + i)
    two_ls.append(two_ls[-1] + one_ls[-1])

# print(one_ls[:50])
# print(two_ls[:50])

left = 0
right = int(1e7)

while left < right:
    mid = (right - (right - left)) >> 1
    if check(mid):
        left = mid + 1
    else:
        right = mid
L = left - 1

l = 0
r = int(1e7)
while left <= right:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1
R = l
num = two_ls[R] - two_ls[L]

print(num)
