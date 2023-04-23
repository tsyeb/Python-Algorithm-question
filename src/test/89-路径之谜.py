"""
路径之谜
题目

题解
(215)
记录
(39)
题目描述
小明冒充
�
X 星球的骑士，进入了一个奇怪的城堡。

城堡里边什么都没有，只有方形石头铺成的地面。

假设城堡地面是
�
×
�
n×n 个方格。如下图所示。

图1

按习俗，骑士要从西北角走到东南角。可以横向或纵向移动，但不能斜着走，也不能跳跃。每走到一个新方格，就要向正北方和正西方各射一箭。（城堡的西墙和北墙内各有
�
n 个靶子）同一个方格只允许经过一次。但不必走完所有的方格。如果只给出靶子上箭的数目，你能推断出骑士的行走路线吗？有时是可以的，比如上图中的例子。

本题的要求就是已知箭靶数字，求骑士的行走路径（测试数据保证路径唯一）

输入描述
第一行一个整数
�
N (
0
≤
�
≤
20
0≤N≤20)，表示地面有
�
×
�
N×N 个方格。

第二行
�
N 个整数，空格分开，表示北边的箭靶上的数字（自西向东）

第三行
�
N 个整数，空格分开，表示西边的箭靶上的数字（自北向南）

输出描述
输出一行若干个整数，表示骑士路径。

为了方便表示，我们约定每个小格子用一个数字代表，从西北角开始编号: 0,1,2,3
⋯
⋯
比如，上图中的方块编号为：

0 1 2 3

4 5 6 7

8 9 10 11

12 13 14 15

输入输出样例
示例
输入

4
2 4 3 4
4 3 3 3
copy
输出

0 4 5 1 2 3 7 11 10 9 13 14 15
copy
运行限制
最大运行时间：5s
最大运行内存: 256M
总通过次数: 1890  |  总提交次数: 2492  |  通过率: 75.8%

难度: 简单   标签: DFS, 2016, 国赛

版权声明
部分题目由用户贡献，若您是著作权持有人，请与我们联系。

随机一题
上一题
下一题
编译语言:
C++
1234567
#include <iostream>
using namespace std;
int main()
{
  // 请在此输入您的代码
  return 0;
}
打开控制台
北 西
"""
import sys
sys.setrecursionlimit(1000000)


def check():

    # 检查是否符合箭的数量
    remain = sum(North) + sum(West)
    if remain == 0:
        return True
    else:
        return False

def dfs(x, y):
    global North
    global West
    global q
    global flag

    if x == n - 1 and y == n - 1:
        if check():
            print(*q)
            flag = 1
            return

    for u, v in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        qx = x + u
        qy = y + v

        # 当以下情况时，退出
        if qx < 0 or qx >= n or qy < 0 or qy >= n:
            continue
        elif vis[qx][qy]:
            continue
        elif North[qy] == 0 or West[qx] == 0:
            continue

        # 可通过
        North[qy] -= 1
        West[qx] -= 1
        q.append(qx * n + qy)
        vis[qx][qy] = True

        dfs(qx, qy)

        North[qy] += 1
        West[qx] += 1
        q.pop()
        vis[qx][qy] = False


n = int(input())
North = list(map(int, input().split()))
West = list(map(int, input().split()))

vis = [[False] * n for _ in range(n)]
q = [0]
North[0] -= 1
West[0] -= 1
flag = 0


dfs(0, 0)
if flag == 0:
    print(-1)
