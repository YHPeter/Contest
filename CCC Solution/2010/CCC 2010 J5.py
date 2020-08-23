bx,by = map(int,input().split())
tx,ty = map(int,input().split())
from typing import Deque
q = Deque()
q.append([bx,by])
depth = [[0]*9 for _ in range(9)]
while q:
    cx,cy = q.popleft()
    if cx==tx and ty==cy:
        print(depth[cx][cy])
        exit()
    for dx,dy in [[2,1],[1,2],[-1,-2],[-1,2],[-2,-1],[2,-1],[-2,1],[1,-2]]:
        nx,ny = dx+cx,cy+dy
        if nx>0 and nx<=8 and ny>0 and ny<=8 and depth[nx][ny]==0:
            q.append([nx,ny])
            depth[nx][ny] = depth[cx][cy]+1