# 读取测试数据组数
T = int(input())
for _ in range(T):
    # 输入 n, m, w_2, w_3
    n, m, w2, w3 = map(int, input().split())
    
    if n >= m:
        print(0)
        continue
    
    ans = float('inf')
    
    # 枚举a的取值，使用32作为上限
    for a in range(32):
        pow2 = 1 << a  # 计算2^a
        if n * pow2 >= m:
            ans = min(ans, a * w2)
            break
        cur2 = n * pow2
        pow3 = 1
        # 枚举b的取值
        for b in range(32):
            if b > 0:
                pow3 *= 3  # 计算3^b
            if cur2 * pow3 >= m:
                cost = a * w2 + b * w3
                ans = min(ans, cost)
                break  # 增加b只会增加花费
    print(ans)
