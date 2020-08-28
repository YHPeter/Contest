from collections import deque

row,column = int(input()),int(input())
max_ad = row*column
adj = {}
visited = set()
for i in range(1,row+1):
    x = [0]+list(map(int,input().split()))
    for j in range(1,column+1):
        next,cross = x[j],i*j
        if cross<=max_ad and next<=max_ad:
            if adj.get(next,False):
                adj[next].add(cross)
            else: adj[next] = set([cross])

q = deque()
q.append(max_ad)
while q:
    cur = q.popleft()
    if cur==1:
        print('yes')
        exit()
    for i in adj.get(cur,[]):
        if not i in visited:
            visited.add(i)
            q.append(i)

print('no')