def output(x):
    for i in x:
        print(' '.join(list(map(str,map(int,i)))))
    exit()

def rotate(x):
    return list(map(list,zip(*x)))[::-1]

def newgrid(a,k1,k2,k3,k4,rtime):
    new = [[a,a+k1,a+2*k1],[a+k4,a+k2+k4,a+2*k2+k4],[a+2*k4,a+2*k4+k3,a+2*k4+k3*2]]
    for _ in range(4-rtime):
        new = rotate(new)
    return new

grid = [input().split() for _ in range(3)]
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'X':
            grid[i][j] = int(grid[i][j])

for rtimes in range(4):
    
    for _  in range(2):
        for i in range(3):
            if grid[i][0]!='X' and grid[i][2]!='X': grid[i][1] = (grid[i][0]+grid[i][2])//2
            if grid[i][0]!='X' and grid[i][1]!='X': grid[i][2] = 2*grid[i][1]-grid[i][0]
            if grid[i][1]!='X' and grid[i][2]!='X': grid[i][0] = 2*grid[i][1]-grid[i][2]
            if grid[0][i]!='X' and grid[2][i]!='X': grid[1][i] = (grid[0][i]+grid[2][i])//2
            if grid[0][i]!='X' and grid[1][i]!='X': grid[2][i] = 2*grid[1][i]-grid[0][i]
            if grid[1][i]!='X' and grid[2][i]!='X': grid[0][i] = 2*grid[1][i]-grid[2][i]
        
    unknown,known = [],[]
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'X': unknown.append([i,j])
            else: known.append([i,j])

    numunknown = len(unknown)

    if numunknown==9: output([[0]*3]*3)

    elif numunknown==8: 
        cur = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j]!='X': cur = grid[i][j]
        output([[cur]*3]*3)
    
    elif numunknown==7:
        x,y = [grid[a][b] for a,b in known]
        if known==[[0,0],[2,2]]: output(newgrid(x,0,0,0,(y-x)/2,rtimes))
        elif known==[[0,0],[2,1]]: output(newgrid(x,y-x,y-x,y-x,0,rtimes))
        elif known==[[0,0],[1,1]]: output(newgrid(x,0,0,0,y-x,rtimes))
        elif known==[[0,0],[1,2]]: output(newgrid(x,0,0,0,y-x,rtimes))

    elif numunknown==6:
        x,y,z = [grid[a][b] for a,b in known]
        if known==[[0,0],[1,1],[2,2]]: output(newgrid(x,0,((x+z)/2-y),(z-2*y+x),(2*y-x-(x+z)/2),rtimes))
        elif known==[[0,0],[1,2],[2,1]] and not (x+y+z)%2: output(newgrid(x,0,y-(z+x)/2,2*y-x-z,z-y,rtimes))
        elif known==[[0,0],[1,2],[2,1]] and (x+y+z)%2: output(newgrid(x,(2*y-1-x)/2,(y-(2*z-1+x)/2)/2,1-z,(2*z-1-x)/2,rtimes))
        elif known==[[0,0],[1,0],[2,0]]: output(newgrid(x,0,0,0,y-x,rtimes))
        elif known==[[0,1],[1,1],[2,1]]: output(newgrid(x,0,0,0,y-x,rtimes))
        
    elif numunknown==4:
        v,w,x,y,z = [grid[a][b] for a,b in known]
        if unknown==[[0,0],[0,2],[2,0],[2,2]]: output(newgrid(v,0,y-x,z-2*w+v,w-v,rtimes))
        elif unknown==[[1,1],[1,2],[2,1],[2,2]]: output(newgrid(v,x-w,x-w,x-w,z-y,rtimes))
        elif known==[[0,0],[1,0],[1,1],[1,2],[2,0]]: output(newgrid(v,0,y-x,2*x-v-z,w-v,rtimes))

    elif numunknown==0: output(grid)
    
    grid = rotate(grid)