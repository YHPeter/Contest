# YACS 2020.5 丙组 #2
x = int(input())

def f(x):
    if x<10:
        return x
    return f(sum(map(int,list(str(x)))))
print(f(x))
