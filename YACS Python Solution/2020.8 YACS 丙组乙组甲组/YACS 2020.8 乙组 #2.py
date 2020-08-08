# YACS 2020.8 乙组 #2
'''
3
200 120
50 40
20 10
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

ans = 0

def f(o,i,cho,ans):
    if len(cho)==1:
        ans+=1
        return ans
    incho = sorted(cho,key = (lambda x: x[1]))
    for k in range(len(cho),-1,-1):
        if incho[k][0]<=i:
            ans+=1
            o,i = incho[k][0],incho[k][1]
            break
        else: incho.pop()
    f(o,i,cho,ans)
