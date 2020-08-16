a,b = map(int,input().split())
c,d = map(int,input().split())
e = int(input())

if e>=abs(a-c)+abs(b-d) and (e-abs(a-c)+abs(b-d))%2==0: print('Y')
else: print('N')