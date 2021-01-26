n = int(input())
card = list(map(int,input().split()))

type = [0,0,0]

for i in card:
    type[i%3]+=1

print(type[0]//2+min(type[1],type[2]))