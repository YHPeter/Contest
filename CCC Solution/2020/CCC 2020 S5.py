n = int(input())
b = list(map(int,input().split()))
nb = max(b) #number of hambergers 

dp =[[0]*max(b) for _ in n]
dp[0][0] = 1/n