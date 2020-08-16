'''Sample Input 1
4 5
WWWWW
W.W.W
WWS.W
WWWWW
Output for Sample Input 1
-1
2
1
Explanation of Output for Sample Input 1
The robot cannot move to the top left empty cell because it is blocked by walls.
The top right empty cell can be reached in 2 steps and the bottom right empty cell can be reached
in 1 step.
Sample Input 2
5 7
WWWWWWW
WD.L.RW
W.WCU.W
WWW.S.W
WWWWWWW
Output for Sample Input 2
2
1
3
-1
-1
1
'''

from collections import deque


rr,ww = map(int,input().split())
graph = []
for i in range(rr):
    graph.append(input())

empty = []
camera = []
wall = []
conveyor = {}
graphs = {}

for r in range(rr):
    for w in range(ww):
        if graph[r][w] == '.': empty.append([r,w])
        elif graph[r][w] == 'W': wall.append([r,w])
        elif graph[r][w] == 'S': start = [r,w]
        elif graph[r][w] == 'C': camera.append([r,w])
        elif graph[r][w] == 'L': conveyor[str([r,w])] = [r,w-1]
        elif graph[r][w] == 'R': conveyor[str([r,w])] = [r,w+1]
        elif graph[r][w] == 'U': conveyor[str([r,w])] = [r-1,w]
        elif graph[r][w] == 'D': conveyor[str([r,w])] = [r+1,w]

deny = wall[::] + camera[::]

for r,w in camera:
    for dr,dw in [[0,1],[1,0],[0,-1],[-1,0]]:
        for i in range(1,min(rr-r,ww-w,r+1,w+1)):
            nr,nw = r+dr*i,w+dw*i
            if [nr,nw] in wall: break
            if nr>0 and nr<rr and nw>0 and nw<ww and not [nr,nw] in deny and not str([nr,nw]) in conveyor.keys(): deny.append([nr,nw])
            


depth = {str(start):1}
for i in range(len(empty)):
    r,w = empty[i]
    depth[str([r,w])]=0

for i in conveyor.keys():
    r,w = map(int,i.replace('[','').replace(']','').split(','))
    depth[str([r,w])]=0


q = deque()
q.append(start)
while q:
    r,w = q.popleft()
    x = conveyor.get(str([r,w]),False)
    if x:
        nr,nw = x
        if not [nr,nw] in deny and depth[str([nr,nw])]==0:
            q.append([nr,nw])
            depth[str([nr,nw])] = depth[str([r,w])]
        continue

    for dr,dw in [[0,1],[1,0],[0,-1],[-1,0]]:
        nr,nw = r+dr,w+dw
        if not [nr,nw] in deny and depth[str([nr,nw])]==0:
            q.append([nr,nw])
            depth[str([nr,nw])] = depth[str([r,w])]+1

for r,w in empty:
    if str([r,w]) in depth.keys() and depth[str([r,w])]!=0: print(depth[str([r,w])]-1)
    else: print(-1)