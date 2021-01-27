s = input()
ans = 0
for i in s:
    if i in 'adgjmptw ': ans+=1
    elif i in 'behknqux': ans+=2
    elif i in 'cfilorvy': ans+=3
    elif i in 'sz': ans+=4
print(ans)