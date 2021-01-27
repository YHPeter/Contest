# YACS 2020.7 丙组 #3
# 树根
x = int(input())

def f(x):
    if x<10:
        return x
    return f(sum(map(int,list(str(x)))))
print(f(x))