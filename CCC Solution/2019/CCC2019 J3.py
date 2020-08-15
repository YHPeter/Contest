for i in range(int(input())):
    j=list(input())
    list1=[]
    while True:
        if len(j)==0:
            break
        tage=j[0]
        num=0
        for i in range(80):
            try:
                if tage==str(j[i]):
                    num = num+1
                else:
                    break
            except:
                break
        list1.append([num,tage])
        for z in range(num):
            j.remove(tage)
    for k in list1:
        print(k[0],k[1],end=' ')
    print()