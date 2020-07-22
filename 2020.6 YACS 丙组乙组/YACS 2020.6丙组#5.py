# YACS 2020.6丙组 #5
# 影厅选座
# sample solution from https://iai.sh.cn/contribution/175
'''
3 3 4
XXX
XX.
XX.

No Solution

4 5 5
..XXX
X.XXX
XX.X.
XX...

6
'''
import sys
a = [[0]*1101 for _ in range(1102)]
ans = 999999999
num= 0

def two_pointers(l,r):
    sum = 0
    global ans
    global cnt
    u = 1
    for b in range(1,m+1):
        while u <= m and sum < cnt:
            sum += a[u][r] - a[u][l - 1]
            u+=1
        if sum < cnt: break
        ans = min(ans,(r - l + 1) * (u - b))
        sum -= a[b][r] - a[b][l - 1]

n,m,cnt = map(int,input().split(' '))

for i in range(1,n+1):
    x = input().strip()
    for j in range(1,len(x)+1):
        num += (x[j-1]=='.')
        a[i][j] = a[i][j - 1] + (x[j-1] == '.')

if num<cnt:
    print('No Solution')
    sys.exit()
for l in range(1,n+1):
    for r in range(l,m+1):
        two_pointers(l,r)
print(ans)