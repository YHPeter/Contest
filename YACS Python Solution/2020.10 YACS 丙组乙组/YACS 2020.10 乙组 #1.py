table = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]

n = int(input())
ans = 0
def isvalid(x):
    f = 2
    search = x // 2
    i = 2
    while(i <= search):
        if x % i == 0:
            if x // i > i: f += 2
            elif x // i == i: f+=1
            else: break
        i+=1
    return x if f in table else 0
for i in range(2,n+1):
    ans+=isvalid(i)
print(ans)