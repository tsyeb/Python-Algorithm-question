def jiechen(num):

    ans = 0
    while num:
        ans += num
        num -= 1
    return ans

def fanjiechen(num, d):

    ans = 0
    while d:
        ans += num
        num -= 1
        d -= 1
    return ans

def checkL(mid):

    if one_ls[mid] <= aim_L:
        return True
    else:
        return False


def checkR(mid):

    if one_ls[mid] <= aim_R:
        return True
    else:
        return False


aim_L, aim_R = map(int, input().split())
one_ls = [1]
two_ls = [1]
i = 1
while i < 1000000:
    i += 1
    one_ls.append(one_ls[-1] + i)
    two_ls.append(two_ls[-1] + one_ls[-1])
print(one_ls[:30])
print(two_ls[:30])

L_left = 0
L_right = int(1e5)
while L_left < L_right:
    mid = (L_left + L_right) // 2
    if checkL(mid):
        L_left = mid + 1
    else:
        L_right = mid
L = L_left - 1

R_left = 0
R_right = int(1e5)
while R_left < R_right:
    mid = (R_left + R_right + 1) // 2
    if checkR(mid):
        R_left = mid
    else:
        R_right = mid - 1
R = R_left

print(L)
print(R)
print(one_ls[L])
print(one_ls[R + 1])
print(two_ls[R] - two_ls[L])

print('-' * 10)

ansnum = two_ls[R + 1] - two_ls[L]
ansnum -= jiechen(aim_L - one_ls[L] - 1)
ansnum -= fanjiechen(R - 1, one_ls[R + 1] - aim_R)
print(ansnum)
