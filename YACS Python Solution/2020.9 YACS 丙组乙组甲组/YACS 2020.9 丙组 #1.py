'''
枚举n<=10时的答案

for n in range(1,10):
    ans = 0
    for i in range(2<<n-1):
        if i^(2*i)^(3*i) == 0: ans+=1
    print(n, ans)
# Output:
# n answer
# 1 2
# 2 3
# 3 5
# 4 8
# 5 13
# 6 21
# 7 34
# 8 55
# 9 89
# 10 144
amazing啊！结果符合斐波那契数列，直接写：
斐波那契数列 - 最经典的动归
转移方程： dp[i] = dp[i-1]+dp[i-2]
加上常数优化和取模就好了~~~
'''
n = int(input())
for i in range(int(10000000**0.5),0,-1):
    if i<=n and n%(i**2)==0: 
        print(i**2)
        exit()