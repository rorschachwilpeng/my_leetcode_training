# 代码随想录
## 数组
### 《代码随想录》数组：长度最小的子数组
#### 任务要求
#### 209.长度最小的子数组

题目建议： 本题关键在于理解滑动窗口，这个滑动窗口看文字讲解 还挺难理解的，建议大家先看视频讲解。  拓展题目可以先不做。 

题目链接：https://leetcode.cn/problems/minimum-size-subarray-sum/ 

文章讲解：https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html 

视频讲解：https://www.bilibili.com/video/BV1tZ4y1q7XE
##### 重要知识点
- （最小）滑动窗口
- 具体代码实现中的知识点

**（最小）滑动窗口**

使用两个指针（快指针和慢指针）构造滑动窗口。快指针用于扩展窗口，慢指针用于缩小窗口。当窗口内的元素和大于等于 target 时，尝试缩小窗口以找到最短子数组。

**具体代码实现中的知识点**

首次提交的超时问题是由于重复计算窗口总和（```tmp=sum(nums[slow:fast])```）导致的。解决方法是维护一个变量 tmp 来存储窗口总和，每次只更新变化部分，避免使用 sum()。

注意：内循环中的操作顺序很重要，需要先更新结果，再移动慢指针。

操作顺序：
 1. 计算当前窗口长度，更新最小子数组长度（全局最小值）。
 2. 减去当前慢指针对应的值（缩小窗口），再移动慢指针。


```Python 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 使用两个指针（快指针和慢指针）构造滑动窗口。
        # 快指针用于扩展窗口，慢指针用于缩小窗口。
        # 当窗口内的元素和大于等于 target 时，尝试缩小窗口以找到最短子数组。
        
        slow = 0
        fast = 0
        size = len(nums)
        res = float('inf')
        tmp = 0  # 窗口总和
        
        while fast < size:
            tmp += nums[fast]  # 扩展窗口，更新窗口总和
            while tmp >= target:
                # 1. 计算当前窗口长度，更新最小子数组长度（全局最小值）。
                res = min(res, fast - slow + 1)
                # 2. 缩小窗口：减去当前慢指针对应的值，再移动慢指针。
                tmp -= nums[slow]
                slow += 1
            fast += 1  # 快指针向右扩展窗口
        
        # 如果未找到满足条件的子数组，返回 0；否则返回结果。
        return 0 if res == float('inf') else res
```

### 《代码随想录》数组：螺旋矩阵II
#### 任务要求
#### 59.螺旋矩阵II
题目建议：  本题关键还是在转圈的逻辑，在二分搜索中提到的区间定义，在这里又用上了。 

题目链接：https://leetcode.cn/problems/spiral-matrix-ii/ 

文章讲解：https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html 

视频讲解：https://www.bilibili.com/video/BV1SL4y1N7mV/
##### 重要知识点
- 循环不变量

**循环不变量**

循环不变量是一种确保算法在每轮迭代中保持特定条件成立的设计思路，用于保证逻辑的正确性和简洁性。
在该代码中，**循环不变量**的构造体现在以下方面：
1. **每圈的起点与边界**：
	- 使用变量 `start_x` 和 `start_y` 定义当前圈的左上角起点。
	- 使用变量 `offset` 控制当前圈的边界范围（与 `n-offset` 结合，确定右下角边界）。
2. **每次更新后的规则保持一致**：
	- 每次完成一圈后，更新 `start_x`, `start_y`, 和 `offset`，确保下一个圈的范围缩小并保持一致的方向顺序。
4. **特殊情况处理**：
	- 如果矩阵 `n` 为奇数，中心元素单独处理 (`grid[circles][circles]`)。

**关键点**：通过维护 `start_x`, `start_y` 和 `offset` 的规则性更新，使得每圈操作对矩阵的填充范围始终正确。

**代码**
```Python 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #如何构造循环不变量
        grid=[[0]*n for _ in range(n)]
        #如果n为奇数-->矩阵中心会有一个多的元素
        #如果n为偶数-->矩阵中心没有多的元素

        circles=n//2#转几圈
        offset=1#偏置-->用于构造循环不变量
        start_x,start_y=0,0
        counter=1#当前元素

        for item in range(1,circles+1):
            #从左到右
            for j in range(start_y,n-offset):
                grid[start_x][j]=counter
                counter+=1
            #从上到下
            for i in range(start_x,n-offset):
                grid[i][n-offset]=counter
                counter+=1

            #从右到左
            for j in range(n-offset,start_y,-1):
                grid[n-offset][j]=counter
                counter+=1

            #从下到上
            for i in range(n-offset,start_x,-1):
                grid[i][start_y]=counter
                counter+=1
            #更新下一圈的变量
            start_x+=1
            start_y+=1
            offset+=1
        if n%2==1:
            grid[circles][circles]=counter
        return grid
```

### 《代码随想录》数组：区间和
#### 任务要求
#### 区间和

