import sys

# 一次性读取输入数据
# data = sys.stdin.read().strip().split()
# n = int(data[0])
# a = list(map(int, data[1:]))


n=int(input())
a=list(map(int,input().strip().split()))

# 1) 计算前缀和 s[0..n]，s[0] = 0, s[i] = a1 + ... + a_i
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

# 2) 不使用反转技能时，在过程中出现的 |s[i]| 的最大值
ans = 0
for i in range(n + 1):
    ans = max(ans, abs(s[i]))

# 3) 计算后缀最大值 Mplus[i] = max(s[i..n])
#           后缀最小值 Mminus[i] = min(s[i..n])
Mplus = [0] * (n + 1)
Mminus = [0] * (n + 1)
Mplus[n] = s[n]
Mminus[n] = s[n]
for i in range(n - 1, -1, -1):
    Mplus[i] = max(Mplus[i + 1], s[i])
    Mminus[i] = min(Mminus[i + 1], s[i])

# 4) 枚举反转点 i (包含 i=0 和 i=n)
#    在第 i 步(用完第 i 个门)反转后，后续位置变为 s[j] - 2*s[i] (j >= i)
#    比较 Mplus[i] - 2*s[i] 和 Mminus[i] - 2*s[i] 的绝对值
for i in range(n + 1):
    val1 = abs(Mplus[i] - 2 * s[i])
    val2 = abs(Mminus[i] - 2 * s[i])
    ans = max(ans, val1, val2)

print(ans)

