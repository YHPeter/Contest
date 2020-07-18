# 1.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d>=85:
    if a+b>=180 or a+c>=180 or c+b>=180:
        print('Qualified')
    else: print('Not qualified')
else:
    print('Not qualified')

# 2.
# 若处于存活状态，用 * 表示，
# 若处于死亡状态，用 . 表示。
f = str(input()).split()
n,m = int(f[0]),int(f[1])
grid = []
for i in range(n):
    grid.append(['.']+list(input())+['.'])
grid.append(['.' for _ in range(n+2)])

def h(grid):
    point=[]
    nm = 0
    for i,iv in enumerate(grid):
        for j,jv in enumerate(iv):
            if jv == '*':
                # try:
                if i==0 and j==0: point=[grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]
                elif i==0: point = [grid[i][j-1],grid[i+1][j-1],grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]
                elif j==0: point = [grid[i-1][j],grid[i+1][j],grid[i-1][j+1],grid[i][j+1],grid[i+1][j+1]]
                else: point = [grid[i-1][j-1],grid[i][j-1],grid[i+1][j-1],grid[i-1][j],grid[i+1][j],grid[i-1][j+1],grid[i][j+1],grid[i+1][j+1]]
                # except: pass
                live = point.count('*')

                if live!=2 and live!=3:
                    print('Other')
                    return None
    print('Still life')
t = [['.','.','.','.'],['.','*','*','.'],['.','*','*','.'], ['.','.','.','.']]
h(grid)
            


# 3.
#  824
# -685 594 139 -48
# 37 -> 90506
# 367 -467 -937 -924 475 -542 -776 -516 -523 904 -884 388 52 926 -939 -804 -544 -843 841 927 683 638 980 -29 -623 32 281 -180 -282 -263 429 34 491 37 732 -20 879
n = int(input())
city = list(map(int,input().split(' ')))
d=0
for i in range(n-1):
    if city[i]<0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]-ab
    if city[i]>0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]+ab
print(d)


# 4. sample answer from https://iai.sh.cn/contribution/81
a=input()
if a.isnumeric()==True:
  print("Valid")
elif (a[0]=='-' or a[0]=='+') and a[1:].isnumeric()==True:
  print("Valid")
elif len(a)!=1 and a.count('.')==1 and a.find('.')!=-1:
  print("Valid")
else:
  print('Invalid')

# 4. my solution 90分
def sdf(n):
    try: 
        h = int(n)
        return True
    except:
        return False
        
n = str(input())
if n[-1]=='.': 
    n=n[0:-1]
    try: 
        h = int(n)
        print('Valid')
    except:
        print('Invalid')
elif n[0]=='.': 
    n=n[1:]
    try: 
        h = int(n)
        print('Valid')
    except:
        print('Invalid')
else:
    x=0
    if list(n).count('.')==1:
        m = n.split('.')
        for i in m:
            if sdf(i): x+=1
    if x==2: print('Valid')
    else: print('Invalid')

# 5. sample answer from https://iai.sh.cn/contribution/74
n = int(input())
a = [0]+list(map(int, input().split(' ')))
a.sort()
num=0
for i in range(1,n+1):
    num += (a[i] >= num)
print(num)

# 5. my solution 40分
n = int(input())
m = input().split(' ')
m = sorted(list(map(int, m)))

max_ = 0
u = []
for i in range(n):
    if i in m:
        u.append(i)
        m.remove(i)
    else: u.append('#')
if len(m)==0:
    for i in range(u.count('#')):
        u.remove('#')
    print(len(u))
elif len(u)>0:
    for i in m:
        for k in u[:i]:
            if k=='#':
                inde = u.index('#')
                u.pop(inde)
                u.insert(inde,'k')
    for i in range(u.count('#')):
        u.remove('#')
    print(len(u))