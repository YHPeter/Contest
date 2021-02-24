import sys, functools, itertools
input = sys.stdin.readline
from collections import defaultdict
from heapq import *

ans = 0
n,m = map(int,input().split())
tree = [0]*n
depth = [0]*n
target = list(map(int,input().split()))
pairs = []
for _ in range(n-1):
    a,b = map(int,input().split())
    pairs.append([a,b])
    # if a>b: a,b = b,a
    # tree[b] = a
    # depth[b] = depth[a]+1
level_max = [0]
visited_p = []
for level in range(n):
    level_next = []
    for a,b in pairs:
        if [a,b] in visited_p: continue
        if a in level_max:
            tree[b] = a
            depth[a] = level
            depth[b] = level+1
            level_next.append(b)
            visited_p.append([a,b])
        elif b in level_max:
            tree[a] = b
            depth[b] = level
            depth[a] = level+1
            level_next.append(a)
            visited_p.append([a,b])
    level_max = level_next

    
print(tree, depth)

flag = False
sonset = {x:set([x]) for x in range(n)}
sett = set(target)

point = 0
for dep in range(max(depth),-1,-1):
    for i in range(n):
        if depth[i]==dep:
            sonset[tree[i]]|=set([i])
            sonset[tree[i]]|=sonset[i]
            if sett <= sonset[i]:
                flag, point = True, i
    if flag: break
# print(point, sonset)
# +sum([1 for i in range(m) if target[i]!=0])
visited = set(target)
for _ in range(max(depth)):
    target = [tree[x] for x in target if x!= point]
    
    ans+=len(target)
    if target==[point]*len(target): break
    counter = {x:[0,[]] for x in range(n)}
    for i,x in enumerate(target):
        counter[x][0]+=1
        counter[x][1].append(i)

    for i in range(n):
        if i==point: continue
        if i in visited:
            for index in counter[i][1]:
                target[index] = point
            if counter[i][0]>1: ans+=counter[i][0]-1
        else:
            if counter[i][0]>1:
                for index in counter[i][1][1:]:
                    target[index] = point
                ans+=counter[i][0]-1
    visited |= set(target)
print(ans)




'''
8 7
0 1 2 3 4 5 6
0 1
0 2
2 3
4 3
6 1
1 5
7 3
'''