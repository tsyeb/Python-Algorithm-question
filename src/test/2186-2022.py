"""
将 2022 拆分成 10 个互不相同的正整数之和, 总共有多少种拆分方法?

问题可转化为 容积为10的背包有多少装法
"""
n = 2022
dp = [[0] * 2023 for _ in range(11)]
dp[0][0] = 1

for i in range(1, 2023) :
    for j in range(10, 0, -1) :
        for k in range(i, 2023) :
            dp[j][k] += dp[j - 1][k - i]

print(dp[10][2022])
