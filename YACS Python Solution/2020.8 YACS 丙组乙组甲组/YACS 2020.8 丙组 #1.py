# YACS 2020.8 丙组 #1

def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

# 促销骰子

s = stdinput()

if len(s)==3 and s[2]==6:
    print(1000)
elif len(s)>=2 and s[1]==6:
    print(100)
elif len(s)>=1 and s[0]==6:
    print(10)
else: print(0)