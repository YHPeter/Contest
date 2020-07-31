
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

4
4 8 12 16
3 7 11 15
2 6 10 14
1 5 9 13
'''


# f=open("C:/Users/peter/Desktop/4.txt","r")
# list2=f.read()
# list2=list2.split("\n")#对行进行切片
# for i in range(len(list2)):#对列进行切片
#     list2[i]=list2[i].split()
# list2 = list(map(lambda x:map(int, x), list2))
t=[]
n = int(input())
for i in range(n):
    j = (input().replace(' ', ',')).split(',')
    t.append(j)
#list1=[3,[4,3,1],[6,5,2],[9,7,3]]
ele = t #list2
'''
for i in range(n):
    for j in range(n):
        print(ele[i][j],end="\t")
    print()

print()
'''
def isCorrect(t,n):
    for i in range(n):
        w=0
        row_data = t[i]
        sort_list=sorted(row_data)
        if sort_list != list(row_data):
            w = w+1
        else:
            pass
        if w == 0:
            max_item = max(max(row,default=0) for row in t)
            # print(max_item)
            if max_item in t[n-1]:
                nm = 0
                t_sum = []
                for j in range(n):
                    sumj=0
                    for sumi in t[j]:
                        sumj = sumj+int(sumi)
                    t_sum.append(sumj)
                if t_sum == sorted(t_sum):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

for c in range(4):
    if isCorrect(ele,n):
        # print(ele)
        for i in range(n):
            for j in range(n):
                print(ele[i][j],end="\t")
            print()
        break
    else:
        # print(ele)
        ele = list(zip(*ele[::-1]))