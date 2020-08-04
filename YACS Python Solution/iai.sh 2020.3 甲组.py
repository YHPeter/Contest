# 甲组 2020年3月

# 1 sample answer from 
import sys,math

def gcd(a,b):
    return math.gcd(eval(a),eval(b))

def mark(x,r):
    if r < x or x < 0 or vis[x] == True: return
    vis[x] = True
    sum+=1
    mark(x + a,r)
    mark(x - b,r)

n,a,b = map(int,input().split(' '))
Gcd =  gcd(a,b),Rb = 2 * max(a,b)
num = (n / Gcd * Gcd - Rb) / Gcd
ans = 0
vis = [1]+[0]*1000100
for i in range(1,Rb+1):
    if i >= a and vis[i - a] == True: 
        mark(i,i)
        ans+=sum
    if i==n:
        print(ans)
        sys.exit()
ans += Gcd * ((sum + sum + num - 1) * num / 2) + num
ans += (n % Gcd) * (sum + num)
print(ans)