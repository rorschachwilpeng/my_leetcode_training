# 代码随想录
## 贪心算法
### [《代码随想录》贪心算法：分发饼干](https://notes.kamacoder.com/questions/502042)
#### 任务要求

#### 455.分发饼干


https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html


##### 重要知识点
- 解题思路

**解题思路**

利用双指针+局部最优（小饼干优先）。

虽然双指针实现代码比代码随想录的版本复杂一些，但是更方便我自己理解。


**代码**

```
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #将两个数组都进行增序排序
        #从左到右分配，尽量将最小的饼干分给胃口最小的孩子
        #利用双指针，最后直接返回指向胃口指针的值即可
        
        g=sorted(g)
        s=sorted(s)
        #双指针
        child=0
        bis=0

        while bis<len(s) and child<len(g):
            if s[bis]>=g[child]:#可以分配饼干
                child+=1#将当前饼干分配给当前的孩子
                bis+=1#遍历下一块饼干
            else:#遍历下一个饼干，直到饼干大小足以分配给孩子
                bis+=1

        return child#返回满足了多少个孩子
```
### [《代码随想录》贪心算法：摆动序列](https://notes.kamacoder.com/questions/502043)
#### 任务要求

#### 376. 摆动序列


https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html


##### 重要知识点

- 解题思路
- 三种特殊情况

**解题思路**

局部最优：减去每个单调坡上的节点，即可得到全局最优 --> 最大子序列的长度。

**三种特殊情况**

- 上下坡中间有平坡

![截屏2025-01-20 12.15.23.png](http://cdn.notes.kamacoder.com/2b05b71e-0b84-4f8e-8653-6e6fbdd53d43.png) 

解决方案：对于平坡上的元素，全部删掉左边的元素，只保留最右边的节点。在代码中对应的部分是：```if (preDiff<=0 and curDiff>0) or (preDiff>=0 and curDiff<0)```中的"="


- 首尾元素
![截屏2025-01-20 12.15.30.png](http://cdn.notes.kamacoder.com/fc69ccde-6aaa-4805-aa93-47b80307b61a.png)

在首元素之前造一个平坡，相当于虚拟头节点，在代码中对应 --> ```preDiff=0``` : 因为平坡，所以没有差值，所以为0。



- 单调坡中间有平坡

![截屏2025-01-20 12.15.39.png](http://cdn.notes.kamacoder.com/04c47f93-04cb-460b-a035-8c95c6e8afe8.png) 


只当单调性发生变化的时候才更新preDiff即可，在代码中对应为将```preDiff=curDiff```的更新放在了判断条件中，而不是每次遍历都会更新。


```
if(preDiff<=0 and curDiff>0) or (preDiff>=0 and curDiff<0):
                result+=1
                preDiff=curDiff
```



**代码**

```
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #贪心思路：
        #减去每个局部单调坡中多余的元素，就能得到全局最优，即最长子序列的长度
        #但是需要注意的情况
            #1.上下坡有平坡 --> 统一减去左边的元素 --> 判断条件里定义
            #2.首尾元素 --> 造一个平坡，并且将result初始化为1
            #3.单调坡中间有平坡 --> 只在单调性发生变化时更新preDirff
        preDiff=0#造一个平坡
        result=1

        for i in range(0,len(nums)-1):
            curDiff=nums[i+1]-nums[i]
            
            if(preDiff<=0 and curDiff>0) or (preDiff>=0 and curDiff<0):
                result+=1
                preDiff=curDiff

        return result
```
### [《代码随想录》贪心算法：最大子序和](https://notes.kamacoder.com/questions/502044)
#### 任务要求

#### 53. 最大子序和


https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html


##### 重要知识点

- 解题思路

**解题思路**

只要连续和为负数，立刻重置。


**代码**

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=float('-inf')
        tmp=0
        for idx in range(len(nums)):
            tmp+=nums[idx]
            if tmp>result:
                result=tmp
            if tmp<=0:
                tmp=0
        return result
```
