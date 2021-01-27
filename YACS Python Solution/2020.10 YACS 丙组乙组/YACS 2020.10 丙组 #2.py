n,m = map(int,input().split())
x = [0]+list(map(int,input().split()))
ans = 0
for i in range(m):
    a,b = map(int,input().split())
    ans+=x[a]*b
print(ans)