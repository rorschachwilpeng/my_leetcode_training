# 大厂真题
## 美团
### [2025年3月23日](https://codefun2000.com/p/P2792)
#### 任务要求
#### 美团-2025年4月05日-整数的最小花费
https://codefun2000.com/p/P2792

##### 重要知识点
- 解题思路


**解题思路**
解本题的思路在于连立下列两个等式：

`(2^a)*(3^b)*n>=m`

`cost=a*w_2 + b*w_3`

对于第一个等式，因为a和b的取值范围最多就到31。所以我们可以穷举a和b的组合。然后选择出能让公式1左边大于m的组合。将组合放入公式2中，找到cost最小的组合。



**代码实现**

```Python
T=int(input())

for _ in range(T):
    n,m,w2,w3=map(int,input().strip().split())

    cost=float('inf')
    #判断边界情况
    if n>=m:
        print(0)
        continue
    #枚举操作次数
    operation_list=[]
    for i in range(32):#
        for j in range(32):
            operation_list.append((i,j))
    #计算结果并更新最小花费
    for a,b in operation_list:
        if (2**a) * (3**b) * n>=m:
            cost=min(cost,a*w2+b*w3)
    #输出答案
    print(cost)

```
