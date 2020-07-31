def sample(s):
    w = 1
    x = 2
    y = 3
    z = 4
    for j in s:
        if j == 'V':
            w,x = x,w
            y,z = z,y
        if j == 'H':
            w,y = y,w
            z,x = x,z
    print(w,x)
    print(y,z)
sample(input())