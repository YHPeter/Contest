# YACS 2020.8 乙组 #2
'''
3
200 120
50 40
20 10

输出: 369
15
64 30
55 52
6 5
2 1
62 22
6 5
596 553
3 2
46 19
6 5
2 1
6 5
2 1
2 1
40 33

 准输出: 202 你的输出: ['16\n', '2 1\n', '2 1\n', '2 1\n', '2 1\n', '2 1\n', '10 8\n', '8 7\n', '520 154\n', '6 5\n', '6 5\n', '2 1\n', '5 4\n', '6 5\n', '559 302\n', '6 5\n', '2 1\n']
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))
choose = []
for i in range(int(input())):
    x = stdinput()
    if not x in choose:
        choose.append(x)

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
        if inside<cur_outside: continue
        ans+=(inside//cur_outside)
        for i in range(inside//cur_outside):
            f(cur_inside,choose)
        inside %= cur_outside
        if not choose or inside<min([i[0] for i in choose]): break
        
print(choose)
inside_ = sorted(choose,key = (lambda x: x[1]))
ind = inside_[-1][1]
inside_.pop()
f(ind,inside_)
print(ans)