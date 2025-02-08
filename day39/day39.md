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
### [《代码随想录》动态规划：不同路径](https://notes.kamacoder.com/questions/502065)
#### 任务要求
#### 62.不同路径


本题大家掌握动态规划的方法就可以。 数论方法 有点非主流，很难想到。 

https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html   
视频讲解：https://www.bilibili.com/video/BV1ve4y1x7Eu

##### 重要知识点
- 解题思路



**解题思路**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i][j]:走到坐标[i,j]总共有多少条不同的路径
2. 递推公式 --> dp[i][j]=dp[i-1][j]+dp[i][j-1]
3. 初始化 --> 在二维数组/矩阵中，第一行初始化为1，第一列也需要初始化为1
4. 遍历顺序 --> 从左往右，从上往下
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]

        #边界需要都初始化成1
        for i in range(0,m):#从上往下
            dp[i][0]=1
        for j in range(1,n):#从左往右
            dp[0][j]=1
        print(dp)
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
```
### [《代码随想录》动态规划：不同路径II](https://notes.kamacoder.com/questions/502066)
#### 任务要求
#### 63. 不同路径 II


[https://programmercarl.com/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.htmlhttps://programmercarl.com/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.html](https://programmercarl.com/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.html)  
视频讲解：https://www.bilibili.com/video/BV1Ld4y1k7c6

##### 重要知识点
- 解题思路



**解题思路**

和“#62.不同路径”差不多，只是需要判断障碍物

1. dp数组下标以及定义 --> dp[i][j]:走到坐标[i,j]总共有多少条不同的路径
2. 递推公式 --> dp[i][j]=dp[i-1][j]+dp[i][j-1]
3. 初始化 --> 在二维数组/矩阵中，第一行初始化为1，第一列也需要初始化为1
4. 遍历顺序 --> 从左往右，从上往下
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        hor=len(obstacleGrid)
        ver=len(obstacleGrid[0])
        dp=[[0]*ver for _ in range(hor)]

        #初始化
        for j in range(ver):#从左往右
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1
        for i in range(hor):#从上往下
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1

        for i in range(1,hor):
            for j in range(1,ver):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[hor-1][ver-1]
```
### [《代码随想录》动态规划：整数拆分](https://notes.kamacoder.com/questions/502067)
#### 任务要求
#### 343.  整数拆分 （可跳过）

本题思路并不容易想，一刷建议可以跳过。如果学有余力，可以看视频理解一波。

https://programmercarl.com/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.html    
视频讲解：https://www.bilibili.com/video/BV1Mg411q7YJ

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

自己想到了解题思路，但是没能将思路抽象成递推公式。思路还是比较直接的，我们利用拆分的方法（类似于二叉树中的拆分）来找最大乘积。举个例子，如果n为10的话，10可以拆分成"1+9","2+8","3+7","4+6",..。其中对于"1+9"的话，9又可以拆分成"1+8","2+7",....。这样我们已经可以发现了递归公式的痕迹。


抽象成递推公式的话，

```dp[i] = max(dp[i], j * (i-j), j * dp[i-j])```

这代表着我们可以计算当前的最大乘积，或者继续拆分再计算乘积

