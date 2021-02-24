import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
dp = [0] * n
c = 0
last = {b[-1]: n - 1}
if b[-1] == b[0]: # 如果Josh和coach选一样的Burger，不受影响，100%概率返回
    print("{:.8f}".format(1))
else:
    for i in range(n - 2, -1, -1):
        if b[i] == b[0]: # 如果这个人和coach选一样的Burger，不受影响，100%
            dp[i] = 1
        elif b[i] in last: # 如果这个人士这个种类的最后一个人，且和coach种类不一样，概率等于同款汉堡的最后一个人的选择概率
            dp[i] = dp[last[b[i]]]
        else:
            dp[i] = (1 + c) / (n - i) # 这款汉堡（不是coach选的）的最后一个人，概率就等于？？？？
        
        c += dp[i]

        if b[i] not in last: # 获取每个种类最后一个汉堡的位置
            last[b[i]] = i

    print("{:.8f}".format(c / n))
