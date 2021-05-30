import sys
m,n,k = int(input()),int(input()),int(input())
# 0 true, 1 false
row, col = [False]*(m+1),[False]*(n+1)
# options = sys.readlines()
for h in range(k):
    opt,index = input().split()
    index = int(index)

    if opt=='R':
        row[index] = not(row[index])
    elif opt=='C':
        col[index] = not(col[index])

ans = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if row[i]^col[j]: ans += 1

print(ans)