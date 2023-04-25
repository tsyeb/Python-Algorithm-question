n, g = map(int, input().split())
line = [0] + list(map(int, input().split()))

ans = 0
last = 0
j = 1
for i in range(1, n + 1) :
    if line[i] % g != 0 :
        j = last + 1
        last = i
    if i - j + 1 >= 2 : ans += i - j  # 啊啊啊啊啊啊啊啊啊啊啊啊！！！！！！！！！！！！！

print(ans)
