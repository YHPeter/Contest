n = int(input())
fridens = []

for _ in range(n):
    fridens.append(list(map(int,input().split())))
ans = 9999999999999999
def check(point):
    time = 0
    for p,w,d in fridens:
        if abs(point-p)>=d:
            time+=(abs(point-p)-d)*w
    return time
for i in range(max([x[0] for x in fridens])+1):
    ans = min(ans,check(i))
    # print(check(i),i)
print(ans)
exit()
ll,rr = 0, max([x[0] for x in fridens])
llcheck = check(ll)
rrcheck = check(rr)

if rr==0: print(ll)

while ll<rr:
    mid = (ll+rr)//2
    midcheck = check(mid)
    
    if llcheck<midcheck:
        rr = mid
        rrcheck = midcheck
    if rrcheck<midcheck:
        ll = mid
        llcheck = midcheck
    else:
        print(midcheck)
        