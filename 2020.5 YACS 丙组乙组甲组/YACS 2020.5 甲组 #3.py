# YACS 2020.5 甲组 #3
'''
3 4 2
1 2 20
2 3 30
1 3 40
1 3 10
1 3
3 4
'''
# sample answer from https://iai.sh.cn/contribution/131
N = 105
M = 40010
INF = 1061109567;
a = [0]*M
b = [0]*M
c = [0]*M
g = [[INF]*N for _ in range(N)] # 邻接矩阵 
dist = [INF]*N # 某个点和集合相连的最小边权 
st = [False]*M # 某个点是否在集合内 

def prim():
    res = 0
    for i in range(1,n+1):
        t = -1
        for j in range(1,n+1):
            #从集合外的点中，找出和集合中的点之间的的边权最小的点t 
            if (not st[j]) and (t == -1 or dist[j] < dist[t]): t = j
        #如果集合外所有的点都不和集合内的点连通，则不存在最小生成树 
        if i > 1 and dist[t] == INF: return INF
        #将点t加入集合，将权重值增加 
        st[t] = True
        if i > 1: res += dist[t]
        #把点t加入集合之后，其它点到集合中的点的边权最小值可能需要更新 
        for j in range(1,n+1): 
            dist[j] = min(dist[j], g[t][j])
    return res

n,m,q = map(int,input().split(' '))

#保存m条边的信息
for i in range(1,m+1):
    a[i], b[i], c[i] = map(int,input().split(' '))


while q:
    q-=1
    l,r = map(int,input().split(' '))
    
    #由查询区间内的边组成图，用二维数组邻接矩阵存储图的信息
    #如果两点之间有重边，则存储最小的权重 
    for i in range(l,r+1):
        #因为是无向图，所以建两条边 
        g[a[i]][b[i]] = g[b[i]][a[i]] = min(g[a[i]][b[i]], c[i])

    t = prim()
            
    if t == INF: print("-1")
    else: print(t)
    