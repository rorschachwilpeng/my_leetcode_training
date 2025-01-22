# 代码随想录
## 贪心算法
### [《代码随想录》贪心算法：加油站](https://notes.kamacoder.com/questions/502049)
#### 任务要求

#### 134. 加油站

本题有点难度，不太好想，推荐大家熟悉一下方法二 
https://programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html


##### 重要知识点
- 解题思路

**解题思路**

1. 计算每个油站的剩余量```gas[i]-cost[i]```。
2. 累加剩余量，当剩余量<0时代表如果选择[0,i]区间的元素作为起点的话，一定无法抵达终点。所以将遍历索引移动至 i+1
3. 遍历结束后，如果totSum<0，代表着总油量不够总路程，那么一定无法抵达；
4. 否则，返回维护的起点索引



```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum=0
        totSum=0
        start=0

        for i in range(len(gas)):
            curSum+=(gas[i]-cost[i])
            totSum+=(gas[i]-cost[i])
            if curSum<0:
                start=i+1
                curSum=0#重置curSum
        
        if totSum<0:return -1
        return start
```
### [《代码随想录》贪心算法：分发糖果](https://notes.kamacoder.com/questions/502050)
#### 任务要求

#### 135. 分发糖果

本题涉及到一个思想，就是想处理好一边再处理另一边，不要两边想着一起兼顾，后面还会有题目用到这个思路 
https://programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html

##### 重要知识点
- 贪心，贪心，贪心

**贪心，贪心，贪心**

本题无法通过一次遍历解决问题，因为在单次遍历中只能顾及一侧，而会忽略另一侧的评分需求。因此需要两次遍历：
1. 第一次从左向右遍历：
	- 确保每个孩子的糖果数至少比左侧评分低的孩子多。
	- 当 `ratings[i] > ratings[i-1]` 时，分配的糖果数应为 `result[i] = result[i-1] + 1`。
2. 第二次从右向左遍历：
	- 确保每个孩子的糖果数至少比右侧评分低的孩子多。
	- 当 `ratings[i] > ratings[i+1]` 时，更新为 `result[i] = max(result[i], result[i+1] + 1)`，从而在满足右侧评分需求的同时，不破坏左侧的分配结果。

通过两次遍历，确保每个孩子的糖果分配既符合左侧要求，也满足右侧需求，实现最优分配。


```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        size=len(ratings)
        result=[1]*size

        #从左往右遍历
        for idx in range(1,size):
            if ratings[idx]>ratings[idx-1]:
                result[idx]=result[idx-1]+1

        #从右往左遍历
        for idx in range(size-2,-1,-1):
            if ratings[idx]>ratings[idx+1]:
                result[idx]=max(result[idx],result[idx+1]+1)

        return sum(result)
```
### [《代码随想录》贪心算法：柠檬水找零](https://notes.kamacoder.com/questions/502051)
#### 任务要求

#### 860.柠檬水找零


本题看上好像挺难，其实很简单，大家先尝试自己做一做。
https://programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html

##### 重要知识点
- 解题思路

**解题思路**

模拟题 + 贪心思路。

本题贪心思路体现在尽可能地少用5美元找零，因为5美元即可以找零10美元，也可以找零20美元，用处更大。

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #模拟题
        #当用户支付5美元时-->不用找零
        #当用户支付10美元时-->找零5块
        #当用户支付20美元时-->5+5+5/10+5

        #用字典作为数据存储容器
        dic={'5':0,
             '10':0,
             '20':0}
        
        for item in bills:
            if item==5:
                #不需要找零，直接加入字典
                dic['5']+=1
            elif item==10:
                if dic['5']>0:
                    dic['5']-=1
                    dic['10']+=1
                else:#如果无法找零，返回False
                    return False   
            elif item==20:
                #优先用10美元找零，因为5美元的用处更大
                if dic['10']>0 and dic['5']>0:
                    dic['10']-=1
                    dic['5']-=1
                    dic['20']+=1
                elif dic['10']==0 and dic['5']>=3:
                    dic['5']-=3
                    dic['20']+=3
                else:
                    return False

        return True
```
### [《代码随想录》贪心算法：根据身高重建队列](https://notes.kamacoder.com/questions/502052)
#### 任务要求

#### 406.根据身高重建队列


本题有点难度，和分发糖果类似，不要两头兼顾，处理好一边再处理另一边。 
https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html

##### 重要知识点
- 解题思路

**解题思路**

![截屏2025-01-22 20.41.10.png](http://cdn.notes.kamacoder.com/dfed3de5-a9e4-4488-91c3-2b2abb6fbcc3.png) 

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        que=[]

        for p in people:
            que.insert(p[1], p)
        return que
```
