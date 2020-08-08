# YACS 2020.8 乙组 #3

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
    graph[a] = graph.get(a,set([b]))
    graph[a].add(b)
    graph[b] = graph.get(b,set([a]))
    graph[b].add(a)

res = [1]

def dfs(start,end,visited):
    visited.append(start)
    if end in graph[start]: return visited
    for choose in sorted(list(graph[start])):
        visited.append(start)
        dfs(choose,end,visited)
    return visited
        

for i in range(2,n):
    # if len(res)==n: break
    if not i in res:
        visited = []
        res+=dfs(res[-1],i,visited)+[i]

print(res)
