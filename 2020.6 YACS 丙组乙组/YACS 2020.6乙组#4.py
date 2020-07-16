# YACS 2020.6 乙组 #4.py
'''
输出: 22907/56 输入： ['10 3\n', '629 13\n', '53 19\n', '151 8\n', '927 2\n', '372 19\n', '630 6\n', '230 20\n', '371 2\n', '13 6\n', '65 11\n']
输出: 39031/63 输入： ['10 3\n', '54 16\n', '105 4\n', '266 10\n', '679 1\n', '65 10\n', '751 1\n', '864 10\n', '587 19\n', '596 8\n', '631 20\n']
输出:76666/107 输入： ['10 1\n', '214 2\n', '759 17\n', '718 15\n', '509 17\n', '305 6\n', '919 12\n', '984 19\n', '622 9\n', '20 13\n', '676 10\n']
10 1
214 2
759 17
718 15
509 17
305 6
919 12
984 19
622 9
20 13
676 10

输出:499/5
3 1
100 99
90 99
80 1
'''
'''
# TLE
import sys,itertools
from fractions import Fraction
n,k = map(int,input().split(' '))
total_up, total_down,ans,x = 0,0,0,[]
for i in list(sys.stdin.readlines()):
    x+=[[int(i.strip().split()[0])*int(i.strip().split()[1]),int(i.strip().split()[1])]]
    total_down+=x[-1][1]
    total_up+=x[-1][0]
for h in range(k+1):
    drop = list(itertools.combinations(x,h))
    while drop:
        up,down = 0,0
        for i in drop.pop():
            up,down = up+i[0],down+i[1]
        ans = max(ans,Fraction(total_up-up,total_down-down))
print(ans)
'''
# Sample anser from https://iai.sh.cn/contribution/154

def gcd(x,y):
    if y==0: return x
    else: return gcd(y,x%y)
s = [0]*100005
c = [0]*100005
withdraw = [0]*10005
n,k = map(int,input().split(' '))
ttl,pt = 0,0
for i in range(1,n+1):
    s[i],c[i] = map(int,input().split(' '))
    ttl += s[i]*c[i]
    pt += c[i]
max_ttl = ttl
max_pt = pt
while k:
    t = 0
    for i in range(1,n+1):
        if withdraw[i]: continue
        a = ttl - s[i] * c[i]
        b = pt - c[i]
        if (a/b) > (max_ttl/max_pt):
            max_ttl = a
            max_pt = b
            t = i
    if t==0: break
    ttl = max_ttl
    pt = max_pt
    withdraw[t] = 1
    k-=1
if max_ttl % max_pt == 0: print(max_ttl / max_pt)
else: print(str(int(max_ttl / gcd(max_ttl, max_pt)))+'/'+str(int(max_pt / gcd(max_ttl, max_pt))))
	