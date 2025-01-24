# 代码随想录
## 贪心算法
### [《代码随想录》贪心算法：合并区间](https://notes.kamacoder.com/questions/502057)
#### 任务要求

#### 56. 合并区间

本题也是重叠区间问题，如果昨天三道都吸收的话，本题就容易理解了。

https://programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html


##### 重要知识点

- 解题思路
- 代码实现


**解题思路**

做了前两道（#435.无重叠区间 和 #452.用最少数量的箭引爆气球）题目之后，这道题还是很简单的。

1. 将数组中的元素按照左区间元素大小进行排序；
2. 遍历数组，若前后元素出现重合，进行合并；否则，加入结果数组。



**代码实现**

30mins写的版本：

```Python 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #1.按照左区间将数组内的元素进行排序
        #2.从左往右遍历集合中的元素，若当前元素左区间<=前一个元素右区间时，进行合并
        #Q:怎么合并?
        intervals.sort(key=lambda x:x[0])
        result=[]
        size=len(intervals)
        idx=0
        for idx in range(0,size):
            if result and intervals[idx][0]<=result[-1][1]:
                left=min(intervals[idx][0],result[-1][0])
                right=max(intervals[idx][1],result[-1][1])
                result[-1]=[left,right]
            else:
                result.append(intervals[idx])
        return result
```

存在的问题：
1. ```left=min(intervals[idx][0],result[-1][0])```多余，因为整个数组已经按照左区间进行排序了；
2. 对应的，在区间合并时只需要更新右区间即可。

**优化后的代码**

```Python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result=[]
        size=len(intervals)
        idx=0
        for idx in range(0,size):
            if result and intervals[idx][0]<=result[-1][1]:
                right=max(intervals[idx][1],result[-1][1])
                result[-1][1]=right
            else:
                result.append(intervals[idx])
        return result
```

### [《代码随想录》贪心算法：单调递增的数字](https://notes.kamacoder.com/questions/502058)
#### 任务要求

#### 738.单调递增的数字

https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html


##### 重要知识点

- 解题思路
- 代码实现




**解题思路**

本题暴力思路很好想到，利用一个函数来判断单调递增性，然后逐一递减，但是会超时。


贪心思路的话，倒也不难。将数字转换成字符串，然后从前往后遍历数组，当前一个元素大于后一个元素时，前一个元素值“-1”，后一个元素变成“9”。



**代码**

**30mins写的代码，❌的**
```Python 
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        #从右往左遍历，当前一个元素比后一个元素大时候
        num=list(str(n))
        for idx in range(len(num)-1,0,-1):
            if int(num[idx])<int(num[idx-1]):#非递增
                num[idx]="9"
                num[idx-1]=str(int(num[idx-1])-1)
        return int("".join(num))
```

为什么错：

```num[idx]="9"```错误出在这行代码，应该将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质

**正确的代码**
```Python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        #从右往左遍历，当前一个元素比后一个元素大时候
        num=list(str(n))
        for idx in range(len(num)-1,0,-1):
            if int(num[idx])<int(num[idx-1]):#非递增
                num[idx-1]=str(int(num[idx-1])-1)
                for j in range(idx,len(num)):
                    num[j]="9"
        return int("".join(num))
```
