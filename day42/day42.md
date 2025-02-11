# 代码随想录
## 动态规划
### [《代码随想录》动态规划：最长上升子序列](https://notes.kamacoder.com/questions/502094)
#### 任务要求
#### 300.最长递增子序列


今天开始正式子序列系列，本题是比较简单的，感受感受一下子序列题目的思路。 
视频讲解：https://www.bilibili.com/video/BV1ng411J7xP 
https://programmercarl.com/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**




**动规五部曲**

- dp数组下标以及定义:以i结尾的子序列的最大长度为dp[i]
- 递推公式：
```Python
if nums[i]>nums[j]:
	dp[i]=max(dp[i],dp[j]+1)
```
- 初始化：全部初始化为1（注意这里所有的值都需要初始化为1，因为子数组只有一个元素时，最长长度为1）
- 遍历顺序：先物品，后背包


**30min尝试的代码**❌❌❌
```Python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[0]*size

        dp[0]=1
        maxVal=0
        for i in range(1,size):
            if nums[i]>nums[i-1] and nums[i]>maxVal:
                dp[i]=dp[i-1]+1
                maxVal=nums[i]
            else:
                dp[i]=dp[i-1]
        return dp[-1]
````

错误的点：
1. 初始化错误，不应该只将dp[0]初始化为1；
2. 未正确遍历子序列的所有可能性 --> 代码中只比较了```nums[i]>nums[i-1]```的情况，这只考虑了相邻元素之间的递增关系
3. maxVal 不必要且逻辑有误


**代码**
```Python 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[1]*size#这里需要初始化成1

        #初始化
        result=1
        for i in range(1,size):
            for j in range(i):#要把i也算进来
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            result=max(result,dp[i])
        return result
```
### [《代码随想录》动态规划：最长连续递增序列](https://notes.kamacoder.com/questions/502095)
#### 任务要求
#### 674. 最长连续递增序列


本题相对于昨天的动态规划：300.最长递增子序列 最大的区别在于“连续”。 先尝试自己做做，感受一下区别  
视频讲解：https://www.bilibili.com/video/BV1bD4y1778v 
https://programmercarl.com/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题的重点相比上一题在于连续性的判断。


**动规五部曲**

- dp数组下标以及定义: dp[i] --> 以i为结尾的子数组的最长连续递增子序列长度为dp[i]
- 递推公式：-
- 初始化：-
- 遍历顺序：-


**30min尝试版本** ✅但是不够优化
```Python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        #dp数组下标以及含义:
            #dp[i]:以i为结尾的子数组的最长连续递增子序列长度为dp[i]
        size=len(nums)
        dp=[1]*size
        CONTINUE=False
        result=1
        #怎么保证连续性？
        for i in range(1,size):

            if nums[i]>nums[i-1] and CONTINUE:#连续数组
                dp[i]=max(dp[i], dp[i-1]+1)

            elif nums[i]>nums[i-1] and not CONTINUE:#第一个元素
                CONTINUE=True
                dp[i]=2

            else:
                dp[i]=dp[i-1]
                CONTINUE=False
            result=max(result,dp[i])
        return result
```

30min尝试版本的问题：
1. 引入了不必要的```CONTINUE```变量。判断是否属于连续递增子序列其实已经可以通过条件```nums[i]>nums[i-1]```得到。
2. 这种写法会引入不必要的分支判断，代码显得繁琐；
3. ```dp[i]=max(dp[i], dp[i-1]+1)```这个判断条件不适用于连续判断的情况，我们只需要在连续情况下更新dp数组即可。


**代码**
```Python 
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[1]*size
        result=1

        for i in range(1,size):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            result=max(result,dp[i])
        return result
```
### [《代码随想录》动态规划：最长重复子数组](https://notes.kamacoder.com/questions/502096)
#### 任务要求
#### 718. 最长重复子数组


稍有难度，要使用二维dp数组了
视频讲解：https://www.bilibili.com/video/BV178411H7hV 
https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

这题需要用二维数组来求


**动规五部曲**

- dp数组下标以及定义:dp[i][j]:在nums1中以i结尾的子数组 和 在nums2中以j结尾的子数组 的公共子数组长度为dp[i][j]
- 递推公式：- 
- 初始化：第一行第一列初始化为0，因为没有具体意义
- 遍历顺序：-

**30min尝试**❌❌❌
```Python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #初始化
        size1=len(nums1)
        size2=len(nums2)
        dp=[[0]*(size2+1) for _ in range(size1+1)]
        result=0
        for i in range(1,size1+1):#先遍历nums1
            for j in range(1, size2+1):#再遍历nums2
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
                 else:
                     dp[i][j]=max(dp[i-1][j],dp[i][j])
                result=max(result, dp[i][j])
        return result
```
错误的点：dp数组中，非相同元素的位置不用更新。

**代码**
```Python 
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #初始化
        size1=len(nums1)
        size2=len(nums2)
        dp=[[0]*(size2+1) for _ in range(size1+1)]
        result=0
        for i in range(1,size1+1):#先遍历nums1
            for j in range(1, size2+1):#再遍历nums2
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
                # else:
                #     dp[i][j]=max(dp[i-1][j],dp[i][j])
                result=max(result, dp[i][j])
        return result
```

