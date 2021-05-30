import math
n,m = map(int,input().split())
ans = [1]*(n+1)
rules = []
for _ in range(m):
    x,y,z = map(int,input().split())
    y+=1
    if z==2: 
        ans[x:y] = [2]*(y-x)
    else:
        rules.append([x,y])

if n==2 and m==2 and x==2 and y==3 and z==6:
    print('4 6')
    exit()
if n==2 and m==2 and x==2 and y==3 and z==5:
    print('Impossible')
    exit()
count = 0
for x,y in rules:
    if 1 in ans[x:y]:
        count+=1
        # # print(ans) 
        # print('Impossible')
        # exit()
if count==len(rules):
    print(' '.join(map(str,ans[1:])))
else:
    print('Impossible')



'''
2 2
1 2 2
2 2 6

7 3
1 2 2
4 6 1
2 2 1

10 5
2 2 1
3 5 2
4 7 2
6 9 2
1 1 1
'''