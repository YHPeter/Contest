n,ans = map(int,input().strip().split())
x = []
for i in range(n):
    a,b = map(int,input().strip().split(' '))
    if a>b:
        x.append([b,a])
x.sort(key=lambda c: c[1],reverse=True)
x.sort(key=lambda c: c[0])
x+=[[ans,ans]]
gstart,gend = 0,0
for start,end in x:
    if start>=gend:
        ans+=(gend-gstart)*2
        gstart,gend = start,end
    else:
        gend = max(gend,end)
print(ans)
        

'''
1 78
78 3
'''
