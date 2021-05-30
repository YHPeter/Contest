import sys
n = int(input())
h = list(map(int,input().split()))
w = list(map(int,input().split()))

ans = 0
for i in range(n):
    ans+=(h[i]+h[i+1])*w[i]/2

print(ans)