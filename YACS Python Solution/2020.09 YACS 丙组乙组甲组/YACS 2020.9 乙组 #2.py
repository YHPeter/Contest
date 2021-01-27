n,l = map(int,input().split())
line = sorted(list(map(int,input().split())))
ans = 0
for i in range(n):
    start = line[i]
    j = 1
    while i+j<n and line[i+j]-start<=l:
        j+=1
        ans+=1

print(ans)