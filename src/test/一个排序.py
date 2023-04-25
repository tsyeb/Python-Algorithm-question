import os
import sys

# 请在此输入您的代码
total = 300
table = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
num_cnt = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
xx = sorted(table.items(), key=lambda x: (x[1], -int(x[0])), reverse=False)
print(xx)
nums = []
for i in xx:
    for j in range(10):
        # print(num_cnt[i[0]])
        if num_cnt[i[0]] < 10 and total > 0:
            nums.append(i[0])
            total -= table[i[0]]

print(''.join(sorted(nums, reverse=True)))
