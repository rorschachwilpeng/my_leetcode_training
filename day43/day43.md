# 代码随想录
## 动态规划
### [《代码随想录》动态规划：最长公共子序列](https://notes.kamacoder.com/questions/502097)
#### 任务要求
#### 1143.最长公共子序列

体会一下本题和 718. 最长重复子数组 的区别  
视频讲解：https://www.bilibili.com/video/BV1ye4y1L7CQ 
https://programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html

##### 重要知识点

- 动规五部曲


**动规五部曲**

- 完全背包问题-->求组合
- dp数组下标以及定义: dp[i][j]:在text1中以i结尾的子序列和text2中以j结尾的子序列的最长公共子序列长度为dp[i][j]
- 递推公式：如果两个字符新相同的话，从dp[i-1][j-1]推出来。如果不相同的话，取dp[i-1][j]和dp[i][j-1]中最大的
```Python
if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
```
- 初始化：初始化为0
- 遍历顺序：遍历两个字符串

**代码**
```Python 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1=len(text1)
        size2=len(text2)

        #初始化
        dp=[[0]*(size2+1) for _ in range(size1+1)]

        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
```
### [《代码随想录》动态规划：不相交的线](https://notes.kamacoder.com/questions/502098)
#### 任务要求
#### 1035.不相交的线


其实本题和 1143.最长公共子序列 是一模一样的，大家尝试自己做一做。
视频讲解：https://www.bilibili.com/video/BV1h84y1x7MP 
https://programmercarl.com/1035.%E4%B8%8D%E7%9B%B8%E4%BA%A4%E7%9A%84%E7%BA%BF.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

实际上，这道题的本质仍然是求解最长公共子序列。即使题目要求在线条不相交的情况下找到最大连线数，归根结底，问题还是转换为在两个数组之间，寻找最长的相同子序列（可以是不连续的），同时保持原有的元素顺序，最终求出这个最长子序列的长度。


**动规五部曲**

- dp数组下标以及定义:dp[i][j]:nums1中以第i个数结尾，nums2中以第j个数结尾的两个数之间最大连线数为dp[i][j]
- 递推公式：
```Python
if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
```
- 初始化：构造dp数组的时候，多构造了一行一列。因为考虑到递推公式中我们需要考虑i-1和j-1，如果没有填充行列的话会数组越界，否则需要写多余的逻辑来处理
- 遍历顺序：从前到后遍历两个数组

**代码**
```Python 
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        size1=len(nums1)
        size2=len(nums2)

        dp=[[0]*(size2+1) for _ in range(size1+1)]

        for i in range(1,size1+1):
            for j in range(1, size2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
```
### [《代码随想录》动态规划：最大子序和（动态规划）](https://notes.kamacoder.com/questions/502099)
#### 任务要求
#### 53. 最大子序和


这道题我们用贪心做过，这次 再用dp来做一遍 
视频讲解：https://www.bilibili.com/video/BV19V4y1F7b5 
https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

##### 重要知识点
- 解题思路
- 动规五部曲


**解题思路**

其实和贪心思路一样的。越来越觉得其实动态规划就是 “局部贪心 + 递归构造”。这个和BERT模型里面用的WordPiece也是一样的思想。 


**动规五部曲**
1. dp数组下标以及定义 -->dp[i]:第i个元素所对应的子数组中的连续子数组的最大和为dp[i]
2. 递推公式 -->dp[i]=max(dp[i-1]+nums[i],nums[i])
3. 初始化 --> dp[0]=nums[0] & result[0]=dp[0]
4. 遍历顺序 --> 从前到后
5. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[0]*(size)
        dp[0]=nums[0]
        result=dp[0]
        for i in range(1,size):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            result=max(dp[i],result)
        return result
```
### [《代码随想录》动态规划：判断子序列](https://notes.kamacoder.com/questions/502100)
#### 任务要求
#### 392.判断子序列


这道题目算是 编辑距离问题 的入门题目（毕竟这里只是涉及到减法），慢慢的，后面就要来解决真正的 编辑距离问题了

https://programmercarl.com/0392.%E5%88%A4%E6%96%AD%E5%AD%90%E5%BA%8F%E5%88%97.html

##### 重要知识点
- 解题思路
- 动规五部曲

**解题思路**

本题其实和“最长公共子序列”的思路是一样。只是在做递推公式时候，如果两个字符串不相同的话，我们只能删除s中的字符。

**动规五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i][j]:以i-1结尾的t序列和以j-1结尾的s序列的子序列长度为dp[i][j]
2. 递推公式 --> 
```Python
if t[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:#只能在t字符串中删除字符
                    dp[i][j]=dp[i-1][j]
```
4. 初始化 --> 初始化为0即可，但是要加填充的第一行和第一列，方便进行递推
5. 遍历顺序 --> 从前到后
6. 打印dp数组 --> ~

**代码**
```Python 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size1=len(t)+1
        size2=len(s)+1
        dp=[[0]*(size2) for _ in range(size1)]
        
        for i in range(1,size1):
            for j in range(1,size2):
                if t[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:#只能在t字符串中删除字符
                    dp[i][j]=dp[i-1][j]
        
        return dp[-1][-1]==len(s)
```
