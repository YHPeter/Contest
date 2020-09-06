n = int(input())
for i in range(int(10000000**0.5),0,-1):
    if i<=n and n%(i**2)==0: 
        print(i**2)
        exit()