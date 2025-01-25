# 代码随想录
## 动态规划
### [《代码随想录》动态规划：斐波那契数](https://notes.kamacoder.com/questions/502062)
#### 任务要求
#### 509. 斐波那契数


很简单的动规入门题，但简单题使用来掌握方法论的，还是要有动规五部曲来分析。

https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html   
视频：https://www.bilibili.com/video/BV1f5411K7mo

##### 重要知识点
- 简单题用来理解方法论



**简单题用来理解方法论**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i]: 第i个数的斐波那契数值是dp[i]
2. 递推公式 --> dp[i]=dp[i-1]+dp[i-2]
3. 初始化 --> dp[0],dp[1]=0,1
4. 遍历顺序 --> 从前到后
5. 打印dp数组 --> ~


**代码**
```Python 
class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        
        dp=[float('-inf')]*(n+1)
        dp[0],dp[1]=0,1
        if n>=2:
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
```
### [《代码随想录》动态规划：爬楼梯](https://notes.kamacoder.com/questions/502063)
#### 任务要求
#### 70. 爬楼梯


本题大家先自己想一想， 之后会发现，和 斐波那契数 有点关系。

https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html   
视频：https://www.bilibili.com/video/BV17h411h7UH

##### 重要知识点
- 解题思路



**解题思路**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i]: 爬到第i层台阶有dp[i]种方法
2. 递推公式 --> dp[i]=dp[i-1]+dp[i-2]
3. 初始化 --> dp[1],dp[2]=1,2
4. 遍历顺序 --> 从前到后
5. 打印dp数组 --> ~


本质上和“斐波那契数列”一样，只是递推公式需要自己推导出来，而且初始化的逻辑也不太一样。对于初始化而言，dp[0]是没有实际意义的，因为没有第0阶。所以需要初始化的是dp[1]和dp[2]。



**代码实现**
```Python 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
```
### [《代码随想录》动态规划：使用最小花费爬楼梯](https://notes.kamacoder.com/questions/502064)
#### 任务要求
#### 746. 使用最小花费爬楼梯


这道题目力扣改了题目描述了，现在的题目描述清晰很多，相当于明确说 第一步是不用花费的。 

更改题目描述之后，相当于是 文章中 「拓展」的解法 

https://programmercarl.com/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.html    
视频讲解：https://www.bilibili.com/video/BV16G411c7yZ

##### 重要知识点
- 简单题用来理解方法论



**简单题用来理解方法论**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i]: 爬到第i个台阶的最低花费为dp[i]
2. 递推公式 --> dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
3. 初始化 --> dp[0],dp[1]=0,0
4. 遍历顺序 --> 从前到后
5. 打印dp数组 --> ~

很重要的一个信息:楼梯顶部的高度为len(cost)+1


**代码**
```Python 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        dp[0],dp[1]=0,0
        
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]
```