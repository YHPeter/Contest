# YACS 2020.5 丙组 #1
n = int(input())
ini = 10
for i in range(2,200):
    if i%7==0 or i%7==1:
        ini+=6
    else:
        ini-=1
    if ini==n:
        print(i-1)
        break