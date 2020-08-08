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
ans = n
heights = {}
for i in range(n):
    x,y = stdinput()
    heights[x] = max(heights.get(x,0),y)
print(heights)
key = list(heights.keys())
for x in key:
    y = heights.get(x,0)
    for dy in range(1,y):
        if heights.get(x-dy,1000000001)<=y-dy:
            heights.pop(x-dy)
        if heights.get(x+dy,1000000001)<=y-dy:
            heights.pop(x+dy)
print(len(heights.keys()))