# 丙组 2020年3月
# 1.
n = int(input())
m = n%5
if n%5 == 4 or n%5 == 0:
    print('Lying')
else:
	print('Fishing')


# 2.
n = list(str(input()))
n[0], n[3] = n[3], n[0]
n[2], n[1] = n[1], n[2]
r1 = 9-int(n[0])
r2 = 9-int(n[1])
r3 = 9-int(n[2])
r4 = 9-int(n[3])
number = str(r1)+str(r2)+str(r3)+str(r4)
print(number)

#3.
# num = int(input())
import sys
import math
def isPrime(n):
    if (n==1) or (n==2) or (n==3) or (n==5) or (n==7):
        return True

    if (n%2==0) or (n%3==0) or (n%5==0) or (n%7==0):
        # print('if n==1 or n%2==0 or n%3==0 or n%5==0 or n%7==0 or n<=0:')
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1),1):
            if n%i == 0:
                # print(n)
                return False
            else:
                return True

def main():
    t=0
    s,e = map(int, sys.stdin.readline().split())
    for r in range(s,e+1):
        if isPrime(r) and isPrime(int(r//10)):
            print(r)
            t += 1
        else: pass
    if t==0:
        print('None')

if __name__ == "__main__":
    main()


# 4.
i = int(input())
li = list(map(int,str(input()).split()))
#除法
from functools import reduce
n = reduce(lambda a,b:a*b,li)
for i in range(len(li)):
    print(int((n/int(li[i]))%10000))

# 5.
def ts(tq): #get time stamp
    tq = list(map(int,tq.split(':')))
    h,m = tq[0],tq[1]
    ts = h*60+m
    return ts
    pass

import sys
n = int(input())
inputs = sys.stdin.readlines()
result = []
for n,t in enumerate(inputs):
    t = t.strip().split()
    st,dt = ts(t[0]),ts(t[1])
    result.append([st,st+dt,n+1])
result.sort()
for x in result: print(x[2])
