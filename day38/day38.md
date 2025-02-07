# 代码随想录
## 动态规划
### [《代码随想录》动态规划：零钱兑换](https://notes.kamacoder.com/questions/502079)
#### 任务要求
#### 279.完全平方数

本题 和 322. 零钱兑换 基本是一样的，大家先自己尝试做一做 
视频讲解：https://www.bilibili.com/video/BV12P411T7Br 
https://programmercarl.com/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

首先需要明确这道题是一道完全背包组合问题，因此我们可以确定遍历顺序和背包维度的遍历先后顺序。于此同时因为求的是*最少硬币个数*，所以我们需要在初始化时候将初始值定义为无穷大，同时确保递推公式中是求最小值。


**动规五部曲**

- 完全背包问题-->求组合
- dp数组下标以及定义:dp[j]:凑成容量为j的背包最少的硬币个数为dp[j]
- 递推公式：dp[j]=min(dp[j],dp[j-coin]+1)
- 初始化：初始化为float('inf')
- 遍历顺序：先物品，后背包

**代码**
```Python 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        
        for coin in coins:#物品
            for j in range(coin,amount+1):#背包--组合问题
                dp[j]=min(dp[j],dp[j-coin]+1)
        
        if dp[-1]==float('inf'):
            return -1
        else:
            return dp[-1]
```
### [《代码随想录》动态规划：完全平方数](https://notes.kamacoder.com/questions/502080)
#### 任务要求
#### 279.完全平方数

本题 和 322. 零钱兑换 基本是一样的，大家先自己尝试做一做 
视频讲解：https://www.bilibili.com/video/BV12P411T7Br 
https://programmercarl.com/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.html

##### 重要知识点

- 解题思路

**解题思路**

将题目抽象化一下，其实和“零钱兑换”非常相似。但这道题里面比较tricky的地方在于完全平方数的判断。刚开始我的思路是通过写一个函数来判断完全平方数，只将完全平方数放入背包。但是其实并不需要，可以用同样的思路但是更简洁的方法来实现 -- 通过限定物品的取值范围，确保最多只取到最大值开方后的值。



**代码**
```Python 
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for num in range(1,int(n**0.5)+1):#物品
            sqrtVal=num*num#只取完全平方数
            for j in range(sqrtVal,n+1):#背包
                dp[j]=min(dp[j], dp[j-sqrtVal]+1)
        
        return dp[-1]
```
### [《代码随想录》动态规划：单词拆分](https://notes.kamacoder.com/questions/502081)
#### 任务要求
#### 139.单词拆分

视频讲解：https://www.bilibili.com/video/BV1pd4y147Rh 
https://programmercarl.com/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题首先需要将问题抽象化成背包问题，其次很重要的一点是需要明确这道题中我们需要在乎顺序，因此这是一个完全背包+排列问题


**动规五部曲**

- 完全背包问题-->求排列
- dp数组下标以及定义:dp[j]:容量为j的背包是否能够装满
- 递推公式：
```
if dp[j-len(word)] and s[j-len(word):j]==word:
		dp[j] = True
		break
```
- 初始化：初始化为False
- 遍历顺序：先背包，再物品

**代码**
```Python 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size=len(s)
        dp=[False]*(size+1)
        dp[0]=True

        for j in range(size+1):
            for word in wordDict:            
                if len(word)<=j:
                    if dp[j-len(word)] and s[j-len(word):j]==word:
                        dp[j]=True
                        break

        return dp[-1]
```
