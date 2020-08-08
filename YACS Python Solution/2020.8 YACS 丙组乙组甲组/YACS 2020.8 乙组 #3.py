# YACS 2020.8 乙组 #3
'''
3 4
1 3
1 4
2 4
2 3
[1,3,2,4]

5 5
1 3
1 4
2 5
3 5
3 4
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n,m = stdinput()
graph = {}
for i in range(m):
    a,b = stdinput()
    graph[a],graph[b] = graph.get(a,set([b])),graph.get(b,set([a]))
    graph[a].add(b)
    graph[b].add(a)

def dfs(start,end,visited):
    visited.append(start)
    if end in graph[start]:
        visited.append(end)
        return visited
    for choose in sorted(list(graph[start])):
        if choose in visited: continue
        visited.append(choose)
        dfs(choose,end,visited)
    return visited

res = [1]
for i in range(2,n):
    if not i in res: res+=dfs(res[-1],i,[])+[i]

ans,alin = [],set()
for i in res:
    if not i in alin: 
        ans.append(i)
        alin.add(i)
print(ans)
