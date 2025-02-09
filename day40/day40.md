# 代码随想录
## 动态规划
### [《代码随想录》动态规划：买卖股票的最佳时机](https://notes.kamacoder.com/questions/502087)
#### 任务要求
#### 121. 买卖股票的最佳时机

视频讲解：https://www.bilibili.com/video/BV1Xe4y1u77q 
https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html

##### 重要知识点

- 重要知识点
- 动规五部曲

**重要知识点**

从*动规五部曲*来分析，每个点都是重点：

1. dp数组的下标以及定义：如果我们要求给定股票第i天的价格，需要明确的点是对于每天的股票都会存在两个状态：买入/卖出。因此不如将dp数组定义设置为:  dp[i][0]:"第i天不持有股票的最大利润"，dp[i][1]:"第i天持有股票的最大利润"。
2. 递推公式：递推公式需要分类讨论，首先对于第i天持有股票的情况：如果第i天持有股票的话，可能是由两种情况推导而来：第一是：第i-1天就持有股票，第二种情况则是第i天买入股票。两者取最大利润 --> dp[i][1]=max(dp[i-1][1], -prices[i])。对于第i天不持有股票也是由两种情况推倒而来：第一是：第i-1天就不持有股票，第二种是第i天卖出股票。两者取最大利润 --> dp[i][0]
=max(dp[i-1][0], dp[i-1][1]+prices[i]) 

3. 初始化：dp[0][0]=0, dp[0][1]=-prices[0]
4. 遍历顺序：从左到右

**代码**
```Python 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp数组下标以及定义
            #dp[i][0]:第i天不持有股票能够获取的最大利润
            #dp[i][1]:第i天持有股票能够获取的最大利润
        size=len(prices)
        if size==0:
            return 0
        
        dp=[[0]*2 for _ in range(size)]
        #初始化
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,size):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])#不持有的-->i-1天就不持有的 / 第i天卖出的
            dp[i][1]=max(dp[i-1][1], -prices[i])#持有的-->i-1天就持有的/第i天买入的
        
        return dp[-1][0]
```
### [《代码随想录》动态规划：买卖股票的最佳时机II（动态规划）](https://notes.kamacoder.com/questions/502088)
#### 任务要求
#### 122.买卖股票的最佳时机II

视频讲解：https://www.bilibili.com/video/BV1D24y1Q7Ls 
https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

##### 重要知识点

- 解题思路

**解题思路**

和上一题思路差不多，唯一的区别是在于本题可以多次买入和卖出，而上一题只能买入一次，卖出一次。所以区别在于递推公式中，对于买入情况需要调整一下。


**代码**
```Python 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #本题和上题的区别在于：本题支持多次买卖
        #dp数组下标以及含义:
            #dp[i][0]:第i天不持有股票的最大利润
            #dp[i][1]:第i天持有股票的最大利润
        size=len(prices)
        if size==0:
            return 0
        
        dp=[[0]*2 for _ in range(size)]
        #初始化
        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1, size):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]-prices[i])#区别在这儿
        
        return dp[-1][0]
```
### [《代码随想录》动态规划：买卖股票的最佳时机III](https://notes.kamacoder.com/questions/502089)
#### 任务要求
#### 123.买卖股票的最佳时机III


这道题一下子就难度上来了，关键在于至多买卖两次，这意味着可以买卖一次，可以买卖两次，也可以不买卖。
视频讲解：https://www.bilibili.com/video/BV1WG411K7AR 
https://programmercarl.com/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题的主要难点在于：递推公式的构建以及初始化上。


**动规五部曲**
1. dp数组下标以及含义：dp[i][0]/dp[i][1]/dp[i][2]/dp[i][3]/dp[i][4] --> 无操作 / 第一次买入 / 第一次卖出 / 第二次买入 / 第二次卖出；
2. 递推公式
```Python
	dp[i][0]=0
	dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
	dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prcies[i])
	dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
	dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
```
3. 初始化: 见代码
4. 遍历顺序：从小到大


**代码**
```Python 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size=len(prices)
        dp=[[0]*5 for _ in range(size)]

        #初始化
        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[0][2]=0
        dp[0][3]=-prices[0]
        dp[0][4]=0

        #遍历顺序
        for i in range(1,size):
            dp[i][0]=0
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        
        return dp[-1][4]
```
