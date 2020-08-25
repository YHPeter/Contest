x = []
for i in range(4):
    x.append(list(map(int,input().split())))
su = sum(x[0])
flag = True
for i in range(4):
    if su!=sum(x[i]): flag = False
    if su!=(x[0][i]+x[1][i]+x[3][i]+x[2][i]): flag = False
if flag: print('magic')
else: print('not magic')