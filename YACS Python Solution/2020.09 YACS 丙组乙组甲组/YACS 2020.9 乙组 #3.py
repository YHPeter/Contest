from collections import deque

depth = [[0]*500 for _ in range(500)]
n = int(input())
time = {}
totalban = set()
totalban.add('[0, 0]')
for i in range(n):
    t,x,y = map(int,input().split())
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1],[0,0]]:
        newx,newy = dx+x,dy+y
        h = time.get(t,[])
        if newx>=0 and newy>=0 and newx<=500 and newy<=500:
            h.append([newx,newy])
            time[t] = h
            totalban.add(str([newx,newy]))
ban = set(str(time.get(0)))
ban.add(str([0,0]))
# print(totalban)
q = deque()
q.append([0,0])
while q:
    x,y = q.popleft()
    timenow = depth[x][y]
    if not str([x,y]) in totalban:
        print(timenow)
        exit()
    h =  time.get(timenow,False)
    if h:
        for hh in map(str,h):
            ban.add(hh)

    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        newx,newy = dx+x,dy+y
        if newx>=0 and newy>=0 and newx<=500 and newy<=500 and not str([newx,newy]) in ban and depth[newx][newy]==0:
            q.append([newx,newy])
            depth[newx][newy]  = timenow+1

print('No Solution')

'''
4
0 1 0
2 0 1
2 3 3
1 1 4

ans: 3
'''

''' 
24
3 3 4
10 3 1
12 3 0
3 0 3
24 2 1
4 20 5
17 7 10
13 12 15
4 3 0
17 19 8
7 2 16
11 8 19
6 2 20
23 4 20
24 16 1
13 2 19
18 20 19
22 7 5
9 10 20
9 20 11
10 16 3
2 5 12
12 16 20
14 10 14
ans: 1
'''
# import sys
# print(list(map(lambda x: x.replace('\n',''), sys.stdin.readlines()[15:])))
