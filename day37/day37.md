# 代码随想录
## 动态规划
### [《代码随想录》动态规划：零钱兑换II](https://notes.kamacoder.com/questions/502076)
#### 任务要求
#### 518. 零钱兑换 II

视频讲解：https://www.bilibili.com/video/BV1KM411k75j
https://programmercarl.com/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.html


##### 重要知识点

- 求装满背包有多少种方法
- 二维背包实现
- 一维背包实现

**求装满背包有多少种方法**

求装满背包有多少种方法的递推公式 --> dp[j]+=dp[j-num]

如果是一维背包的话，01背包和完全背包的递推公式是一样的。但是如果是二维背包的话，递推公式应该是：

dp[i][j]=max(dp[i-1][j], dp[i][j-num])

主要区别是在于“装物品i的情况”，物品中仍然包括物品i，因为每个物品有无数个。


**二维背包实现**

```Python 
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size=len(coins)
        dp=[[0]*(amount+1) for _ in range(size)]
        
        #初始化
        for j in range(0,amount+1):
            if j%coins[0]==0:dp[0][j]=1
            
        for i in range(0,size):
            dp[i][0]=1

        for i in range(1,size):#物品
            for j in range(amount+1):#背包
                if coins[i]>j:
                    dp[i][j]=dp[i-1][j]#不放物品i
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
                
                
        return dp[-1][-1]
```

**一维背包实现**

需要注意的是，初始化时候dp[0]代表有多少种方法能够装满容量为0的背包，这里不装物品也是一种方法，因此dp[0]初始化为1

```Python 
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)

        #初始化
        dp[0]=1

        for coin in coins:#物品
            for j in range(coin,amount+1):#背包
                dp[j]+=dp[j-coin]
        return dp[-1]
```
### [《代码随想录》动态规划：组合总和Ⅳ](https://notes.kamacoder.com/questions/502077)
#### 任务要求
#### 377. 组合总和 Ⅳ

视频讲解：https://www.bilibili.com/video/BV1V14y1n7B6 
https://programmercarl.com/0377.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%E2%85%A3.html


##### 重要知识点

- 排列和组合的区别
- 为什么？

**排列和组合的区别**

本题中求的是排列，关于怎么区分排列和组合，以及它们对应的代码实现：排列-->顺序有关系，组合-->顺序无关系

组合的代码实现：先遍历物品，再遍历背包

排列的代码实现：先遍历背包，再遍历物品


**为什么？**

为什么先遍历物品，再遍历背包就是组合呢？

*先遍历物品（硬币）*

	- 计算时，先确定「使用哪种硬币」，然后计算所有可能情况。
	- 这样保证了 *相同元素不会以不同顺序重复出现*。
	- **适用于组合问题**（即顺序不重要）。

为什么先遍历背包，再遍历物品就是组合呢？
*先遍历背包（目标金额）*

	- 计算时，先确定「当前金额」，然后考虑能用的硬币。
	- 这样会导致 **同样的数字可能以不同顺序出现**（因为前面计算的结果会影响后续）。
	- **适用于排列问题**（即顺序重要）。


**代码**
```Python 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        #初始化 
        dp[0]=1

        for j in range(0,target+1):
            for num in nums:
                if num<=j:
                    dp[j]+=dp[j-num]
        return dp[-1]
```
### [《代码随想录》动态规划：爬楼梯完全背包版本](https://notes.kamacoder.com/questions/502078)
#### 任务要求
#### 70. 爬楼梯 （进阶）


这道题目 爬楼梯之前我们做过，这次再用完全背包的思路来分析一遍 

https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E7%89%88%E6%9C%AC.html


##### 重要知识点

- 还是完全背包，还是求排列

**解题思路**

和前两题一样


**代码**
```Python 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        #初始化 
        dp[0]=1

        for j in range(0,target+1):
            for num in nums:
                if num<=j:
                    dp[j]+=dp[j-num]
        return dp[-1]
```

