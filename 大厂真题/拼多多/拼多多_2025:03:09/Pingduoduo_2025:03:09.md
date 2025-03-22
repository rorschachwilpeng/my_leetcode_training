# 大厂真题
## 拼多多
### [2025年3月09日](https://codefun2000.com/p/P2673)
#### 任务要求
#### 拼多多-2025年3月09日-算法岗位-传送门游戏
https://codefun2000.com/p/P2672

##### 重要知识点
- 代码实现

**代码实现**

```Python
#利用贪心的思想，距离初始位置的最大值即正负值的绝对值之和

n=int(input())
arr=list(map(int,input().strip().split()))

#将数组中的正负进行分类
res=0
for item in arr:
    if item>=0:#正数
        res+=item
    else:#负数
        res+=(-item)
print(res)
```


### [2025年3月09日](https://codefun2000.com/p/P2673)
#### 任务要求
#### 拼多多-2025年3月09日-算法岗位-传送门游戏2

https://codefun2000.com/p/P2673

##### 重要知识点
- 暴力枚举思路
- 利用前后缀的解题思路
- 代码实现

**暴力枚举思路**

如果使用暴力枚举思路的话，我们需要：

1. 枚举`i`作为反转点；
2. 计算`S[j]`在`i`之后的最大值和最小值（因为`|S[j]-2*s[i]|`取决于`s[j]`的最值）。
3. 计算`max(abs(S[j])-2*S[i])`

但问题是：

- 如果使用暴力方法，每次计算`S[j]`的最大/最小值，需要`O(n)`时间，整体复杂度是`O(n^2)`,会超时。
- 但是如果使用后缀最大/最小值的数组，我们可以在`O(n)`的时间复杂度内完成这部分计算。


**利用前后缀的解题思路**

核心步骤：计算前缀和，记录前缀和中的最大值 --> 计算后缀最大和最小值（即最值） --> 枚举最大距离，找到答案

1. 计算前缀和，记录前缀和中的最大值
```Python
ans=0#最终结果
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+arr[i-1]
    #2.计算前缀和中的最大值
    ans=max(ans,prefix[i])
```

2. 计算后缀的最大值和最小值

这里比较晦涩的一点是关于计算后缀和的步骤。因为后缀是从右往左的，所以我们在遍历的时候也需要从右往左，这其实和前缀和思路一样，只是调换了方向。

需要特别注意的是`postfix_max[i]`代表下一个后缀和，需要参考上一个后缀和的结果`postfix_max[i+1]`。

```Python
postfix_max=[0]*(n+1)
postfix_min=[0]*(n+1)
postfix_max[n]=prefix[n]#更新第一个后缀元素
postfix_min[n]=prefix[n]#更新第一个后缀元素
for i in range(n-1,-1,-1):
    postfix_max[i]=max(postfix_max[i+1],prefix[i])
    postfix_min[i]=min(postfix_min[i+1],prefix[i])
```

4. 枚举最大距离

枚举前后缀数组元素计算最大距离的公式是怎么来的：
<img src="img1.png" width="800" />

```Python
for i in range(n+1):
    val1=abs(postfix_max[i]-2*prefix[i])
    val2=abs(postfix_min[i]-2*prefix[i])
    ans=max(ans,val1,val2)
print(ans)
```

**代码实现**

```Python
n=int(input())
arr=list(map(int,input().strip().split()))

#1.计算前缀和
ans=0#最终结果
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+arr[i-1]
    #2.计算前缀和中的最大值
    ans=max(ans,prefix[i])

#3.计算后缀和的最大值和最小值
postfix_max=[0]*(n+1)
postfix_min=[0]*(n+1)
postfix_max[n]=prefix[n]#更新第一个后缀元素
postfix_min[n]=prefix[n]#更新第一个后缀元素
for i in range(n-1,-1,-1):
    postfix_max[i]=max(postfix_max[i+1],prefix[i])
    postfix_min[i]=min(postfix_min[i+1],prefix[i])

#4.计算最大距离
for i in range(n+1):
    val1=abs(postfix_max[i]-2*prefix[i])
    val2=abs(postfix_min[i]-2*prefix[i])
    ans=max(ans,val1,val2)
print(ans)
```


# 大厂真题
## 拼多多
### [2025年3月09日](https://codefun2000.com/p/P2673)
#### 任务要求
#### 拼多多-2025年3月09日-算法岗位-多多读书

https://codefun2000.com/p/P2673

##### 重要知识点
- 如何将问题转化为背包问题
- 动规五部曲
- 代码实现

**如何将问题转化为背包问题**

题目通读下来就是一股浓浓的动规味。我们可以将问题抽象化为背包问题，这能帮助我们更好了解题意。


首先在背包问题中，
对于物品：
- 价值
- 重量
- 数量

对于背包：
- 容量
- 数量

那我们可以先找到题目中和背包问题中变量之间的映射关系。题目中说了，我们需要在读完书的前提下，尽可能地多获取知识量。那么我们不难知道“物品价值”即题目中的“知识量”。“物品重量”即“每次读多少页”。如果我们需要在指定时间内读完书的话，那么背包的“容量”不就是**在指定时间内需要读完的页数**吗？同时我们只需要读完这一本书，即“背包数量”为1，这是一个01背包问题。


总结一下，所以我们的映射关系如下
对于物品：
- 价值-->知识量
- 重量-->每次读多少
- 数量

对于背包：
- 容量-->在指定时间内需要读完的页数
- 数量-->1个

而问题页可以抽象成一个背包问题来理解：**装满背包的前提下，能够装下的最大重量是？**。

**动态规划五部曲**

1. **dp数组的下标以及含义**：dp[i][j]（i代表物品）（j代表背包）-->在j分钟内读完前i页能获取到的最大知识量为dp[i][j]。


2. **递推公式**：题目已经明确，对于单次遍历我们有两种状态转移方式：
    - 正常读，即一分钟读一页，这种情况下的递推公式为：
        `dp[i][j]=max(dp[i][j], dp[i-1][j-1]+s[i])`
    - 使用能力，一分钟读两页，这种情况下的递推公式为：
        `dp[i][j]=max(dp[i][j], dp[i-1][j-2]+(s[i]+s[i-1])/2.0)`

3. **初始化**
    - 要求最大值，且物品值都为正数，那么我们可以将二维dp数组都初始化为"-1"
    - 同时为了递推可达性，将dp[0][0]初始化为0，不然算不出来...


4. **遍历顺序**：这道题中不要求顺序，所以我们求组合就行。组合的遍历顺序是先物品，再背包


**代码实现**
```Python
n,m=map(int,input().strip().split())#页数（物品），时间（背包）
s=[0.0]+list(map(float,input().strip().split()))

def main():
    #首先判断极端情况（每次每分钟都读两页）能否装满背包，
    #如果不能装满的话，直接返回-1
    #如果能够装满的话再继续
    if m*2<=n:
        print(-1)
        return
    
    #初始化
    dp=[[-1.0]*(m+1) for _ in range(n+1)]
    dp[0][0]=0.0
    
    ans=-1.0#最终答案
    for i in range(1,n+1):#先遍历物品
        for j in range(1,m+1):#再遍历背包
            if dp[i-1][j-1]>=0:#正常读
                dp[i][j]=max(dp[i][j], dp[i-1][j-1]+s[i])
            if i>=2 and dp[i-2][j-1]>=0:#使用能力
                dp[i][j]=max(dp[i][j], dp[i-2][j-1]+(s[i]+s[i-1])/2.0)
    ans=max(dp[n][1:m+1])
            
    if ans<0:
        print(-1)
    print(ans)
    
main()
```