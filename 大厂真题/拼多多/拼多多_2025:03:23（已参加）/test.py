n = int(input())  # 输入同学人数
h = list(map(int, input().split()))  # 输入同学的身高列表

stack = []  # 用来存储身高索引的栈
total = 0  # 用来累加视线数量

# 从右往左遍历每个同学
for i in range(n - 1, -1, -1):
    # 移除栈中比当前同学矮的同学
    while stack and h[stack[-1]] < h[i]:
        stack.pop()
    
    # 如果栈不为空，栈顶的同学是第一个比当前同学高的同学
    if stack:
        cnt = stack[-1] - i  # 当前同学能看到的同学数量
    else:
        cnt = n - 1 - i  # 当前同学能看到所有在他右边的同学
    
    total += cnt  # 累加总的视线数量
    
    stack.append(i)  # 将当前同学的索引加入栈中

print(total)  # 输出最终结果
