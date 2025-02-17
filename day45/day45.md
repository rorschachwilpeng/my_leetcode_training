# 代码随想录
## 动态规划
### [《代码随想录》动态规划：编辑距离](https://notes.kamacoder.com/questions/502103)
#### 任务要求
#### 72. 编辑距离


最终我们迎来了编辑距离这道题目，之前安排题目都是为了 编辑距离做铺垫。 

https://programmercarl.com/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html

##### 重要知识点
- 解题思路
- 动规五部曲


**解题思路**

编辑距离，dp数组的下标以及定义: dp[i][j] --> 表示以i-1为结尾的字符串word1,和下标j-1为结尾的字符串word2，最近的编辑距离为dp[i][j]。递推公式中，如果word1[i-1]==word2[j-1]的话，那么不需要操作，直接让dp[i][j]=dp[i-1][j-1]就可以了。如果word1[i-1]!=word2[j-1]不相同的话，那么可能有三种情况：1. 增加；2. 删除；3. 替换。其中增加元素其实是和删除元素的递推公式一样的，可能存在的情况包括：需要从word1中删除一个字符（dp[i-1][j]+1）/从word2中删除一个字符(dp[i][j-1]+1)。对于替换的话，只需要一次替换操作，就可以让word1[i-1]==word2[j-1]，所以dp[i][j]=dp[i-1][j-1]+1


**动规五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i][j]:表示以下标i-1为结尾的字符串word1,和下标j-1为结尾的字符串word2,最近编辑距离为dp[i][j]
2. 递推公式 -->
```
 if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    #增/删/替换
                    #其中删除和增加的递推公式其实是一样的
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
```
3. 初始化 --> 初始化第一行和第一列
4. 遍历顺序 --> 从前到后
5. 打印dp数组 --> ~


**代码**
```Python 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1=len(word1)+1
        size2=len(word2)+1
        dp=[[0]*size2 for _ in range(size1)]

        #初始化
        for i in range(1,size1):
            dp[i][0]=i
        for j in range(1,size2):
            dp[0][j]=j
        
        for i in range(1,size1):
            for j in range(1,size2):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    #增/删/替换
                    #其中删除和增加的递推公式其实是一样的
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]
```
### [《代码随想录》动态规划：回文子串](https://notes.kamacoder.com/questions/502105)
#### 任务要求
#### 647. 回文子串


动态规划解决的经典题目，如果没接触过的话，别硬想 直接看题解。
https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题的递推思路是从短子串扩展到长子串。扩展过程中，如果两端字符不相等，则当前子串不是回文；如果两端字符相等，则需要判断当前子串是否是回文（如果短子串已经是回文了，且拓展出来的字符也相等，自然可以推导出长子串是回文串）。根据这个思路，dp数组的下标以及定义应该为：“设 `dp[i][j]` 表示字符串 `s` 的子串 在`[i,j]`范围是否是回文子串。”，dp数组的值是bool类型。


**动态规划五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i][j]:表示区间范围`[i,j]`的子串是否是回文子串，如果是dp[i][j]为true, 否则为false。
2. 递推公式 --> 

在确定递推公式中需要考虑的情况：`s[i]`和`s[j]`相等 / `s[i][j]`不相等。如果不相等的话，那么`dp[i][j]`一定是false。如果相等的话，需要分类讨论：

情况一： 下标i和下标j相同，同一个字符例如a，那么一定是回文串；
情况二：下标i和下标j相差为1，例如aa/bb，那么也一定是回文串；
情况三：下标i和下标j相差大于1的时候，我们就需要判断dp[i+1][j-1]是否为true（短子串是否为回文串）

 
4. 初始化 -->  全部初始化为False
5. 遍历顺序 --> 根据递推公式不难得到，本题中的dp[i][j]是根据dp[i+1][j-1]推导出来的。这意味着我们需要从上到下，从左到右进行递推
6. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def countSubstrings(self, s: str) -> int:
        size=len(s)
        dp=[[False]*size for _ in range(size)]
        result=0
        for i in range(size-1,-1,-1):
            for j in range(i,size,+1):
                if s[i]==s[j]:
                    if j-i<=1:#情况一和情况二
                        result+=1
                        dp[i][j]=True
                    elif dp[i+1][j-1]:#情况三
                        result+=1
                        dp[i][j]=True
        return result
```
