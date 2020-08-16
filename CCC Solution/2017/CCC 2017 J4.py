
d = int(input())
a = d%720
ans = (d-a)//720*31
d = a
def issequence(z):
    res = set()
    k = 0
    for i in range(len(z)-1):
        res.add(int(z[i])-int(z[i+1]))
    return len(res)==1
time = [1,2,0,0]
for time in range(d+1):
    mins = time%60
    hours = ((time-mins)//60)%12
    if hours==0: hours='12'
    if mins<10: mins = '0'+str(mins)
    if issequence(str(hours)+str(mins)): ans+=1
print(ans)