'''
当子串长度小于等于3时，出现了两个相同字母那就是不随机的。
可以转化为两个相同的字母出现的位置差小于等于2就是不随机的。

时间复杂度：O(n) （只扫了一遍字符串）
空间复杂度：O(1) （只有一个countl字典储存字母位置）
'''

countl = {'q': -3, 'w': -3, 'e': -3, 'r': -3, 't': -3, 'y': -3, 'u': -3, 'i': -3, 'o': -3, 'p': -3, 'a': -3, 's': -3, 'd': -3, 'f': -3, 'g': -3, 'h': -3, 'j': -3, 'k': -3, 'l': -3, 'z': -3, 'x': -3, 'c': -3, 'v': -3, 'b': -3, 'n': -3, 'm': -3}
# print(countl)
s = input()
countl[s[0]]=0
for i in range(1,len(s)):
    if i - countl[s[i]]<=2:
        print('Not a random string')
        exit()
    countl[s[i]] = i
print('Random string')
