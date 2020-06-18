# # YACS 2020.6乙组#4.py
n,m = map(int,input().split(' '))
np,mp = [],[]
tn,tm = 0,0
pren,prem = 0,0
ans = 0
lead,pre_lead =0,0
for i in range(n):
    time,speed = map(int,input().split(' '))
    tn+=time
    np += [pren+speed*f for f in range(1,time+1)]
    pren = np[-1]
for i in range(m):
    time,speed = map(int,input().split(' '))
    mp += [prem+speed*f for f in range(1,time+1)]
    prem = mp[-1]


for i in range(1,min(len(np),len(mp))):
    if np[i]>mp[i]:
        lead = 1
    elif np[i]<mp[i]:
        lead = 2
    elif np[i]==np[i]:
        pass
    if not lead == pre_lead:
        ans+=1
    pre_lead = lead
# print(np,mp)
print(ans-1)