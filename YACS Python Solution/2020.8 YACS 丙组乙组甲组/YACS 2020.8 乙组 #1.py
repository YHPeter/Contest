# YACS 2020.8 乙组 #1
'''
4
1 1
2 2
4 1
4 2
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n = int(input())
ans = n
c = []
max_height = [-1]*(n+1)
for i in range(n):
    x,y = stdinput()
    max_height[x] = max(max_height[x],y)
    c.append([x,y])
c.sort(key = (lambda x:x[0]))
for i in range(n):
    if 