n,k = map(int,input().split())
x = list(map(int,input().split()))
dic = {}

for i in range(n):
    dic[x[i]] = dic.get(x[i],0)+1

print(sum(sorted(list(dic.values()), reverse = True)[k:]))