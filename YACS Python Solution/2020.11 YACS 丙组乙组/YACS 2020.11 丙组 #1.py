n,m = map(int,input().split())
for i in range(n,m+1):
    if i%7==0 or (str(i)[-1]=='7' ): print('pass')
    else: print(i)