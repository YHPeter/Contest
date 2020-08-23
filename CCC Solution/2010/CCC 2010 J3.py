'''Sample Input (with output shown in italics)
1 A 3
1 B 4
2 B
2 A
3 A B
2 A
5 A A
2 A
2 B
7
'''
dic = {'A':0,'B':0}
while 1:
    x = input().split()
    if x[0]=='1': dic[x[1]] = int(x[2])
    elif x[0]=='2': print(dic[x[1]])
    elif x[0]=='3': dic[x[1]]+=dic[x[2]]
    elif x[0]=='4': dic[x[1]]=dic[x[2]]*dic[x[1]]
    elif x[0]=='5': dic[x[1]]-=dic[x[2]]
    elif x[0]=='6': dic[x[1]]//=dic[x[2]]
    else: break
