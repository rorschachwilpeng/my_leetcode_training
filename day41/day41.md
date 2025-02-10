# 代码随想录
## 动态规划
### [《代码随想录》动态规划：买卖股票的最佳时机IV](https://notes.kamacoder.com/questions/502090)
#### 任务要求
#### 188.买卖股票的最佳时机IV

本题是123.买卖股票的最佳时机III 的进阶版  
视频讲解：https://www.bilibili.com/video/BV16M411U7XJ 
https://programmercarl.com/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题是“买卖股票的最佳时机III”的升级版。首先我们需要找到规律，即能够买卖k次的话代表着奇数-->买入，偶数-->卖出。然后就和上一题的思路一样一样的了。


**动规五部曲**

- dp数组下标以及定义:
```Python
        #dp数组下标以及定义:
            #if j%2==0: --> 不持有
                #dp[i][j]:第i天不持有股票能收获的最大利润
            #elif j%2==1: --> 买入
                #dp[i][j]:第i天持有股票能收获的最大利润
```
- 递推公式：
```Python
            if j%2==0:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
            elif j%2==1:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
```
- 初始化：详见代码实现
- 遍历顺序：从小到大

**代码**
```Python 
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #可以买卖k次的话，首先需要判断
        #从1～2k+1，奇数-->买入，偶数-->卖出
        
        size=len(prices)
        dp=[[0]*(2*k+1) for _ in range(size)]
        
        #初始化
        for j in range(1,2*k+1):#跳过第一个状态-->无操作
            if j%2==1:
                dp[0][j]=-prices[0]
            else:
                dp[0][j]=0#其实可以不用，留着为了方便理解
        

        #遍历顺序-->从小到大
        for i in range(1,size):
            for j in range(1,2*k+1):#好像右边界需要+1
                if j%2==0:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
                elif j%2==1:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
        
        return dp[-1][-1]
```
### [《代码随想录》动态规划：最佳买卖股票时机含冷冻期](https://notes.kamacoder.com/questions/502091)
#### 任务要求
#### 714.买卖股票的最佳时机含手续费

相对122.买卖股票的最佳时机II ，本题只需要在计算卖出操作的时候减去手续费就可以了，代码几乎是一样的，可以尝试自己做一做。
视频讲解：https://www.bilibili.com/video/BV1z44y1Z7UR 
https://programmercarl.com/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

我刚开始做本题的时候思路是分析出了三种状态：“持有状态”，“冷冻期”，“不持有状态”。这个分析思路没错，但是如果表示冷冻期需要有一天不能卖出的状态难住我了。


代码随想录中的题解将状态分解成了四种：“买入状态”，“今天卖出”，“冷冻期”，“卖出状态”。

他们之间的相互转换关系：


![截屏2025-02-10 10.36.15.png](http://cdn.notes.kamacoder.com/a5cb6a75-2899-4380-b279-5cd23fb257c6.png) 


**动规五部曲**

- dp数组下标以及定义: ～
- 递推公式：
	1. 状态一（持有股票状态）：一直持有 / 刚刚从“卖出状态”买入 / 刚刚从“冷冻状态”买入
	2. 状态二（保持卖出股票状态）：之前就是卖出状态 / 冷冻状态
	3. 状态三（今天卖出股票）：刚刚从“买入状态“卖出
	4. 状态四（今天为冷冻期状态，但冷冻期状态不可持续，只有一天）：刚从今天卖出状态推导过来（这里完美解决了我自己思路中的迷思）
- 初始化：只将”买入状态“初始化为-prices[0], 其他都是0，至于为什么可以去代码随想录上看，我有点解释不清（是根据递推公式来看的，推出第一个元素的话，需要初始元素为甚，一种reverse engineering）。
- 遍历顺序：从小到大

**代码**
```Python 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #状态一(dp[i][0]):持有股票状态
        #状态二(dp[i][1]):保持卖出股票的状态
        #状态三(dp[i][2]):今天卖出股票
        #状态四(dp[i][3]):今天为冷冻期状态，但冷冻期状态不可持续，只有一天
        
        size=len(prices)
        dp=[[0]*4 for _ in range(size)]
        #初始化
        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=0
        dp[0][3]=0

        #遍历顺序
        for i in range(1,size):
            dp[i][0]=max(dp[i-1][0], dp[i-1][3]-prices[i], dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]

        return max(dp[-1][1],dp[-1][2],dp[-1][3])
```
### [《代码随想录》动态规划：买卖股票的最佳时机含手续费（动态规划）](https://notes.kamacoder.com/questions/502092)
#### 任务要求
#### 714.买卖股票的最佳时机含手续费


相对122.买卖股票的最佳时机II ，本题只需要在计算卖出操作的时候减去手续费就可以了，代码几乎是一样的，可以尝试自己做一做。
视频讲解：https://www.bilibili.com/video/BV1z44y1Z7UR 
https://programmercarl.com/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

##### 重要知识点

- 解题思路


**解题思路**

“买卖股票的最佳时机含手续费II”基础上加入手续费

**动规五部曲**

- dp数组下标以及定义:
```Python
            dp[i][0]:第i天不持有股票的最大利润
            dp[i][1]:第i天持有股票的最大利润
```
- 递推公式：
```Python
            dp[i][0]<--第i-1天不持有股票/第i天卖出股票 +手续费
            dp[i][1]<--第i-1天持有股票/第i天买入股票
```
- 初始化：
```Python
            dp[0][0]=0
            dp[0][1]=-prices[0]
```
- 遍历顺序：从小到大

**代码**
```Python 
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
 
        size=len(prices)
        dp=[[0]*2 for _ in range(size)]

        #初始化
        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1,size):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        
        return dp[-1][0]
```
