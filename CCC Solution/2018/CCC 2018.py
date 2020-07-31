## 
##  Python 3.x version of 2012 CCC Senior Problem 1 Solution
##  
##  Using python version 3.4.0 interpreter 
## 

# Q1 15/15

list1=[]
for i in range(4):
    j = input()
    list1.append(j)

n = 0
n1 = int(list1[0])
n2 = int(list1[1])
n3 = int(list1[2])
n4 = int(list1[3])
if  n1 == 8 or n1 ==9:
    if  n4 == 8 or n4 == 9:
        if  n2 == n3:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")


# Q2 9/15
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


# Q3
list1=[]
for i in range(3):
    j = list(input())
    list1.append(j)
d1 = list1[0]
d2 = list1[1]
d3 = list1[2]
d4 = list1[3]

print(0,d1,d1+d2,d1+d2+d3,d1+d2+d3+d4)
print(d1,0,d2,d2+d3,d2+d3+d4)
print(d1+d2,d2,0,d3,d3+d4)
print(d1+d2+d3,d2+d3,d3,0,d4)
print(d1+d2+d3+d4,d2+d3+d4,d3+d4,d4,0)