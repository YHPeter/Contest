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
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1),1):
            if n%i == 0:
                return False
            else:
                return True

def main():
    t=0
    s,e = map(int, sys.stdin.readline().split())
    for r in range(s,e+1):
        if isPrime(r) and isPrime(int(r%10)):
            print(r)
            t += 1
        else: pass
    if t==0:
        print('None')

if __name__ == "__main__":
    main()

# 3. sample answer from https:#iai.sh.cn/contribution/21
import sys
a,b = map(int, sys.stdin.readline().split())
def prime(n):
	if n == 2:
		return True
	elif n == 1 or n%2 == 0:
		return False
	else: pass
	
	for j in range(2,int(pow(n,0.5))+2):
		if n%j == 0:
			return False
	else:
		return True
count = 0
for i in range(a,b+1):
	if prime(i) and prime(i%10):
		print(i)
		count += 1
if count == 0:
	print(None)

# 4.
i = int(input())
li = list(map(int,str(input()).split()))
from functools import reduce
n = reduce(lambda a,b:a*b,li)
for i in range(len(li)):
    print(int((n/int(li[i]))%10000))
i = int(input())
li = str(input()).split()

# 4. sample answer from https:#iai.sh.cn/contribution/41
n = int(input())
a = list(map(int,str(input()).split()))
l = [0]*1000100
r = [0]*1000100
l[0] = r[n + 1] = 1
for i in range(1,n): 
    l[i] = l[i - 1] * a[i] % 10000
for i in range(n,0,-1): 
    r[i] = r[i + 1] * a[i] % 10000
for i in range(1,n): 
    print(l[i - 1] * r[i + 1] % 10000)

# 5.
import sys
def ts(tq):
    tq = list(map(int,tq.split(':')))
    h,m = tq[0],tq[1]
    ts = h*60+m
    return ts
n = int(input())
inputs = sys.stdin.readlines()
result = []
for n,t in enumerate(inputs):
    t = t.strip().split()
    st,dt = ts(t[0]),ts(t[1])
    result.append([st,st+dt,n+1])
result.sort()
for x in result: print(x[2])

# 5. sample ansser from https://iai.sh.cn/contribution/33
n = int(input())
t = [[0,0,0] for _ in range(1005)]# 出发时间,路程时间,队伍编号
tmp = t[::]
'''
int depart;	//	出发时间 [0]
int arrival;//	路程时间 [1]
int x;		//	队伍编号 [2]
'''
for i in range(1,n):
    #输入出发时间，并转换为整数形式 
    hour,mintue = list(map(int,input().split(':')))
    t[i][0] = hour * 60 + mintue
    #输入路程时间，并转换为到达时间的整数形式
    t[i][1] = t[i][0] + hour * 60 + mintue
    #变量 i 的值就是队伍的编号
    t[i][2] = i

	#用选择排序 
for i in range(1,n):
    k = i
    for j in range(i+1,n+1):
        #首先挑选到达时间靠前的队伍 
        if t[j][1] < t[k][1]: k = j
        elif t[j][1] == t[k][1]:
            #在到达时间相同的情况下，挑选出发时间靠前的队伍
            if t[j][0] < t[k][0]: k = j
            elif t[j][0] == t[k][0]:
                #如果出发时间仍然相同，则编号较小的队伍排在前列 
                if t[j][2] < t[k][2]: k = j
    #交换 
    tmp = t[i]
    t[i] = t[k]
    t[k] = tmp

#输出排序后的队伍编号 
for i in range(1,n+1):
    print(t[i][2])