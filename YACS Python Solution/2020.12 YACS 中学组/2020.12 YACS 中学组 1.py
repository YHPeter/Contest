# 排列计数
import math
n = int(input())
li = tuple(map(int, input().split()))
not_visited = set([x for x in range(1, n+1)])

l,r = 1, math.perm(n,n)
for i in range(n-1):
    part = (r-l+1)//(n-i)
    l += part*(li[i]-min(not_visited))
    r -= part*(max(not_visited)-li[i])
    not_visited.remove(li[i])
print(r)