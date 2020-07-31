# YACS 2020.5 乙组 #3
# Dimond
'''
题目描述
给定一颗大号钻石，重量为 n 克拉。市场上，各种重量的钻石的价格是非常稳定的，每一颗重量为 ii 克拉的钻石，都可以卖出 ai元。假设切割钻石不会有任何损耗，请问应该如何切割钻石，才能使得售出的总价达到最高呢？

输入格式
第一行：单个整数 n；
第二行：n个整数，表示 a1, a2, a3...an 

输出: 95
输入:
7
10 28 39 40 50 60 70

输出: 12416
输入：
14
76 345 1217 3690 4363 4366 4907 5213 6668 6851 7927 8646 8862 8897

输出:17460
输入： 
20 
873 1085 1085 1116 1271 1271 1359 1876 2338 2844 4457 4950 5456 6700 7058 7522 7535 7977 8002 9916

输出:28900
输入： 
20 
1445 2014 2017 2415 2666 3011 3013 3633 3788 4187 4448 4974 5251 5581 5900 6701 7890 7989 9729 9966
'''
# 优化 100分
n= v = int(input())
value = list(map(int,input().split()))
goods = [[i+1,value[i]] for i in range(len(value))]
dp = [0 for i in range(v+1)]
for i in range(n):
    for j in range(v+1):
        if j >= goods[i][0]:
            dp[j] = max(dp[j], dp[j-goods[i][0]] + goods[i][1])
print(dp[-1])

# 没有优化 60分
n= v = int(input())
value = list(map(int,input().split()))
goods = [[i+1,value[i]] for i in range(len(value))]
dp = [0 for _ in range(v+1)]
for i in range(n):
    for j in range(v,-1,-1):
        k = j//goods[i][0]
        dp[j] = max([dp[j- x* goods[i][0]] + x * goods[i][1] for x in range(k+1)])
print(dp[-1])