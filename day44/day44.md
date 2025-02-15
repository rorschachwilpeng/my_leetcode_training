# 代码随想录
## 动态规划
### [《代码随想录》动态规划：不同的子序列](https://notes.kamacoder.com/questions/502101)
#### 任务要求
#### 115.不同的子序列


但相对于刚讲过 392.判断子序列，本题 就有难度了 ，感受一下本题和  392.判断子序列 的区别。 

https://programmercarl.com/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

还是删除元素，但是相比上一题的话我们需要考虑的是有多少种不同的删除方法。刚开始我以为这和背包问题中的求有多少种装满背包的方法很像，但其实并不是。



**动态规划五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 --> dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]。
2. 递推公式 -->
 两种情况，情况一: s[i-1]和t[j-1]不相等；情况二：s[i-1]和t[j-1]相等。
 对于情况二：我们又要分成两种情况，1. 用s[i-1]来匹配，2.不用s[i-1]匹配。例如： s：bagg 和 t：bag ，s[3] 和 t[2]是相同的，但是字符串s也可以不用s[3]来匹配，即用s[0]s[1]s[2]组成的bag。一部分是用s[i - 1]来匹配，那么个数为dp[i - 1][j - 1]。即不需要考虑当前s子串和t子串的最后一位字母，所以只需要 dp[i-1][j-1]。一部分是不用s[i - 1]来匹配，个数为dp[i - 1][j]（相当于是用s中前前索引的字符来匹配t中当前索引对应的字符）。
 
4. 初始化 --> 第一行初始化为1，因为如果t为空集的话，那么s把全部字符删掉就能得到t；第一列初始化为0，因为我们只需要在s的子序列中找t
5. 遍历顺序 --> 从前到后
6. 打印dp数组 --> ~



**代码**
```Python 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        size1=len(s)+1
        size2=len(t)+1
        dp=[[0]*size2 for _ in range(size1)]
        
        #初始化
        for i in range(size1):
            dp[i][0]=1
        for j in range(1,size2):
            dp[0][j]=0#我们是看s的子序列中t出现的个数


        for i in range(1,size1):
            for j in range(1, size2):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
```
### [《代码随想录》动态规划：两个字符串的删除操作](https://notes.kamacoder.com/questions/502102)
#### 任务要求
#### 583. 两个字符串的删除操作


本题和动态规划：115.不同的子序列 相比，其实就是两个字符串都可以删除了，情况虽说复杂一些，但整体思路是不变的。
https://programmercarl.com/0583.%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C.html

##### 重要知识点
- 解题思路
- 动规五部曲


**解题思路**

这题自己做AC了，但是是靠画动态规划的递推过程做出来的。重点是根据dp数组的含义进行递推和理解。当两个字符串中的字符相等时，那么我们不用¨做删除操作，当前dp[i][j]等于dp[i-1][j-1]。而当字符不相等时，就存在三种情况了：1. 需要删除word1中的元素；2. 删除word2中的元素；3.删除word1和word2中的元素。



**动规五部曲**

直接列出动规五部曲
1. dp数组下标以及定义 -->dp[i][j]:能让word1和word2相同所需的最小步数为dp[i][j]
2. 递推公式 --> 
```Python
if word1[i-1]==word2[j-1]:
	dp[i][j]=dp[i-1][j-1]
else:
	dp[i][j]=min(dp[i-1][j-1]+2,dp[i][j-1]+1,dp[i-1][j]+1)
```

4. 初始化 --> 第一行和第一列初始化为当前字符串长度
5. 遍历顺序 --> 从前到后
6. 打印dp数组 --> ~


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
        
        #递推公式
        for i in range(1,size1):
            for j in range(1,size2):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1]+2,dp[i][j-1]+1,dp[i-1][j]+1)
        
        return dp[-1][-1]
```
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

