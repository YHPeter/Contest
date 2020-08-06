data = []
for i in range(int(input())):
    data.append(list(map(int,input().split())))
data.sort()
ans = 0

for i in range(1,len(data)):
    ans = max(ans,abs(data[i][1]-data[i-1][1])/(data[i][0]-data[i-1][0]))
print(ans)