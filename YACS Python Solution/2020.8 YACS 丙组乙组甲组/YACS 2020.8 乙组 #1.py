# YACS 2020.8 乙组 #1
'''
4
1 1
2 2
4 1
4 2

8
1 3
3 3
3 7
5 5
7 9
9 5
9 1
20 10
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n = int(input())
ans = 0
heights = {}
topx = set()
removex = set()
for i in range(n):
    x,y = stdinput()
    heights[x] = max(heights.get(x,0),y)
    topx.add(x)

print(heights,topx)

for x in heights.keys():
    if x in removex: continue
    y = heights.get(x)
    for ts in topx.difference(removex):
        if ts<x-y or ts>x+y or ts==x: continue
        ty = heights.get(ts)
        if (ts<x and ty<=(ts+y-x)) or (ts>x and ty<=(x+y-ts)):
            removex.add(ts)

print(len(topx.difference(removex)))

# 超时
# n = int(input())
# ans = n
# heights = {}
# for i in range(n):
#     x,y = stdinput()
#     heights[x] = max(heights.get(x,0),y)
# print(heights)
# key = list(heights.keys())
# for x in key:
#     y = heights.get(x,0)
#     for dy in range(1,y):
#         if heights.get(x-dy,1000000001)<=y-dy:
#             heights.pop(x-dy)
#         if heights.get(x+dy,1000000001)<=y-dy:
#             heights.pop(x+dy)
# print(len(heights.keys()))