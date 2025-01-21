# 代码随想录
## 贪心算法
### [《代码随想录》贪心算法：买卖股票的最佳时机II](https://notes.kamacoder.com/questions/502045)
#### 任务要求
#### 122.买卖股票的最佳时机II


本题解法很巧妙，本题大家可以先自己思考一下然后再看题解，会有惊喜！ 

https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html

##### 重要知识点

- 巧妙的贪心思路

**巧妙的贪心思路**

将最终利润拆解开，最大的利润就是所有正利润相加起来。


**代码**

```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for idx in range(1,len(prices)):
            result+=max(prices[idx]-prices[idx-1],0)
        return result
```
### [《代码随想录》贪心算法：跳跃游戏](https://notes.kamacoder.com/questions/502046)
#### 任务要求
#### 55. 跳跃游戏


本题如果没接触过，很难想到，所以不要自己憋时间太久，读题思考一会，没思路立刻看题解 

https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html

##### 重要知识点

- 贪心思路


**贪心思路**

只需要考虑所达范围是否能够包括终点位置即可。具体代码实现中，通过维护最大值```cover```来判断是否能够到达最后一个节点。



**代码**
```Python 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover=0
        if len(nums)==1:return True
        i=0
        while i<=cover:
            cover=max(i+nums[i],cover)
            if cover>=len(nums)-1:
                return True
            i+=1
        return False
```

### [《代码随想录》贪心算法：跳跃游戏II](https://notes.kamacoder.com/questions/502047)
#### 任务要求
#### 45.跳跃游戏II


本题同样不容易想出来。贪心就是这样，有的时候 会感觉简单到离谱，有时候，难的不行，主要是不容易想到。

https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html


##### 重要知识点
-  **贪心算法核心**
-  **关键变量**
-  **特殊情况**
-  **复杂度分析**

1. **贪心算法核心**
	- 每次跳跃选择当前覆盖范围内能跳的最远位置，确保跳跃次数最少。

2. **关键变量**
	- `cur_distance`：当前跳跃的覆盖范围。
	- `next_distance`：下一步跳跃的最大覆盖范围。
	- 遍历到 `cur_distance` 时，增加跳跃次数并更新覆盖范围。

3. **特殊情况**
	- 如果数组长度为 1，直接返回 0 次跳跃。

4. **复杂度分析**
	- 时间复杂度：O(n)，每个元素最多访问一次。
	- 空间复杂度：O(1)，仅使用常量空间。


```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        cur_distance=0
        next_distance=0
        ans=0#最大步长
        
        for i in range(len(nums)):
            next_distance=max(nums[i]+i, next_distance)
            if i==cur_distance:#如果遍历到了当前覆盖距离的右边界
                ans+=1
                cur_distance=next_distance
                if next_distance>=len(nums)-1:
                    break
        return ans

```
### [《代码随想录》贪心算法：K次取反后最大化的数组和](https://notes.kamacoder.com/questions/502048)
#### 任务要求

#### 1005.K次取反后最大化的数组和

本题简单一些，估计大家不用想着贪心 ，用自己直觉也会有思路。 
https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html

##### 重要知识点
- 解题思路

**解题思路**

1. 首先将数组按照绝对值大小从大到小倒序排列
2. 遍历数组，将负数改成正数
3. 如果K还没减完，且K的剩余值为奇数（偶数的话相当于负负得正，不需要变化），将绝对值最小的值变换成负数。


```python
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #把负数改成正的
        #1.如果有负数的话，就把负数都改成正的，并且改的时候优先改绝对值最大的，如果k还有剩余的话，走步骤2
        #2.将最小的正数改成负数
        
        nums.sort(key=lambda x:abs(x),reverse=True)
        
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-nums[i]#取反
                k-=1
        
        #如果k还剩的话，且为奇数（偶数的话直接无视）
        if k%2==1:
            nums[-1]=-nums[-1]
        return sum(nums)
```
