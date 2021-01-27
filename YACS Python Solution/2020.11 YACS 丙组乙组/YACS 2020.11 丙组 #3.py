import calendar

year,date = map(int,input().split())


for month in range(1,13):
    num = calendar.monthrange(year,month)[1]
    for day in range(1,num+1):
        if day==13 and date==5: print(month)
        if date<7: date+=1
        else: date = 1
        