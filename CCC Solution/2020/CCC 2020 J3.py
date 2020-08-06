upmax,upmin,sidemax,sidemin = 0,999,0,999
for i in range(int(input())):
    n,m = map(int,input().split(','))
    upmax,upmin,sidemax,sidemin = max(upmax,m),min(upmin,m),max(n,sidemax),min(n,sidemin)
print(str(sidemin-1)+','+str(upmin-1))
print(str(sidemax+1)+','+str(upmax+1))