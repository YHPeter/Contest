n = int(input())
ans = 0
for l in range(n,1,-1):
    a = n/l+0.5-l/2
    if a>0 and float(str(a).split('.')[1])==0:
        ans+=1
        for i in range(int(a),int(a)+l):
            print(i,end=' ')
        print()

if not ans: print('None')