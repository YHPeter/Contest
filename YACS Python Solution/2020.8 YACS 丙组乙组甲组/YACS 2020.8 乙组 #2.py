# YACS 2020.8 乙组 #2
'''
3
200 120
50 40
40 10
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))
choose = []
for i in range(int(input())):
    choose.append(stdinput())

ans = 1

def f(inside,choose):
    global ans
    if len(choose)==0: return
    if len(choose)==1:
        ans+=(inside//choose[0][0])
        return
    while 1:
        insideli = [i[1] for i in choose]
        cur_outside,cur_inside = choose.pop(insideli.index(max(insideli)))
        # if inside//cur_outside==0: break
        ans+=(inside//cur_outside)
        for i in range(inside//cur_outside):
            f(cur_inside,choose)
        inside %= cur_outside
        if inside<min([i[0] for i in choose]): break
        

inside_ = sorted(choose,key = (lambda x: x[1]))
ind = inside_[-1][1]
inside_.pop()
f(ind,inside_)
print(ans)