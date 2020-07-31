points = int(input())

board = []
x = []
y = []
for i in range(points):
    temp = input().split(",")
    x.append(int(temp[0]))
    y.append(int(temp[1]))

print(str(min(x) - 1) + "," + str(min(y) - 1))
print(str(max(x) + 1) + "," + str(max(y) + 1))
