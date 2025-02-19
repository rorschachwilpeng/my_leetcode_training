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
``