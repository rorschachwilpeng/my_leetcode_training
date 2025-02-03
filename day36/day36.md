# 代码随想录
## 动态规划
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
