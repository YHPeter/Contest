# YACS 2020.5 乙组 #1
# 负二进制
def baseNeg2(N):
    res = []
    # n = N
    while N:
        N, b = divmod(N, 2)
        N = -N
        res.append(str(b))
    return "".join(res[::-1]) or "0"
print((baseNeg2(int(input()))))