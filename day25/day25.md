# 代码随想录
## 回溯算法
### [《代码随想录》回溯算法：递增子序列](https://notes.kamacoder.com/questions/502033)
#### 任务要求

#### 491.递增子序列


本题和大家刚做过的 90.子集II 非常像，但又很不一样，很容易掉坑里。 

https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html  

视频讲解：https://www.bilibili.com/video/BV1EG4y1h78v


##### 重要知识点
- 利用哈希表进行去重 


**利用哈希表进行去重**

- 层级去重逻辑
    -  在回溯树的 **每一层**（同一层的多个分支）中，需要避免选择相同的元素。为此，使用 `used` 数组标记在当前层已经访问过的元素。
	- 关键在于理解：**`used` 的作用范围仅限于当前层**，无需跨层考虑。
	- 这其实和BFS（层序遍历）中利用```level```来记录每一层的节点值非常相似。

- 路径递增性
	- 如果当前选择的元素比路径中最后一个元素小，直接剪枝。这是对递增性质的核心要求。




**代码**

```
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #我想知道利用当前元素和上一个元素的比较这个解法相比其他解法有什么优势？
        result=[]
        def back_tracking(startIdx,path):
            if len(path)>1:
                result.append(path[:])
            
            #递减性质判断
            used=[0]*201
            for i in range(startIdx,len(nums)):
                if (path and nums[i]<path[-1]) or used[nums[i]+100]==1:#如果当前元素小于路径中的最近元素/元素已经用过了 -- 跳过
                    continue
                path.append(nums[i])
                used[nums[i]+100]=1
                back_tracking(i+1,path)
                path.pop()
            
        back_tracking(0,[])
        return result
```
### [《代码随想录》回溯算法：全排列](https://notes.kamacoder.com/questions/502034)
#### 任务要求

#### 46.全排列

本题重点感受一下，排列问题 与 组合问题，组合总和，子集问题的区别。 为什么排列问题不用 startIndex 
https://programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html    
视频讲解：https://www.bilibili.com/video/BV19v4y1S79W


##### 重要知识点

- 排列和组合问题的区别
- 这次又该怎么去重？


**排列和组合问题的区别**

在组合问题中，例如路径 "[1,2]" 和 "[2,1]" 其实是同一个路径。但是在排列问题中，这两个路径代表两个答案。因此我们需要记录下不同顺序的结果，所以在树层遍历中每次都是从第一个元素开始遍历，因此在排列问题中我们不需要startIdx。


**这次又该怎么去重？**

虽然需要记录下元素不同的排列情况，但是我们不能使用重复的元素，这一点题目中也已经提到了。所以我们需要用一个used数组来进行**树枝去重**，即同一路径中用过的元素不能再用了。

**代码**

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        size=len(nums)
        used=[False]*size
        def backTracking(path):
            if len(path)==size:
                result.append(path[:])
                return
            for i in range(0,size):
                if used[i]==True:
                    continue
                path.append(nums[i])
                used[i]=True
                backTracking(path)
                used[i]=False
                path.pop()
        backTracking([])
        return result
```
### [《代码随想录》回溯算法：全排列II](https://notes.kamacoder.com/questions/502035)
#### 任务要求

#### 47.全排列 II

本题 就是我们讲过的 40.组合总和II 去重逻辑 和 46.全排列 的结合，可以先自己做一下，然后重点看一下 文章中 我讲的拓展内容： used[i - 1] == true 也行，used[i - 1] == false 也行 

https://programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html      
 
视频讲解：https://www.bilibili.com/video/BV1R84y1i7Tm


##### 重要知识点

- 排列+去重


**排列+去重**

本题就是在“全排列”的基础上加上树层去重（排序+used数组）

**代码**

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #排列+去重
        result=[]
        nums=sorted(nums)
        size=len(nums)
        used=[False]*size

        def backTracking(path):
            if len(path)==size:
                result.append(path[:])
            
            for i in range(0,size):
                if used[i]:
                    continue
                if (i>0 and nums[i]==nums[i-1]) and used[i-1]==False:
                    continue
                path.append(nums[i])
                used[i]=True
                backTracking(path)
                used[i]=False
                path.pop()

        backTracking([])
        return result
```
### [《代码随想录》回溯算法：重新安排行程](https://notes.kamacoder.com/questions/502037)
#### 任务要求

#### 332. 
    重新安排行程（可跳过）

本题很难，一刷的录友刷起来 比较费力，可以留给二刷的时候再去解决。
本题没有录制视频，当初录视频是按照 《代码随想录》出版的目录来的，当时没有这道题所以就没有录制。
https://programmercarl.com/0332.%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E8%A1%8C%E7%A8%8B.html


##### 重要知识点

- 困难题不难
- 本题难点
- 用什么数据结构来存储航班信息？
- 怎么避免死循环？
- 递归中的终止条件是？



**困难题不难**

不能在心态上被困难题吓到，困难题其实也不过就是两道中等题加在一起，中等题其实也不过就是两道简单题加在一起。都是一步一步分析做出来了。


**本题难点**

本题是DFS的思路来做，重点难点包括：

1. 用什么数据结构来存储航班信息？
2. 怎么避免死循环？
3. 递归中的终止条件是？
4. 怎么递归？这次递归需要返回值吗？



**用什么数据结构来存储航班信息？**

字典是最优选项，因为需要存储的出发地和目的地都是string数据类型，且可能存在一对多的映射关系。所以可以利用字典，key是出发地，value是目的地（可能存在多个）数组。



**怎么避免死循环？**

每次递归过程中，一旦确定下一个目的地后，将其从对应的航班信息中弹出，避免重复遍历造成死循环。


**递归中的终止条件是？**

这点我的理解有点模糊，代码随想录上说的是“回溯遍历的过程中，遇到的机场个数，如果达到了（航班数量+1），那么我们就找到了一个行程，把所有航班串在一起了。”

但是在代码实现中，没有看到具体步骤。

我自己的理解是在树形结构中找到一条能够覆盖所有航班信息（节点）路径的通路。

- CHATGPT给的解释：

```
终止条件的隐式设计

递归没有显式的 `return` 语句，因为路径的记录通过全局变量 `result` 实现，而递归终止是通过以下逻辑完成的：
1. 没有更多的目的地可以访问时，当前递归自然退出。
2. 通过回溯，依次将每个节点添加到 `result` 中，最终形成完整的行程。
```


**怎么递归？这次递归需要返回值吗？**

不需要返回值，因为我们目标返回的数组可以通过维护全局变量完成。



**代码**

```
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj={}#字典，用于存储航班信息；key-出发地,val:目的地
        
        tickets.sort(key=lambda x:x[1])#将航班信息按照字母顺序重新排序

        for u,v in tickets:
            if u in self.adj:
                self.adj[u].append(v)
            else:
                self.adj[u]=[v]

        result=[]
        def dfs(ori):#入参 --> 出发地
            while ori in self.adj and self.adj[ori]:
                des=self.adj[ori][0]#找到下一个目的地
                self.adj[ori].pop(0)#弹出目的地，确保不重复遍历
                dfs(des)
            result.append(ori)
        dfs("JFK")
        return result[::-1]
```