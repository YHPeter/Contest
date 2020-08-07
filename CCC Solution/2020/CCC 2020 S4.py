n = int(input())
num = {}
buglist = []

def f(x):
    x = int(x)
    if num.get(x,False):
        num[x] = 1
        buglist.append(x)
    else: num[x]+=1
    return x

li = list(map(f(),input().split()))