**动规五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i]:正整数i拆分后最大乘积为dp[i]
2. 递推公式 --> ```dp[i]=max(dp[i],i*(i-j),i*dp[i-j])```
3. 初始化 --> dp[2]=1
4. 遍历顺序 --> 每次只遍历一半就可以了
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def integerBreak(self, n):
        dp=[0]*(n+1)
        
        dp[2]=1

        for i in range(3,n+1):
            for j in range(1,(i//2)+1):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]
```
### [《代码随想录》动态规划：不同的二叉搜索树](https://notes.kamacoder.com/questions/502068)
#### 任务要求
#### 96 .不同的二叉搜索树 （可跳过）

本题思路并不容易想，一刷建议可以跳过。 如果学有余力，可以看视频理解一波。

https://programmercarl.com/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html    
视频讲解：https://www.bilibili.com/video/BV1eK411o7QA

##### 重要知识点
- 解题思路



**解题思路**

抄了一遍代码，但还没有完全理解



**代码**
```Python 
class Solution:
    def numTrees(self, n: int) -> int:
        #二叉搜索树的特性是按照中序遍历可以得到的是一个递增数组
        dp = [0]*(n+1)
        dp[0]=1#初始化
        for i in range(1,n+1):
            for j in range(1, i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
```
### [《代码随想录》动态规划：分割等和子集](https://notes.kamacoder.com/questions/502071)
#### 任务要求
#### 416. 分割等和子集

本题是 01背包的应用类题目
https://programmercarl.com/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.html     
视频讲解：https://www.bilibili.com/video/BV1rt4y1N7jE

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

求解本题，我们首先需要将问题转换一下。如果这个数组可以分割成两个元素和相等子集的话，那么每个子集的元素和一定等于数组中所有元素和的一半，如此我们可以将问题转换成了背包问题 -- **能否装满容量为target的背包**。

==>

背包 --> 容量：元素和

物品 --> 价值：每个元素值；数量: 每一个元素只能用一次（01背包问题） ；重量：每个元素值（本题中物品的 价值==重量）；


**动规五部曲**

用一维数组来做的五部曲：

1. dp数组下标以及定义 --> dp[j]: 容量为j的背包能够装下的最大价值为dp[j]
2. 递推公式 -->  ```dp[j]=max(dp[j], dp[j-nums[i]+nums[i]]) ```
3. 初始化 --> 都初始化为0，因为题目中已经说了数组中只包含正整数
4. 遍历顺序 --> 先物品，再背包（组合问题）；且背包从大到下遍历（01背包问题）
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        else:
            target=int(sum(nums)/2)
        dp=[0]*10001

        for val in nums:#物品
            for j in range(target,val-1,-1):#背包
                dp[j]=max(dp[j],dp[j-val]+val)
        if dp[target]==target:
            return True
        return False
```
### [《代码随想录》动态规划：最后一块石头的重量II](https://notes.kamacoder.com/questions/502072)
#### 任务要求
#### 1049. 最后一块石头的重量 II


本题就和 昨天的 416. 分割等和子集 很像了，可以尝试先自己思考做一做。 
视频讲解：https://www.bilibili.com/video/BV14M411C7oV  
https://programmercarl.com/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题解题思路还是比较好想的，在数组内找到元素和最接近sum/2的子集，这个子集和数组中剩余元素对撞得到的结果最小。

==>

背包 --> 容量：元素和

物品 --> 价值：每个元素值；数量: 每一个元素只能用一次（01背包问题） ；重量：每个元素值（本题中物品的 价值==重量）；


**动规五部曲**

用一维数组来做的五部曲：

1. dp数组下标以及定义 --> dp[j]: 容量为j的背包能够装下的最大价值为dp[j]
2. 递推公式 -->  ```dp[j]=max(dp[j], dp[j-nums[i]+nums[i]]) ```
3. 初始化 --> 都初始化为0，因为题目中已经说了数组中只包含正整数
4. 遍历顺序 --> 先物品，再背包（组合问题）；且背包从大到下遍历（01背包问题）
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target=sum(stones)//2
        size=len(stones)
        dp=[0]*(1500+1)
        
        for stone in stones:#物品
            for j in range(target,stone-1,-1):#背包
                dp[j]=max(dp[j],dp[j-stone]+stone)
        
        return sum(stones) - 2*dp[target]
```
### [《代码随想录》动态规划：目标和](https://notes.kamacoder.com/questions/502073)
#### 任务要求
#### 494. 目标和

大家重点理解 递推公式：dp[j] += dp[j - nums[i]]，这个公式后面的提问 我们还会用到。  
视频讲解：https://www.bilibili.com/video/BV1o8411j73x 
https://programmercarl.com/0494.%E7%9B%AE%E6%A0%87%E5%92%8C.html


##### 重要知识点

- 解题思路
- 动规五部曲
- 递推公式是怎么来的

**解题思路**

本题的背包问题：有多少种方法装满背包

==>

背包 --> 容量：元素和

物品 --> 价值：每个元素值；数量: 每一个元素只能用一次（01背包问题） ；重量：每个元素值（本题中物品的 价值==重量）；



**动规五部曲**

用一维数组来做的五部曲：

1. dp数组下标以及定义 --> dp[j]: 有dp[j]种方法装满容量为j的背包
2. 递推公式 -->  ```dp[j]+=dp[j-num] ```
3. 初始化 --> dp[0]=1（因为容量为0的时候，不放物体就是一种装法）
4. 遍历顺序 --> 先物品，再背包（组合问题）；且背包从大到下遍历（01背包问题）
5. 打印dp数组 --> ~


**递推公式是怎么来的**
![截屏2025-02-01 09.03.35.png](http://cdn.notes.kamacoder.com/611f7fc7-7a91-4aba-bf63-683307a08ea7.png) 


**代码**
```Python 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #特殊情况判断
        total_sum=sum(nums)
        if total_sum<abs(target):
            return 0
        if (total_sum+target)%2==1:
            return 0
        #首先将问题转换成背包问题
        left=(sum(nums)+target)//2
        dp=[0]*(left+1)
        dp[0]=1
        for num in nums:
            for j in range(left,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[left]
```
### [《代码随想录》动态规划：一和零](https://notes.kamacoder.com/questions/502074)
#### 任务要求
#### 474.一和零

通过这道题目，大家先粗略了解， 01背包，完全背包，多重背包的区别，不过不用细扣，因为后面 对于 完全背包，多重背包 还有单独讲解。
视频讲解：https://www.bilibili.com/video/BV1rW4y1x7ZQ  
https://programmercarl.com/0474.%E4%B8%80%E5%92%8C%E9%9B%B6.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

我们首先先要明确本题其实还是一个01背包问题。只不过每一个物品会同时放进两个背包中，即需要同时考虑两个背包的容量，一个背包装“0”，另一个背包装“1”。

**动规五部曲**

用一维数组来做的五部曲：

1. dp数组下标以及定义 --> dp[j]: 容量为i的背包（用来装0）和容量为j的背包（用来装1）最多能够装下的子集长度为dp[i][j]
2. 递推公式 -->  ```dp[i][j]=max(dp[i][j],dp[i-num_zero][j-num_one]+1) ```
3. 初始化 --> 都初始化为0，第一行和第一列也为0，因为每个物品是同时放入两个背包的
4. 遍历顺序 --> 从左到右，从上到下
5. 打印dp数组 --> ~


**代码**
```Python 
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(m+1) for _ in range(n+1)]
        for item in strs:#物品
            num_zero=item.count("0")
            num_one =item.count("1")
            
            for i in range(n,num_one-1,-1):#背包1
                for j in range(m,num_zero-1,-1):#背包0
                    dp[i][j]=max(dp[i][j], dp[i-num_one][j-num_zero]+1)
        
        return dp[-1][-1]
```
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
### [《代码随想录》动态规划：打家劫舍](https://notes.kamacoder.com/questions/502084)
#### 任务要求
#### 198.打家劫舍

视频讲解：https://www.bilibili.com/video/BV1Te411N7SX 
https://programmercarl.com/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.html

##### 重要知识点

- 重点知识点
- 动规五部曲

**重点知识点**

打家劫舍的第一题。

关键在于dp数组的定义以及递推公式的构造，首先需要明确dp数组 --> dp[i]:考虑下标为i（包括i）在内的房屋，能够偷窃到的最高金额为dp[i]。然后分析递推关系，对于房屋 **i** 而言，我们有两个状态，偷还是不偷。偷的话，当前状态 **i** 只能是通过 **i-2** 房屋推出来的，因为我们在同一晚偷相邻的房屋。不偷的话，当前状态 **i** 则是通过 **i-1** 房屋推出来的。根据分析，不难写出递推公式： ```dp[j]=max(dp[i-2]+nums[i],dp[i-1])```。

初始化的话，是根据递推公式来做的，将dp[0]初始化为第一个元素，dp[1]初始化为前两个元素中的最大值。



**动规五部曲**

- 打家劫舍问题
- dp数组下标以及定义:考虑下标为i（包括i）在内的房屋，能够偷窃到的最高金额为dp[i]
- 递推公式：dp[i]=max(dp[i-2]+num,dp[i-1])
- 初始化：dp[0]=0,dp[1]=max(dp[0],dp[1])
- 遍历顺序：从左到右

**代码**
```Python 
class Solution:
    def rob(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[0]*size
        if size==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,size):
            dp[i]=max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
```
### [《代码随想录》动态规划：打家劫舍II](https://notes.kamacoder.com/questions/502085)
#### 任务要求
#### 213.打家劫舍II

视频讲解：https://www.bilibili.com/video/BV1oM411B7xq 
https://programmercarl.com/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题的难点是首尾相连的情况讨论，最直白的思路就是将首尾情况分类讨论，根据这种分而治之的策略我们可以得到三种情况：

情况一：考虑除了尾以外的元素

情况二：考虑除开首尾的中间元素

情况三：考虑除了头以外的元素

注意：这里是考虑，并不代表选择！


**动规五部曲**

- dp数组下标以及定义: 具体的代码实现里面我们不用dp数组了，否则空间复杂度很高
- 递推公式：和打家劫舍一样，只是这里我们用的双指针来实现
- 初始化：和“打家劫舍I”逻辑一样，dp[0]=nums[0], dp[1]=max(nums[0], nums[1])
- 遍历顺序：-

**代码**
```Python 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end+1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max
```
### [《代码随想录》动态规划：打家劫舍III](https://notes.kamacoder.com/questions/502086)
#### 任务要求
#### 337.打家劫舍III

视频讲解：https://www.bilibili.com/video/BV1H24y1Q7sY 
https://programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

1. 二叉树的遍历顺序：本题一定要用后序遍历，因为我们需要利用子节点返回值做判断
2. 打家劫舍的思路：对于每个节点都有两个状态：偷 / 不偷
3. 我们从下到上递归整颗二叉树，对于每个节点都进行判断，如果偷当前节点的话，就不偷其子节点；如果不偷当前节点的话，偷子节点。递归函数的终止条件是遇到空节点。


**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)
    def traversal(self, node):
        if not node:
            return (0,0)
        
        #后序遍历
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        #不偷当前节点，偷子节点
        val_0 = max(left[0],left[1])+max(right[0], right[1])

        #偷当前节点，不偷子节点
        val_1 = node.val+left[0]+right[0]

        return (val_0, val_1)
```

