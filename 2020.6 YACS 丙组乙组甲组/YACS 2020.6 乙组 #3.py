# YACS 2020.6 乙组 #3.py
# 围三角形
'''
输出: 768
5 
1 1 3 3 4

输出: 71971200
10
31 23 12 12 11 17 26 28 16 34

输出: 1875
15
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

输出: 494887680
16
10 11 12 13 14 15 16 17 18 19 30 31 32 33 34 35
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


# Answer solution from c++, https://iai.sh.cn/contribution/148
ans,sum = 0,0
n = int(input())
side_list = [0]+list(map(int,input().split(' ')))
dp = [[1]*1600 for _ in range(1600)]
for i in range(1,n+1):
    x = side_list[i]
    sum+=x
    for i in range(sum,-1,-1):
        for j in range(sum-i,-1,-1):
            if i>=x: dp[i][j] |= dp[i - x][j]
            if j>=x: dp[i][j] |= dp[i][j - x]
for a in range(1,sum+1):
    for b in range(1,sum-a+1):
        c = sum-a-b
        if dp[a][b] == 1 and a + b > c and b + c > a and c + a > b:
            tmp = sum * (sum - 2 * a) * (sum - 2 * b) * (sum - 2 * c)
            ans = max(ans,tmp)
print(ans)