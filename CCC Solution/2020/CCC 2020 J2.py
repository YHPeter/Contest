P = int(input())
N = int(input())
R = int(input())

total = N
next = N
counter = 0
#print("total:", total)
while total <= P:
    counter += 1
    total += next * R
    next = next * R
    #print("total:", total)

print(counter)