前缀和是一种思维巧妙很实用 而且 很有容易理解的一种算法思想，大家可以体会一下

文章讲解：https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html
##### 重要知识点
- 前缀和
- 代码中的**前缀和**实现
- 前缀和的业务应用场景

**前缀和**
1. **前缀和定义**：
	   对于原数组 `nums`，其前缀和数组 `arr` 的第 `i` 项是 `nums[0]` 到 `nums[i]` 的累加和：

	   arr[i] = nums[0] + nums[1] + ... + nums[i]
   
2. **利用前缀和计算区间和**：

	通过前缀和数组，可以快速计算任意子数组的和：
	
	   子数组和(l, r) = arr[r] - arr[l-1] (如果 l > 0)
	   
	   如果 l = 0，则直接为：
	   arr[r]


**代码中的前缀和实现**
```Python 
import sys
def main():
    n=int(input())
    
    
    sumVal=0
    arr=[]
    #构建区间和数组
    for idx in range(n):
        tmp=int(input())
        sumVal+=tmp
        arr.append(sumVal)
        
    #获取需要计算的下标
    for line in sys.stdin:
        left,right=map(int,line.strip().split())
        if left==0:
            print(arr[right])
        else:
            print(arr[right]-arr[left-1])

main()
```

**前缀和的业务应用场景**

**前缀和**是一种广泛应用于数组和序列处理中的技术，以下是几个常见业务场景：
1. **区间和查询**
	- 典型应用是快速计算任意区间的和，如本题所示。
	- 场景：某个账单系统中，用户需要快速查询任意时间段的总消费。
2. **多维数组的前缀和**
	- 在二维或多维数组中，前缀和可以扩展为快速计算任意子矩阵的和。
	- 场景：统计游戏地图上某个矩形区域内的资源总量。
3. **频繁更新的场景**
	- 当数组数据需要频繁更新时，可以结合差分数组进行优化，避免每次都重建前缀和。
	- 场景：电商平台实时更新的销售数据统计。
4. **子数组和问题**
	- 用于解决子数组和相关问题，比如：- 最大子数组和问题（结合动态规划）。
		- 子数组和为特定值的数量统计。
	- 场景：分析用户行为数据中连续高峰时间段的出现次数。
5. **差分数组**
	- 差分数组是前缀和的逆操作，用于快速构建区间更新操作。
	- 场景：在大规模数据中，需要快速对多个区间的值同时进行加减操作。

### 《代码随想录》数组：开发商购买土地
#### 任务要求
#### 44. 开发商购买土地（第五期模拟笔试）

题目链接：https://www.programmercarl.com/kamacoder/0044.%E5%BC%80%E5%8F%91%E5%95%86%E8%B4%AD%E4%B9%B0%E5%9C%9F%E5%9C%B0.html 

题目建议：希望大家 也做一个自己 对数组专题的总结
文章链接：https://programmercarl.com/%E6%95%B0%E7%BB%84%E6%80%BB%E7%BB%93%E7%AF%87.html
##### 重要知识点
- 二维数组的构造与区间和
- 最小差距的计算
- 优化与注意事项

**二维数组的构造与区间和**

1. **二维数组构造**：- 使用 `grid.append(tmp)` 逐行存储输入数据，构造二维数组。
2. **水平和竖直区间和**：
	- 水平区间和：`horArr[i] = sum(grid[i])`，表示第 `i` 行的总和。
	- 竖直区间和：通过遍历每列累加元素，存储为 `verArr`。

**最小差距的计算**

1. **差值公式**：
	- 差值计算公式：`sum(row_arr) - 2 * horizontalCut`，避免重复计算，快速获得两个区域的差值。
2. **绝对值处理**：
	- 使用 `abs` 确保差值为正，找到最小绝对差距。
3. **水平和竖直最小差距**: 
	- 遍历行（或列），累加当前切割区域和，实时更新最小差距。

```Python 
def main():
    n,m = map(int, input().split())
    
    grid=[]#二维矩阵 
    res=float('inf')#最小差距
    
    #输入二维矩阵的值
    for _ in range(n):
        tmp=list(map(int,input().strip().split()))
        grid.append(tmp)
    
    #构造水平方向区间和
    horArr=[]
    for i in range(0,n):#遍历行
        horArr.append(sum(grid[i]))
        
    #构造竖直方向区间和
    verArr=[]
    for i in range(0,m):#遍历列
        tmp=0
        for j in range(0,n):#遍历行
            tmp+=grid[j][i]
        verArr.append(tmp)
    
    #找到水平最小差距
    horCut=0
    for i in range(n):
        horCut+=horArr[i]
        res=min(res,abs(sum(horArr)-2*horCut))
    
    #找到竖直最小差距
    verCut=0
    for j in range(m):
        verCut+=verArr[j]
        res=min(res,abs(sum(verArr)-2*verCut))
    print(res)
    
main()
```

**优化与注意事项**
- 简化数据构造，减少不必要的嵌套操作。
- 利用前缀和和公式优化，提升效率。