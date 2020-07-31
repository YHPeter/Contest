
# Q2
list1=[]
for i in range(3):
    j = list(input())
    list1.append(j)
n=int(list1[0][0])
j1 = list1[1]
j2 = list1[2]
#print(j1,j2)
m=0
for i in range(n):
    if j1[i] == "C" and j2[i] == "C":
        m = m+1
    else:
        pass
print(m)