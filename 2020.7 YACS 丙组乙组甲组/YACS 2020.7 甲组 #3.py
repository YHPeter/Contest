# YACS 2020.7 甲组 #3
'''
类回文串
内存限制: 256 Mb时间限制: 1000 ms
题目背景
回文串是指倒置后保持不变的字符串。类回文串是指将字符串连续出现的字符合并后，具有回文串性值的字符串。例如BBBBASSAAAB 是类回文串，因为连续的同种字符合并后，它变成了 BASAB，是一个回文串。

题目描述
给定一个字符串 s，请找出一个最长的子串，满足类回文串的性值，输出它的长度。

输入格式
单个字符串：表示一个由英文字母组成的字符串 s。

输出格式
单个整数：表示输入的最长类回文子串长度。

样例数据
输入:
SSBBBBASSAAABRR
输出:
11
说明:
最长类回文子串为 BBBBASSAAAB
'''



s = '#'+input()
count = 0
new_s = ''
new_s_list = []
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        new_s+=s[i]
        new_s_list+=[count]
        count = 1
new_s_list+=[count]
new_s_list.pop(0)
s = new_s
n=len(s)
max_len=1
start=0
for i in range(1,n):
    even=s[i-max_len:i+1]
    odd=s[i-max_len-1:i+1]
    if i-max_len>=0 and even==even[::-1]:
        start=i-max_len
        max_len+=1
        continue
    if i-max_len-1>=0 and odd==odd[::-1]:
        start=i-max_len-1
        max_len+=2
        continue
print(sum(new_s_list[start: start + max_len]))