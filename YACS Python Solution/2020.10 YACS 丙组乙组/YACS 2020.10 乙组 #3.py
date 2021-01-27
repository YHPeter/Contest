from typing import Counter

s,t = input(),input()
ans = 0
times = 0
dict,dics = Counter(t),Counter(s)
for i in dict.values():
    ans += i
    if i==max(dict.values()): times+=1
print(ans-max(dict.values())*times)

'''
标准输出: 45
dvotanaacwxjljqkmxhsmsyzagaivuikxjywaaiajuombpbyhahjyqioey
zoujnuwqxmytowpqpmlurxqkwpjfmzbqsaeqjexclusyktjizuzlvxunfy

标准输出: 13
hohgoflhfotxzulgu
vhvbszpwmywvcfvug

标准输出: 19
mschsbeaeepaqzirydlymco
hpamysqlkxvzxvgywtyeerw

标准输出: 24
hnbrzaoqlhtjvsehatwfwkbdjwemjx
uelstdnctifkhcnwiwzzbvohsqhgjy
'''