# YACS 2020.5 甲组 #1
# 旋转减半数
# sample answer from https://iai.sh.cn/contribution/110
n = int(input())
import sys
s = [[0 for _ in range(2002)]  for _ in range(2002)]
adv = [0]*2002
for i in range(1,n):
    s[i][1] = i
j = 1
while 1:
    for i in range(1,n+1):
        s[i][j + 1] = 2 * s[i][j] + adv[i]
        adv[i] = s[i][j + 1] // n
        s[i][j + 1] %= n
        
        if adv[i]==0 and s[i][j+1] ==i:
            print(' '.join(map(str,s[i][j+1:1:-1])))
            sys.exit()
    j+=1
