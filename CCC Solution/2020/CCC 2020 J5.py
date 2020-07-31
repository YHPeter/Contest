from math import sqrt
from math import floor
import sys
width = int(input())
length = int(input())

board = []
values = {}
for x in range(width):
    temp = input().split()
    board.append(temp)
    for y in range(len(temp)):
        #print(temp[y])
        if temp[y] not in values:
            values[temp[y]] = [[x,y]]
        else:
            values[temp[y]].append([x,y])

#print(values)
#print(board)
start = board[0][0]
end = width * length

visited = set()

def possibleJumps(product):
    output = []
    for i in range(1, int(floor(sqrt(product)) + 1)):
        temp = product / i
        if int(temp) == temp:
            #print(visited)
            if tuple([int(temp), i]) not in visited:
                output.append([int(temp), i])
                visited.add(tuple([int(temp), i])) #####rember
            if tuple([i, int(temp)]) not in visited:
                output.append([i, int(temp)])
                visited.add(tuple([i, int(temp)])) #####rember

    return(output)

#print(possibleJumps(100))

def recurse(positionnum):
    global end
    global board
    if positionnum == end or positionnum == str(end):
        print("yes")
        sys.exit()
    #print(positionnum)
    else:
        next = possibleJumps(int(positionnum))
        for i in next:
            if len(board) > i[0]-1 and len(board[0]) > i[1]-1: 
                #print(i)
                #print(board[i[0]-1][i[1]-1])
                recurse(board[i[0]-1][i[1]-1])
recurse(int(start))
print("no")