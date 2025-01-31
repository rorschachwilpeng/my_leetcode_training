# 代码随想录
## 动态规划
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
