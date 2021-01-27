# YACS 2020.7 丙组 #5
# 游戏闯关
'''
4 22
6 8 10 7 
7 11 9 9

return: 3

4 22
7 8 9 10
4 5 6 7

return: 4
'''

n,t = map(int,input().split(' '))
a = list(map(int,input().strip().split(' ')))
b = list(map(int,input().strip().split(' ')))
flaga,flagb = True,True
for i in range(1,n):
    if not flaga: pass
    elif a[i-1]<t: a[i] = a[i]+a[i-1]
    else:
        a = a[:i]
        flaga = False

    if not flagb: pass
    elif b[i-1]<t: b[i] = b[i]+b[i-1]
    else:
        b = b[:i]
        flagb = False

    if not flaga and not flagb: break

a.insert(0,0)
b.insert(0,0)
max_ = 0
for i in range(1,len(a)):
    if a[i]>t: continue
    for j in range(1,len(b)):
        if a[i]+b[j]<=t: 
            max_ = max(max_,i+j)
        else: break
print(max_)