q = int(input())
n = int(input())
d = list(map(int,input().split()))
p = list(map(int,input().split()))


if q==1:
    same = []
    for x in d:
        if x in p:
            same.append(x)
            p.remove(x)
    for x in same:
        d.remove(x)
    d.sort()
    p.sort()
    ans=0
    for i in range(len(d)):
        ans+=max(d[i],p[i])
    print(ans+sum(same))
else:
    d.sort()
    p.sort(reverse=True)
    ans=0
    for i in range(len(d)):
        ans+=max(d[i],p[i])
    print(ans)