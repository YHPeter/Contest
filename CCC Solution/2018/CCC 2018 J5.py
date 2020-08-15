from collections import deque
q = deque()

n = int(input())
depth = [1,1]+[0]*(n-1)
ans = 100
points = [[]]
for i in range(n):
    points.append(list(map(int,input().split()[1::])))
    if points[-1]==[]: points[-1] = [0]

# bfs with depth
q.append(1)
while q:
    cur = q.popleft()
    for node in points[cur]:
        if node == 0: ans = min(ans,depth[cur])
        else:
            if depth[node] == 0:
                q.append(node)
                depth[node] = depth[cur]+1

if not 0 in depth: print('Y\n%d'%ans)
else: print('N\n%d'%ans)