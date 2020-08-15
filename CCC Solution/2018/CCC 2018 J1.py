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