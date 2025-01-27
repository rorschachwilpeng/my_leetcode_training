# 代码随想录
## 动态规划
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
