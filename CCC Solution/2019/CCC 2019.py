def sample(s):
    w = 1
    x = 2
    y = 3
    z = 4
    for j in s:
        if j == 'V':
            w,x = x,w
            y,z = z,y
        if j == 'H':
            w,y = y,w
            z,x = x,z
    print(w,x)
    print(y,z)
sample(input())
#Q1
# sample('VHVHVVHVHHHVHVVVVHVHVHVVVVVVVVVVVVVVVVVVVVVVVVVHHHHHHHHHHHHHHHHHHHHHVHVHVHVHHVHVHVHVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVHH')



def prime(N):
    for i in range(2,N):
        if N%i == 0:
            return False
            break
    return True

def Q2(N):
    N = N[1:]
    for i in N:
        #print('i',i)
        for x in range(2,i+1):
            #print('x',x)
            if prime(x) == True:
                y = 2*i - x
                #print(x,y)
                if prime(y) == True:
                    print(x,y)
                    break
                    
#Q2([3,4,8,19,21])


#Q4
'''
F = [1,2,3,5,6,2]
length = len(F)
from itertools import *
def itself(rest_F, max_num):
    rest_F = list(rest_F)
    for i in range(1,3):
        if rest_F == []:
            return max_num
        else:
            a = rest_F[0:i]
            rest_F=rest_F[i+1::]
            
        for i in islice(count(),i):
                
            itself(rest_F,max_num+max(a))
            print(max_num)
#itself(F,0)


def split(loop,list1):
    for n in range(loop):
        list1 = list1.append(list1[n:n+1:])
        l = [i for i in range(15)]

    [l[i:i + 3] for i in range(0, len(l), 3)]


F = [2,3,4,5,6,7,3,4,5,1]
if len(F)%3 == 0:
    split_list = [F[i:i + 3] for i in range(0, len(F), 3)]
    n = 0
    for i in split_list:
        n = n + max(i)
    print(n)

elif len(F)%3 == 1:
    list_sum = []
    for k in enumerate(F):
        temp_F = F
        print(F)
        index = k[0]
        value = k[1]
        split_F = F[index:index+1]
        split_F_max = max(F[index:index+1])
        print(split_F_max)
        del temp_F[index:index+1]
        print(temp_F)
        split_list = [temp_F[i:i + 3] for i in range(0, len(temp_F), 3)]
        n = 0
        for i in split_list:
            n = n + max(i)
        list_sum.append(n+split_F_max)
    print(max(list_sum))
else:
    split(2,F)

'''






'''
2018
Q2
Sample Input 2
3
4 3 1
6 5 2
9 7 3
Output for Sample Input 2
1 2 3
3 5 7
4 6 9
'''
list1=[3,[4,3,1],[6,5,2],[9,7,3]]
n = int(list1[0])
ele = list1[1:]

for i in range(n):
    for j in range(n):
        print(ele[i][j],end="\t")
    print()

print()

def isCorrect(t,n):
    for i in range(n):
        n=0
        row_data = t[i]
        sort_list=sorted(row_data)
        if sort_list != list(row_data):
            n = n+1
        else:
            pass
        if n == 0:
            return True
        else:
            return False

for c in range(n):
    if isCorrect(ele,n):
        for i in range(n):
            for j in range(n):
                print(ele[i][j],end="\t")
            print()

        break
    else:
        ele = list(zip(*ele[::-1]))