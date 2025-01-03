# 代码随想录
## 栈与队列
### 《代码随想录》栈与队列：用栈实现队列
#### 任务要求
#### 232.用栈实现队列


大家可以先看视频，了解一下模拟的过程，然后写代码会轻松很多。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html

##### 重要知识点
- 栈和队列的特性
- 实现需要注意的点

**栈和队列的特性**

- 栈的特性：先进后出（First In Last Out/ FILO）;
- 对列的特性：先进先出（First In First Out/ FIFO）。

**实现需要注意的点**
- 利用两个栈即可模拟对列的特性
	- 一个栈负责入队，另一个栈负责出对
	- 当负责出队的栈为空时，将入队栈的元素全部压入出队栈
	- **peek**函数实现需要复用**pop**函数

**代码**
```Python 
class MyQueue:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x: int) -> None:
        self.stack_in.append(x)
       
    def pop(self) -> int:
        #先将stack_in清空，并将所有元素压入stack_out
        #然后清空stack_out
        if self.empty():
            return None
        
        if self.stack_out:#如果out还有元素
            return self.stack_out.pop()
        else:#out没有元素
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int:
        val=self.pop()
        self.stack_out.append(val)
        return val


    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
       


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

### 《代码随想录》栈与队列：用队列实现栈
#### 任务要求
### 225. 用队列实现栈


可能大家惯性思维，以为还要两个队列来模拟栈，其实只用一个队列就可以模拟栈了。 

建议大家掌握一个队列的方法，更简单一些，可以先看视频讲解

题目链接/文章讲解/视频讲解：https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html

##### 重要知识点
- 用一个队列实现的方式

**用一个队列实现的方式**
- 也可以用两个队列来实现栈，其中一个队列用作备份，另一个用作出入元素。
- 如果利用一个队列来实现
	- 对于不需要出栈的元素，先弹出，再压入。直到最终需要返回的元素
	- **top**函数实现可以复用**pop**函数

**代码**
```Python 
class MyStack:
    def __init__(self):
        self.que=deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for _ in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        val=self.pop()
        self.que.append(val)
        return val

    def empty(self) -> bool:
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### 《代码随想录》栈与队列：有效的括号
#### 任务要求
#### 20. 有效的括号

讲完了栈实现队列，队列实现栈，接下来就是栈的经典应用了。 

大家先自己思考一下 有哪些不匹配的场景，在看视频 我讲的都有哪些场景，落实到代码其实就容易很多了。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html

##### 重要知识点
- 基于栈的实现思路
- 不匹配情况要考虑周全

**基于栈的实现思路**

巧用栈的属性，先进后出来做匹配判断。首先逐个遍历字符串中的字符，当识别到左括号就将对应右括号压入栈，当识别到右括号和栈中末尾元素进行判断。若栈在遍历结束后为空，说明所有括号都成功匹配，

**不匹配情况要考虑周全**

一共有三种不匹配情况：
- 已经遍历完了字符串，但是栈不为空，说明有左括号没有找到对应右括号；
- 遍历字符串匹配过程中，发现栈中没有要匹配的字符；
-  遍历字符串匹配的过程中，发现栈已经空了，说明右括号多了。

**代码**
```Python 
from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2==1:return False#奇数个字符无法匹配
        
        for letter in s:
            if letter=='(':
                stack.append(')')
            elif letter=='{':
                stack.append('}')
            elif letter=='[':
                stack.append(']')
            
            elif not stack or stack[-1]!=letter:#情况三和二
                return False
            else:
                stack.pop()
        return not stack#情况一
```

### 《代码随想录》栈与队列：删除字符串中的所有相邻重复项
#### 任务要求
#### 1047. 删除字符串中的所有相邻重复项

栈的经典应用。 

要知道栈为什么适合做这种类似于爱消除的操作，因为栈帮助我们记录了 遍历数组当前元素时候，前一个元素是什么。

题目链接/文章讲解/视频讲解：https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html   

##### 重要知识点
- 天天消消乐

**天天消消乐**

没啥好说的，但是有个衍生问题：“什么时候用栈合适？什么时候用队列合适？”


```Python 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for letter in s:
            if stack and stack[-1]==letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
```

