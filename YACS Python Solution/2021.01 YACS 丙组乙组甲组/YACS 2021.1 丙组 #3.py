a,k = map(int, input().split())
time = 0
page = 0
while 1:
    page+=1
    time+=str(page).count(str(a))
    if time>=k:
        print(page)
        break