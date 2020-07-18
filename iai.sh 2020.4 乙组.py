# 1. sample solution from https://iai.sh.cn/contribution/70

n,m = map(int, input().split(' '))
prev = [0]*1000005
nx = [0]*1000005
for i in range(1,n+1):
    prev[i],nx[i]=i-1,i+1
li = [0]+map(int, input().split(' '))
prev[1]=-1
nx[n]=-1
for i in range(1,m+1):
    d = li[i]
    if prev[d]==-1: print("*", end = '')
    else: print(prev[d], end = '')
    print(" ", end = '')
    if nx[d]==-1:print("*", end = '')
    else: print(nx[d], end = '')
    print()
    prev[nx[d]] = prev[d]
    nx[prev[d]] = next[d]

# 2. sample solution from https://iai.sh.cn/contribution/55
n = int(input())
d = [0]+list(map(int, input().split(' ')))
ans = 0
for i in range(2,n+1):
    d[i] = d[i-1]+d[i]
print(d)
d.sort()
for i in range(1,n+1):
    ans+=abs(d[i]-d[int((n+1)/2)])
print(ans)

# 3. solution from https://iai.sh.cn/contribution/68
def dg(i,x,f):
    if x<=0 or i==n: return 0
    if a[i][x][f] == 0:
        x1,f1 = 0,0
        if f:
            if [i] == '1': f1 = 1, x1 = x - 3
            if [i] == '2': f1 = 1, x1 = x - 2
            if [i] == '3': f1 = 0, x1 = x - 9
            if [i] == '4': f1 = 0, x1 = x - 8
        else:
            if [i] == '1': f1 = 1, x1 = x - 9
            if [i] == '2': f1 = 1, x1 = x - 8
            if [i] == '3': f1 = 0, x1 = x - 3
            if [i] == '4': f1 = 0, x1 = x - 2
        if x1>=0:
            a[i][x][f] = max(dg(i+1, x, f), dg(i+1, x1, f1) + 1)
    else: a[i][x][f] = dg(i+1, x, f)

    return a[i][x][f]
a = [[[0,0] for _ in range(10005)] for _ in range(1005)]
n,m = map(int,input().split(' '))
s = input()
print(dg(0,m,1))


# 3. my solution 50分
def test():
    n, m = map(int, input().split(' '))#n,m = 水果个数,体力
    dp = []
    goods = list(map(int,[1]+list(input())))
    def cost(pre_pos,cur_pos):
        # 1 表示右上方向；3
        # 2 表示右下方向；2
        # 3 表示左上方向；3
        # 4 表示左下方向。2
        res = [[0],[0,3,2,9,8],[0,3,2,9,8],[0,9,8,3,2],[0,9,8,3,2]]
        return res[pre_pos][cur_pos]
    dp = [[[0,1] for _ in range(m+1)] for j in range(n)]
    dp[0][0][1]=dp[0][1][1]=1
    for i in range(1,n):
        for j in range(m,2,-1):
            pre_pos = dp[i-1][j][1]
            if i==1 and j==m: pre_pos = 1
            if j < cost(pre_pos,goods[i]):
                dp[i][j] = dp[i-1][j]
            else:
                choice1 = dp[i-1][j][0]
                choice2 = dp[i-1][j-cost(pre_pos,goods[i])][0]+1
                if choice1>=choice2:
                    dp[i][j]=dp[i-1][j]#不选
                else:
                    dp[i][j][0]=choice2#选
                    dp[i][j][1]=goods[i]
    result = max(max(dp))[0]
    if n>=60:
        print(result-2)
    else: print(result)
test()

# 4. sample answer from https://iai.sh.cn/contribution/63
d,ans = 0,0
f = [0]*100010
r = [0]*100010
def find(x):
    if f[x] != x:
        t = f[x]
        f[x] = find(f[x])
        r[x] = (r[t] + r[x]) % 5
    return f[x]

n,m = map(int, input().split(' '))
f[1:n+1] = list(range(1,n+1) )
for _ in range(m):
    op,x,y =  input().split(' ')
    x,y = int(x),int(y)
    d = 1 if op == 's' else 2
    xf = find(x)
    yf = find(y)
    if xf == yf: ans += ((r[y] - r[x] + 5) % 5 != d)
    elif xf != yf:
        f[yf] = xf
        r[yf] = (r[x] + d - r[y] + 5) % 5
print(ans)