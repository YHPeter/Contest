m,n = map(int,input().split())
course = {}
stand = {}
for i in range(m):
    c,v = input().split()
    stand[c] = int(v)
    course[c] = 0

for i in range(n):
    course[input()]+=1

p,q = 0,0
for i in course.keys():
    if course[i]*2<stand[i]:
        p+=1
        q+=course[i]
    if course[i]>=stand[i]:
        q+=(course[i]-stand[i])

print(p)
print(q)
