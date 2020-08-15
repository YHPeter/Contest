from collections import deque

n = int(input())
points = [[]]
for i in range(n):
    points.append(list(map(int,input().split())))
visited,depth = [True,True]+[False]*(n-1),[1,1]+[0]*n
ans = 100
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for node in points[cur]:
        if node == 0:
            ans = min(ans,depth[cur])
        else:
            if not visited[node]:
                q.append(node)
                depth[node] = depth[cur]+1
                visited[node] = True

if not False in visited: print('Y\n%d'%ans)
else: print('N\n%d'%ans)

'''Sample Input 1
3
2 2 3
0
0
Output for Sample Input 1
Y
2
Explanation of Output for Sample Input 1
Since we start on page 1, and can reach both page 2 and page 3, all pages are reachable. The only
paths in the book are 1 → 2 and 1 → 3, each of which is 2 pages in length.
Sample Input 2
3
2 2 3
0
1 1
Output for Sample Input 2
Y
2
'''