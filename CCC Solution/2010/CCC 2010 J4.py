'''
7 3 4 6 4 5 7 5
3 1 3 5
3 1 4 5
4 3 4 6 7
0

'''
while 1:
    x = list(map(int,input().split()))
    if x==[0]: break
    for i in range(len(x)-1):
        x[i] = x[i+1]-x[i]
    x.pop()
    flag = False
    ans = 999999
    for l in range(1,len(x)):
        # newp = 0
        # count=0
        # tmp = x[1]
        # for ini in range(1,len(x),l):
        #     newp+=1
        #     if tmp==x[ini]: count+=1
        # if count==newp:
        #     print(l)
        #     flag = True
        #     break
        tmp = []
        for i in range(1,len(x),l):
            if i+l>len(x): tmp.append(x[i:])
            else: tmp.append(x[i:i+l])
        pre = tmp[0]
        ans = True
        for j in range(1,len(tmp)):
            if tmp[j]!=pre[:len(tmp[j])]: ans = ans and False
        if ans:
            print(l)
            flag = True
            break

    if not flag:
        print(0)