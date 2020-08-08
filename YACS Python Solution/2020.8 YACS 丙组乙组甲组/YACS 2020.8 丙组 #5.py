# YACS 2020.8 丙组 #5
'''
1
 /\
/__\
2
   /\
  /__\
 /\  /\
/__\/__\
3
       /\
      /__\
     /\  /\
    /__\/__\
   /\      /\
  /__\    /__\
 /\  /\  /\  /\
/__\/__\/__\/__\
4
               /\
              /__\
             /\  /\
            /__\/__\
           /\      /\
          /__\    /__\
         /\  /\  /\  /\
        /__\/__\/__\/__\
       /\              /\
      /__\            /__\
     /\  /\          /\  /\
    /__\/__\        /__\/__\
   /\      /\      /\      /\
  /__\    /__\    /__\    /__\
 /\  /\  /\  /\  /\  /\  /\  /\
/__\/__\/__\/__\/__\/__\/__\/__\
5
                               /\
                              /__\
                             /\  /\
                            /__\/__\
                           /\      /\
                          /__\    /__\
                         /\  /\  /\  /\
                        /__\/__\/__\/__\
                       /\              /\
                      /__\            /__\
                     /\  /\          /\  /\
                    /__\/__\        /__\/__\
                   /\      /\      /\      /\
                  /__\    /__\    /__\    /__\
                 /\  /\  /\  /\  /\  /\  /\  /\
                /__\/__\/__\/__\/__\/__\/__\/__\
               /\                              /\
              /__\                            /__\
             /\  /\                          /\  /\
            /__\/__\                        /__\/__\
           /\      /\                      /\      /\
          /__\    /__\                    /__\    /__\
         /\  /\  /\  /\                  /\  /\  /\  /\
        /__\/__\/__\/__\                /__\/__\/__\/__\
       /\              /\              /\              /\
      /__\            /__\            /__\            /__\
     /\  /\          /\  /\          /\  /\          /\  /\
    /__\/__\        /__\/__\        /__\/__\        /__\/__\
   /\      /\      /\      /\      /\      /\      /\      /\
  /__\    /__\    /__\    /__\    /__\    /__\    /__\    /__\
 /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\

1
 /\
2
   /\
 /\  /\
3

       /\
     /\  /\
   /\      /\
 /\  /\  /\  /\
4
               /\
             /\  /\
           /\      /\
         /\  /\  /\  /\
       /\              /\
     /\  /\          /\  /\
   /\      /\      /\      /\
 /\  /\  /\  /\  /\  /\  /\  /\
'''
n = int(input())
if n==1:
    print(' '+pattern1)
    print(pattern2)
    exit()

pattern1 = "/\\"
pattern2 = "/__\\"
c = [[0]]

for j in range(2,n+1):
    c.append([2**j])
    l = len(c)
    for i in range(1,l):
        if c[i]==2**j or (2**j-i*4)==0: break
        try:
            c.append(c[i]+[2**j-i*4]+c[i])
        except:
            c.append([c[i]]+[2**j-i*4]+[c[i]])
        
cur = 1
for i in range(0,2**n,2):
    print(' '*(2**n-i-1)+pattern1,end = '')
    for x in c[i//2]:
        if x==0: continue
        print(' '*(x-2)+pattern1,end = '')
        
    print('\n'+' '*(2**n-i-2)+pattern2,end = '')
    for x in c[i//2]:
        if x==0: continue
        print(' '*(x-4)+pattern2,end = '')
    print()
