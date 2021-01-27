n = int(input())
a,b,c, = n//3600,n%3600//60,n%3600%60
print(str(a)+':'+str(b)+':'+str(c))