# YACS 2020.5 丙组 #3
'''
扫雷
内存限制: 256 Mb时间限制: 1000 ms
题目描述
给定 n×m 个字符，每个字符代表所属的位置是否有地雷，如果有雷，则用 * 表示，如果没有，用 . 表示。请对每个没有地雷的方格统计它的周围八个方格内，有多少个地雷，并将统计结果输出。
输入格式
第一行：两个正整数 nn 和 mm；
接下来有 n×m 个字符，表示每个方格是否存在地雷。

IN:
3 3
*.*
...
*..
OUT:
*2*
231
*10

IN:
3 4
*..*
.**.
.*.*
OUT:
*33*
3**3
2*4*

'''
# version 1 
n,m = list(map(int,input().split(' ')))
li = [[0 for _ in range(m+2)]]
lei = []
for i in range(n):
    inm = [0]+list(input())+[0]
    for j in range(m+2):
        if inm[j]=='*':
            lei.append([j,i+1])
        elif inm[j]=='.':
            inm[j]=0
    li.append(inm)
li = li+[[0 for _ in range(m+2)]]
for x,y in lei:
    for cx,cy in [[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,1],[0,-1]]:
        if not [x+cx,y+cy] in lei:
            li[y+cy][x+cx] = int(li[y+cy][x+cx]) + 1
for i in range(1,n+1):
    print("".join(map(str,li[i][1:m+1])))

# version 2

'''
3 4
*..*
.**.
.*.*
'''

'''
0. . . . .
1. * 1 1 *

2. * 3 3 *
   2 * * 2
 OUT: * 3 3 *
3. 3 * * 3
   2 * 4 *
 OUT: 3 * * 3

'''

n,m = list(map(int,input().strip().split(' ')))
pre_lay,cur_lay,next_lay = [0 for _ in range(m+2)],[],[]
res =[]

for i in range(n):
    cur_lay = [0]+list(input().replace('.','0'))+[0]
    for k in next_lay:
        cur_lay[k] = (int(cur_lay[k])+1) if cur_lay[k]!='*' else '*'
        cur_lay[k-1] = (int(cur_lay[k-1])+1) if cur_lay[k-1]!='*' else '*'
        cur_lay[k+1] = (int(cur_lay[k+1])+1) if cur_lay[k+1]!='*' else '*'
    next_lay=[]
    for j in range(1,m+2):
        if cur_lay[j]=='*':
            next_lay.append(j)
            cur_lay[j-1] = (int(cur_lay[j-1])+1) if cur_lay[j-1]!='*' else '*'
            cur_lay[j+1] = (int(cur_lay[j+1])+1) if cur_lay[j+1]!='*' else '*'
            pre_lay[j] = (pre_lay[j]+1) if pre_lay[j]!='*' else '*'
            pre_lay[j-1] = (pre_lay[j-1]+1) if pre_lay[j-1]!='*' else '*'
            pre_lay[j+1] = (pre_lay[j+1]+1) if pre_lay[j+1]!='*' else '*'
    if i==0: pass
    else: print(''.join(map(str,pre_lay[1:m+1])))
    pre_lay = cur_lay
print(''.join(map(str,pre_lay[1:m+1])))


import sys
n,m = list(map(int,input().strip().split(' ')))
c = sys.stdin.readlines()
pre_lay,cur_lay,next_lay = [0 for _ in range(m+2)],[],[]
res =[]

for i in range(n):
    cur_lay = [0]+list(c[i].strip().replace('.','0'))+[0]
    for k in next_lay:
        cur_lay[k] = (int(cur_lay[k])+1) if cur_lay[k]!='*' else '*'
        cur_lay[k-1] = (int(cur_lay[k-1])+1) if cur_lay[k-1]!='*' else '*'
        cur_lay[k+1] = (int(cur_lay[k+1])+1) if cur_lay[k+1]!='*' else '*'
    next_lay=[]
    for j in range(1,m+2):
        if cur_lay[j]=='*':
            next_lay.append(j)
            cur_lay[j-1] = (int(cur_lay[j-1])+1) if cur_lay[j-1]!='*' else '*'
            cur_lay[j+1] = (int(cur_lay[j+1])+1) if cur_lay[j+1]!='*' else '*'
            pre_lay[j] = (pre_lay[j]+1) if pre_lay[j]!='*' else '*'
            pre_lay[j-1] = (pre_lay[j-1]+1) if pre_lay[j-1]!='*' else '*'
            pre_lay[j+1] = (pre_lay[j+1]+1) if pre_lay[j+1]!='*' else '*'
    if i==0: pass
    else: print(''.join(map(str,pre_lay[1:m+1])))
    pre_lay = cur_la
print(''.join(map(str,pre_lay[1:m+1])))
