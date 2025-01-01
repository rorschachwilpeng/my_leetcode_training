# 代码随想录
## 字符串
### 《代码随想录》字符串：反转字符串
#### 任务要求
### 344.反转字符串


建议： 本题是字符串基础题目，就是考察 reverse 函数的实现，同时也明确一下 平时刷题什么时候用 库函数，什么时候 不用库函数 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html
##### 重要知识点
- 双指针实现

**双指针实现**
和`翻转链表`一样的思路，利用双指针交换元素，直到循环结束为止。


**代码**
```Python 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        size=len(s)
        left,right=0,size-1

        while left<=right:
            tmp=s[left]
            s[left]=s[right]
            s[right]=tmp
            left+=1
            right-=1
        return s
```

### 《代码随想录》字符串：反转字符串II
#### 任务要求
### 541. 反转字符串II


建议：本题又进阶了，自己先去独立做一做，然后在看题解，对代码技巧会有很深的体会。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html

##### 重要知识点
- 思路
- 不同的代码实现

**思路**

这题算模拟题，刚开始做的时候想用*快慢指针*求解，但本题更适合直接用索引切片来操作。

*快慢指针适用的场景*
- 链表处理问题，如寻找中点、判断环形链表。
- 滑动窗口问题，如子数组的动态范围更新。
- 连续性问题，如寻找连续最大子数组。

基于索引切片思路，解题思路如下：
1. 按2k的块划分字符串
2. 对每块：反转前k个字符，拼接 -- 前续部分 、反转部分、后续部分；
3. 拼接所有结果

**不同的代码实现**

自己实现的版本，思路清晰但代码冗余。
```Python 
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        size=len(s)
        blockNum=size//(2*k)#字符串可以划分成几个2k块

        #每次只对一个2k块进行操作
        for i in range(blockNum+1):
            start=2*k*i
            end=min(size,start+k)
            if end<size:#如果正常的话，反转这2k字符中的前k个字符
                before=s[:start]
                reverse=s[start:end][::-1]
                remain =s[end::]
                s=before+reverse+remain

            elif end>=size:#剩余字符小于2k但大于或等于k，反转前k个
                before=s[:start]
                reverse=s[start:size][::-1]
                s=before+reverse
        return s
```

随想录上的优化解法
```Python 
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #双指针
        p=0
        while p<len(s):
            p2=p+k
            s=s[:p]+s[p:p2][::-1]+s[p2:]
            p+=2*k
        return s
```


### 《代码随想录》字符串：替换数字
#### 任务要求
### 卡码网：54.替换数字

建议：对于线性数据结构，填充或者删除，后序处理会高效的多。好好体会一下。

题目链接/文章讲解：[替换数字](https://programmercarl.com/kamacoder/0054.%E6%9B%BF%E6%8D%A2%E6%95%B0%E5%AD%97.html)

##### 重要知识点
- 思路
- 双指针思路

**思路**

遍历字符串各个字符，利用ord内置函数来判断字符是否是数字，并将数字替换成“number”。

```Python 
def main():
    s=str(input())
    l=[]
    for idx,letter in enumerate(s):
        if ord(letter)-ord('a')<0:
            l.append("number")
        else:
            l.append(letter)
    print("".join(l))
main()
```

**双指针思路**

随想录上给出了一个双指针思路，即将数组先扩充至所需大小，然后再**从后向前**进行操作（但Python中的string不可改，所以还是需要额外空间）。这个方法就不再需要创建额外空间了。据说这个思路再很多**数组填充类问题**里都能用上，mark一下。

- *为什么不**从前往后**填充？*

从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素整体向后移动。

- *双指针方法*有两个好处：
1. 不用申请新数组。
2. 从后向前填充元素，避免了从前向后填充元素时，每次添加元素都要将添加元素之后的所有元素向后移动的问题。

