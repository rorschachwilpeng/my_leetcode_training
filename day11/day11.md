# 代码随想录
## 栈与队列
### 《代码随想录》栈与队列：逆波兰表达式求值
#### 任务要求
#### 150.逆波兰表达式求值

本题不难，但第一次做的话，会很难想到，所以先看视频，了解思路再去做题 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html

##### 重要知识点
- 实现思路
- 除法实现注意点

**实现思路**

利用栈来实现，每遇到数字就将元素压入栈。每遇到运算符号就将值弹出进行计算。

**除法实现注意点**

题目中明确了要向零截断，实现时候注意下。

```Python 
from operator import add,sub,mul

class Solution:
    def plus(self,stack):
        val1=stack.pop()
        val2=stack.pop()
        return val1+val2
        
    def minus(self,stack):
        val1=stack.pop()
        val2=stack.pop()
        return val2-val1

    def multiple(self,stack):
        val1=stack.pop()
        val2=stack.pop()
        return val1*val2

    def divide(self,stack):
        val1=stack.pop()
        val2=stack.pop()
        return int(val2/val1) if val1*val2>0 else -(abs(val2)//abs(val1))
        
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:
            #将数字压入栈
            #stack.append(item)
            #遇到运算符号则将元素出栈，并进行对应计算
            if item=="+":
                stack.append(self.plus(stack))
            elif item=="-":
                stack.append(self.minus(stack))
            elif item=="*":
                stack.append(self.multiple(stack))
            elif item=="/":
                stack.append(self.divide(stack))
            else:
                stack.append(int(item))
        return stack.pop()
```

### 《代码随想录》栈与队列：滑动窗口最大值
#### 任务要求
#### 239. 滑动窗口最大值 （有点难度，可能代码写不出来，但一刷至少需要理解思路）


之前讲的都是栈的应用，这次该是队列的应用了。

本题算比较有难度的，需要自己去构造单调队列，建议先看视频来理解。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html

##### 重要知识点
- 单调队列的维护
- 如何保证弹出的元素是当前窗口的最大值？
- 滑动窗口的逻辑

1. **单调队列的维护**：
	- 单调队列是一种特殊的双端队列（deque），其维护队列内的元素按大小递减。
	- 队列中存储的是当前窗口内可能成为最大值的元素，任何比当前加入元素小的队列尾部元素都会被弹出，确保队列中的元素始终是按递减顺序排列的。
	- 每次移动窗口时：
		- **右侧扩展**：加入新的元素时，将比其小的队列尾部元素移除。
		- **左侧收缩**：移出窗口左边界时，如果该元素是队列头部（即最大值），则将其从队列头部移除。
2. **如何保证弹出的元素是当前窗口的最大值？**
	- 单调队列的头部始终存储的是当前窗口内的最大值。
	- 每次窗口移动时，直接取队列头部的值即可。
	- 由于队列按递减顺序排列，新的元素加入不会破坏最大值的位置，保证了最大值始终是队列头部。
3. **滑动窗口的逻辑**：
	- 在初始化时，将窗口的前 `k` 个元素加入单调队列。
	- 对于每次窗口的右移：
		- **移除左边界的元素**：调用 `pop()` 方法，从队列头部移除窗口左边界超出的值。
		- **加入右边界的新元素**：调用 `push()` 方法，将新元素加入队列，并移除所有小于新元素的队列尾部元素。
	- 每次窗口移动后，队列头部的元素就是当前窗口的最大值。


```Python 
from collections import deque

class MyQueue:
    def __init__(self):
        self.que=deque()

    def push(self,item):
        #卷走比当前加入元素小的元素
        while self.que and self.que[-1]<item:
            self.que.pop()
        self.que.append(item)
    
    def pop(self,target):
        if self.que and self.que[0]==target:
            self.que.popleft()

    def getMax(self):
        return self.que[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #滑动窗口每次移动时，要考虑左边和右边
        que=MyQueue()
        size=len(nums)
        res=[]
        for i in range(k):#先将前k个值加入单调队列
            que.push(nums[i])
        res.append(que.getMax())
        for i in range(k,size):
            que.pop(nums[i-k])#窗口左边界右移
            que.push(nums[i])#窗口右边界右移
            res.append(que.getMax())
        return res
```
