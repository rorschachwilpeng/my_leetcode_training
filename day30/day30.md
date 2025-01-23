# 代码随想录
## 贪心算法
### [《代码随想录》贪心算法：用最少数量的箭引爆气球](https://notes.kamacoder.com/questions/502054)
#### 任务要求

#### 452. 用最少数量的箭引爆气球


https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html

##### 重要知识点
- 贪心思想
- 代码实现

**贪心思想**

贪心的思路非常直观，尽可能一次多射气球就行。不妨先将数组元素按照元组中第一个元素大小进行排序，然后遍历区间元素，比较当前元素和之前元素的区间关系。

若当前区间的左区间 <= 上一个区间的右区间时，代表两个区间有重合，用一支箭就能解决。


**代码实现**

具体代码实现和思路里面的逻辑还不太一样，因为我们最后返回的是箭的数量，而且我们希望其尽可能地小，所以我们只在排序后的两个相邻区间不挨在一起的时候才增加箭数，对于挨在一起的区间需要更新最小公共右区间。


**代码**
```Python 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        result=1
        for i in range(1,len(points)):
            #只有不挨着的时候才更新箭数
            if points[i][0]>points[i-1][1]:
                result+=1
            
            else:#两个气球挨着
                points[i][1]=min(points[i][1],points[i-1][1])#更新最小公共右边界
        
        return result
```
### [《代码随想录》贪心算法：无重叠区间](https://notes.kamacoder.com/questions/502055)
#### 任务要求

#### 435. 无重叠区间


https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html

##### 重要知识点
- 贪心思想


**贪心思想**

本题和”#452.用最少数量的箭引爆气球“非常相似，首先按照左边界元素将元素进行排序。然后遍历进行区间判断，若当前元素的左边界小于上一个元素的右边界，即存在重合，当前元素需要去除。而我们只需要将当前元素的右边界更新为两个区间右边界的最小值，同时更新最终返回的去除元素数即可。


**代码实现**

具体代码实现和思路里面的逻辑还不太一样，因为我们最后返回的是箭的数量，而且我们希望其尽可能地小，所以我们只在排序后的两个相邻区间不挨在一起的时候才增加箭数，对于挨在一起的区间需要更新最小公共右区间。


**代码**
```Python 
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result=0
        intervals.sort(key=lambda x:x[0])
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1])
                result+=1

        return result
```
### [《代码随想录》贪心算法：划分字母区间](https://notes.kamacoder.com/questions/502056)
#### 任务要求

#### 763.划分字母区间


https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html   


##### 重要知识点

- 解题思路

**解题思路**

本题没有怎么用到贪心思想

1. 通过遍历，记录下每个元素在数组中所出现的**最远位置**；
2. 再遍历一次，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等 --> 找到分割点。



**代码**
```Python 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #首先记录每个元素出现的最远位置
        dic={}
        for idx,val in enumerate(s):
            dic[val]=idx
        
        result=[]
        end=0
        start=0
        for idx,val in enumerate(s):
            end=max(end,dic[val])
            if end==idx:
                result.append(end-start+1)
                start=idx+1
        return result
```
