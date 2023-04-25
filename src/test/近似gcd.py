n, g = map(int, input().split())
ls = list(map(int, input().split()))

cnt = 0
i = 0
j = -1
ans = 0

def is_gcd(a, g) :

    if a % g == 0 : return True
    else : return False

while j < n :
    if cnt < 2 :
        i += 1
        ans += 1
        if is_gcd(ls[i], g) : pass
        else : cnt += 1
    j += 1
    if is_gcd(ls[j], g) : pass
    else : cnt -= 1

print(ans)
