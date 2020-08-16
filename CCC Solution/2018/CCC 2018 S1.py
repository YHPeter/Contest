n = int(input())
vil = [int(input()) for _ in range(n)]
vil.sort()
inter = []
for i in range(n-1):
    inter.append((vil[i]+vil[i+1])/2)
ans = abs(inter[1]-inter[0])
for i in range(1,n-2):
    ans = min(ans,abs(inter[i+1]-inter[i]))
print(ans)
