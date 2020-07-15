# YACS 2020.6乙组#2.py
'''
5
21 38 12 24 13
'''
def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))*16
def tri(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    return True
n = int(input())
t = [int(i) for i in input().split()]
total_length = sum(t)
dp = [[1 for _ in range(int(n*40/2))] for _ in range(int(n*40/2))]
dp[0][0] = 1
for i in range(n):
    for j in range(int(total_length/2)+1,0,-1):
        for k in range(int(total_length/2)+1,0,-1):
            if ((j >= t[i] and dp[j-t[i]][k]) or (k >= t[i] and dp[j][k-t[i]])):
                dp[j][k] = 1
ans = -1
for i in range(int(total_length/2)+1):
    for j in range(int(total_length/2)+1):
        if (dp[i][j] and tri(i, j, total_length-i-j) and ans < area(i, j, total_length-i-j)):
                ans = area(i, j, total_length-i-j)
print(int(ans))