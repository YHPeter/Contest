row,column = int(input()),int(input())
adj = {}
max_ad = row*column
import sys
sys.setrecursionlimit(100000)

def find(cur_index,visited):
    if cur_index==1:
        print('yes')
        sys.exit()
    for i in adj.get(cur_index,[]):
        if not i in visited:
            visited.append(i)
            find(i,visited)
            visited.pop()

for i in range(1,row+1):
    x = [0]+list(map(int,input().split()))
    for j in range(1,column+1):
        next,cross = x[j],i*j
        if cross<=max_ad and next<=max_ad:
            if adj.get(next,False):
                adj[next].add(cross)
            else: adj[next] = set([cross])
visited = [max_ad]
find(max_ad,visited)
print('no')
'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9
'''

'''
2
2
1 1
1 1
'''