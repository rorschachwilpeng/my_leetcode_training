# 代码随想录
## 单调栈
### [《代码随想录》单调栈：每日温度](https://notes.kamacoder.com/questions/502108)
#### 任务要求
#### 115.不同的子序列


但相对于刚讲过 392.判断子序列，本题 就有难度了 ，感受一下本题和  392.判断子序列 的区别。 

https://programmercarl.com/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.html

##### 重要知识点

- 单调栈应用场景
- 单调栈的维护方式

**单调栈应用场景**

在解决涉及 **单调性** 的问题时，单调栈是一种强有力的工具。它能够帮助我们高效地找到元素间的 **递增** 或 **递减** 关系，广泛应用于 **下一个更大元素**、**柱状图最大矩形**、**接雨水** 等经典问题。

**单调栈的维护方式**

我们从左到右遍历整个数组，每次遇到新元素时，与栈顶元素进行比较，可以分为三种情况：


1. **当前元素 > 栈顶元素**
	- 说明当前元素找到了比栈顶元素更大的值。
	- 依次弹出栈顶元素，直到栈为空，或者栈顶元素小于当前元素。
	- 将当前元素入栈。

2. **当前元素 == 栈顶元素**
	- 由于相同的元素不影响单调性，一般可以直接入栈，具体根据题目需求处理。

3. **当前元素 < 栈顶元素**
	- 直接将当前元素入栈，保证栈的单调递增性不被破坏。


**代码**
```Python 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[0]#单调栈
        for i in range(1, len(temperatures)):
            #情况一和情况二
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            #情况三
            else:
                while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return answer
```
### [《代码随想录》单调栈：下一个更大元素I](https://notes.kamacoder.com/questions/502109)
#### 任务要求
#### 496.下一个更大元素 I


本题和 739. 每日温度 看似差不多，其实 有加了点难度。

https://programmercarl.com/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.html

##### 重要知识点

- 解题思路

**解题思路**

在“每日温度”的基础上做了一次哈希映射嵌套，**抄了一遍答案**




**代码**
```Python 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*len(nums1)
        stack=[0]
        for i in range(1, len(nums2)):
            #情况一和情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index=nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()
                stack.append(i)
        return result
```
### [《代码随想录》单调栈：下一个更大元素II](https://notes.kamacoder.com/questions/502110)
#### 任务要求
#### 503.下一个更大元素II


这道题和 739. 每日温度 几乎如出一辙，可以自己尝试做一做

https://programmercarl.com/0503.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0II.html

##### 重要知识点

- 解题思路

**解题思路**

在“每日温度”的基础上加入了循环遍历的要求。循环遍历可以通过遍历两次数组来实现，或者可以拼接两个数组。第一种方法能节省空间复杂度。


**抄了遍答案**

**代码**
```Python 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size=len(nums)
        stack=[0]
        result=[-1]*size
        #情况一：当前遍历元素 < 栈口元素
        #情况二：当前遍历元素==栈口元素
        #情况三：当前遍历元素 > 栈口元素
        for i in range(size*2):
            idx=i%size
            if nums[idx]<=nums[stack[-1]]:#情况一,二
                stack.append(idx)
            else:#情况三
                while len(stack)!=0 and nums[idx]>nums[stack[-1]]:
                    result[stack[-1]]=nums[idx]
                    stack.pop()
                stack.append(idx)
        return result
```
### [《代码随想录》单调栈：接雨水](https://notes.kamacoder.com/questions/502111)
#### 任务要求
#### 42. 接雨水


接雨水这道题目是 面试中特别高频的一道题，也是单调栈 应用的题目，大家好好做做。

建议是掌握 双指针 和单调栈，因为在面试中 写出单调栈可能 有点难度，但双指针思路更直接一些。

在时间紧张的情况有，能写出双指针法也是不错的，然后可以和面试官在慢慢讨论如何优化。 
https://programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html

##### 重要知识点

- 解题思路
- 单调栈的实现

**解题思路**

很经典的一道题。本题思考过程如下：
1. 如果要求雨水面积，那么我们就需要知道凹槽的面积；
2. 凹槽的定义是：只有当前列的左右两边都存在比当前列大的列时，才存在凹槽；
3. 怎么找凹槽呢？-->找到左右比当前列大的第一个列-->单调栈


**单调栈的实现**

其实和“每日温度”的思路一样，构造一个从栈头向栈尾单调递增的单调栈。从左到右遍历元素，单调栈中存放的是遍历过的元素的索引。逐一比较当前遍历元素和栈口元素的大小关系，不难推导出三种关系：小于，等于，大于。

1. 当前遍历元素 < 栈口元素：将元素索引压入栈即可；
2.  当前遍历元素 == 栈口元素：将栈口元素弹出，压入当前遍历的元素（其实不操作也行，对最终结果没有影响）
3.  当前遍历元素 > 栈口元素：持续弹出栈口元素，直到不符合判断条件为止。因为构造的是一个递增单调栈，所以比弹出的每个栈口元素更大的左边列就是当前遍历列，比栈口元素更大的**右边列**是其栈中下一列。


**代码**
```Python 
class Solution:
    def trap(self, height: List[int]) -> int:
        size=len(height)
        stack=[0]
        result=0
        
        for i in range(1,size):#从左到右遍历
            if height[i]<height[stack[-1]]:#情况一
                stack.append(i)
            elif height[i]==height[stack[-1]]:#情况二
                stack.pop()
                stack.append(i)
            else:#情况三
                while stack and height[i]>height[stack[-1]]:
                    mid_height=height[stack[-1]]
                    stack.pop()
                    if stack:
                        rHeight=height[i]
                        lHeight=height[stack[-1]]
                        h=min(rHeight,lHeight)-mid_height
                        c=i-stack[-1]-1
                        result+=h*c
                stack.append(i)
        return result
```
### [《代码随想录》单调栈：柱状图中最大的矩形](https://notes.kamacoder.com/questions/502112)
#### 任务要求
#### 84. 柱状图中最大的矩形

有了之前单调栈的铺垫，这道题目就不难了。 

https://programmercarl.com/0084.%E6%9F%B1%E7%8A%B6%E5%9B%BE%E4%B8%AD%E6%9C%80%E5%A4%A7%E7%9A%84%E7%9F%A9%E5%BD%A2.html

##### 重要知识点

- 解题思路

**解题思路**

和“接雨水”的思路差不多，只不过这道题变成列单调递减栈。



**代码**
```Python 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #单调栈
        #面积计算方法：对于每个柱子，找到左和右比自身矮的第一个柱子，这两个柱子之间的距离即为宽。柱子自身高度为高。
        #矩形面积=高*宽

        #NOTE:heights需要首尾加0-->避免极端情况(数组本身已经单调递减了)
        heights.insert(0,0)
        heights.append(0)
        stack=[0]
        res=0

        #单调栈 -- 单调递减 -- 从大到小（从栈口到栈体）
        for i in range(len(heights)):
            #情况一&二
            if heights[stack[-1]]<=heights[i]:
                stack.append(i)
            #情况三
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    mid=stack[-1]
                    stack.pop()
                    if stack:
                        left=stack[-1]
                        right=i
                        w=right-left-1#矩形的宽
                        h=heights[mid]
                        res=max(res,h*w)#取全局最大的面积
                stack.append(i)
        return res
```
