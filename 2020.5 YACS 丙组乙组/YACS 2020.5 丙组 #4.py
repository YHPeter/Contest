# YACS 2020.5 丙组 #4
'''
增长或翻倍
内存限制: 256 Mb时间限制: 1000 ms
题目描述
给定正整数 s 和 t，保证 s<t，小爱打算使用增长或翻倍操作，让 s 变成 t。
增长操作可以让数字加一，即 x←x+1；
翻倍操作可以让数字翻倍，即 x←2×x。
请问小爱最少需要使用多少步操作才能将 s 变成 t？

输入格式
单独一行：两个正整数，分别表示 s 与 t。

输出格式
单个整数：表示最少操作步数。
 ；
样例数据
输入:
1 4
输出:
2
说明:
1->2->4
输入:
2 10
输出:
3
说明:
2->4->5->10
'''
# 超时
s,t = list(map(int,input().split(' ')))
dp = [0 for i in range(s,t+1)]
dp[0]=0
dp[1]=1
for i in range(1,t-s+1):
    if (i+s)%2==0:
        dp[i] = min(dp[i-1]+1,dp[int((i+s)//2)-s]+1)
    else:
        dp[i] = dp[i-1]+1
print(dp[t-s])

# # 超时
s,t = list(map(int,input().split(' ')))
dp = [999999 for i in range(t+1)]
dp[s]=0
dp[s+1]=1
for i in range(s+1,t+1):
    if i%2==0:
        dp[i] = min(dp[i-1]+1,dp[int(i//2)]+1)
    else:
        dp[i] = dp[i-1]+1
print(dp[t])