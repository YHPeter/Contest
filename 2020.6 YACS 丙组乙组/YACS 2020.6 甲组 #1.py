# YACS 2020.6 甲组 #1
'''
题目描述
一辆火车从1号站出发，依次路过2,3...,n−1，最后停在n号站。除最后一站外，每个站上都有一批乘客，其中i号站上有ci个人，他们的目的地是ti号站。火车的载客量有限，最多只能坐 ss 个人。当一批乘客下车后，座位空出来，可以继续接待下一批乘客。

假设小爱可以在每个站点选择让多少乘客上车，请问她应该怎么做才能让这辆火车接待最多的客人呢？

样例数据
输入:
5 100
4 80
3 70
5 10
5 1
输出:
111
说明:
1号站上车30人；
2号站上车70人；
3号站下车70人，上车10人；
4号站上车1人；
最后都在5号站下车。
'''
class Queue():
    def __init__(self,reverse):
        self.queue = []
        if reverse: self.reverse = True
        else: self.reverse = False
    def push(self,x):
        self.queue.insert(0,x)
        self.queue.sort(reverse = self.reverse, key = lambda x: x[1])

    def top(self):
        return self.queue[-1]

    def pop(self):
        return self.queue.pop()

    def empty(self):
        return self.queue == []
# sampel answer from https://iai.sh.cn/contribution/170 有bug待修复
st = [[0,0]for _ in range(10010)] 
n,limit = map(int,input().split(' '))
num = [0]*120021
ans,sum = 0,0
sk_s,sk_b = Queue(True),Queue(False)# 较近下车优先队列 # 较远下车优先队列 
for i in range(1,n+1):
    end,num[i] = map(int,input().split(' '))
    while (not sk_s.empty()) and sk_s.top()[1] <= i:
        u = sk_s.top()
        sum -= num[u[0]] # 更新车上总人数 
        ans += num[u[0]] # 更新答案 
        num[u[0]] = 0 # 更新该乘客群体在车上的数量
        sk_s.pop() # 该群体下车。
        # 让到站的乘客下车 
        if sum + num[i] <= limit: sum += num[i] # 乘客都可以上车，更新车上总人数  
        else:
            tmp = limit - sum # 目前空位数量 
            while not sk_b.empty():
                u = sk_b.top();
                if tmp == num[i] or sk_b.empty() or u[1] <= end: break # 无可踢下车的乘客 
                elif num[u[0]] == 0: sk_b.pop() # 该乘客群体都不在车上 
                else:
                    cnt = min(num[i] - tmp,num[u[0]]) # 计算踢下去的乘客数量 
                    tmp += cnt # 更新空位数量 
                    num[u[0]] -= cnt # 更新该乘客群体在车上的数量
            num[i] = tmp # 确定乘客上车数量 
            sum = limit # 更新车上总人数 
        sk_s.push({i,end}) # 新乘客上车 
        sk_b.push({i,end})
print(ans+sum)