# YACS 2020.8 丙组 #2

def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

a,b,c = stdinput()
rb,rc = a,a
ans = a
def exchange(rb,rc,ans):
    if rb<b and rc<c:
        return ans
    total = rb//b+rc//c
    ans+=total
    rb = rb%b + total
    rc = rc%c + total
    return exchange(rb,rc,ans)
print(exchange(rb,rc,ans))