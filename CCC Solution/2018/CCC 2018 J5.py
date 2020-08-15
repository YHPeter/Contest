from typing import Counter, Deque

n = int(input())
points = [0]
q = Deque()
for i in range(n):
    points.append(list(map(int,input().split())))
visited = set([1])
q.append(1)
depth = [0,1]+[999999999]*n
endpoint = set()
def dfs(cur,depth):
    if points[cur]==[0] or cur in endpoint:
        endpoint.add(cur)
    else:
        count = 0
        for j in points[cur]:
            if not j in visited:
                q.append(j)
                visited.add(j)
                depth[j] = min(depth[j],depth[cur]+1)
            else: count+=1
        # if count == len(points[cur]): endpoint.add(cur)
dep = []
for i in range(1,n):
    if i in visited and i in endpoint: dep.append(depth[i])
print(dep)
if len(visited)==n:print('Y\n%d'%min(dep))
else:print('N\n%d'%min(dep))

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