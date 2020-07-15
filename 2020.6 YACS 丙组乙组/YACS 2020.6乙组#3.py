# YACS 2020.6乙组#3.py
'''行号0: 标准输出: 22907/56 标准输入： ['10 3\n', '629 13\n', '53 19\n', '151 8\n', '927 2\n', '372 19\n', '630 6\n', '230 20\n', '371 2\n', '13 6\n', '65 11\n']
输出: 39031/63 标准输入： ['10 3\n', '54 16\n', '105 4\n', '266 10\n', '679 1\n', '65 10\n', '751 1\n', '864 10\n', '587 19\n', '596 8\n', '631 20\n']
出: 76666/107 标准输入： ['10 1\n', '214 2\n', '759 17\n', '718 15\n', '509 17\n', '305 6\n', '919 12\n', '984 19\n', '622 9\n', '20 13\n', '676 10\n']
3 1
100 99
90 99
80 1

output:499/5'''
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