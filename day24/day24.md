# 代码随想录

## 回溯算法
### [《代码随想录》回溯算法：复原IP地址](https://notes.kamacoder.com/questions/502030)
#### 任务要求

#### 93.复原IP地址


本期本来是很有难度的，不过 大家做完 分割回文串 之后，本题就容易很多了 

题目链接/文章讲解：https://programmercarl.com/0093.%E5%A4%8D%E5%8E%9FIP%E5%9C%B0%E5%9D%80.html   
视频讲解：https://www.bilibili.com/video/BV1XP4y1U73i/


##### 重要知识点
- 解题思路
- 本题难点

**解题思路**

本题和“切割回文串”很像的，都是将切割问题抽象成组合问题来处理。


**本题难点**

1. 怎么判断IP地址有效性
2. 剪枝时发现的一个知识点

**怎么判断IP地址有效性**




**剪枝时发现的一个知识点**

本题可以通过判断IP地址长度来进行剪枝，如果当前路径中的元素数量已经大于4，那树层结构上就没有必要继续遍历了。所以我们在单次遍历逻辑中，一旦检测到路径元素数量已经等于4，可以直接结束当前树层循环。

发现的一个知识点是：```break```的话，会终止当前for循环，也就是结束当层树层遍历。如果是```continue```的话，只是终止当前分支的遍历，同一树层的节点仍然会被继续遍历。这一点值得好好体会一下。

```python
for i in range(startIdx,len(s)):
                #单次遍历逻辑
                subStr=s[startIdx:i+1]
                if self.isValid(subStr):
                    if len(path)==4:
                        break
                    path.append(subStr)
                    backTracking(i+1,path)
                    path.pop()
```


**代码**

```
class Solution:
    def isValid(self,subS):
        if len(subS)>1 and subS[0]=="0":
            return False
        elif 0<=int(subS)<=255:
            return True
    def restoreIpAddresses(self, s: str) -> List[str]:
        #有效IP地址：
        #1.前导不为0
        #2.每个整数位于0-255之间组成
        result=[]
    
        #还是切割问题
        def backTracking(startIdx,path):#入参
            if startIdx==len(s) and len(path)==4:
                result.append(".".join(path[:]))
                return
                
            if startIdx==len(s):#终止条件
                return

            for i in range(startIdx,len(s)):
                #单次遍历逻辑
                subStr=s[startIdx:i+1]
                if self.isValid(subStr):
                    if len(path)==4:
                        break
                    path.append(subStr)
                    backTracking(i+1,path)
                    path.pop()
                
        backTracking(0,[])
        return result
```
### [《代码随想录》回溯算法：子集](https://notes.kamacoder.com/questions/502031)
#### 任务要求

#### 78.子集


子集问题，就是收集树形结构中，每一个节点的结果。 整体代码其实和 回溯模板都是差不多的。 

题目链接/文章讲解：https://programmercarl.com/0078.%E5%AD%90%E9%9B%86.html   
视频讲解：https://www.bilibili.com/video/BV1U84y1q7Ci


##### 重要知识点
- 子集问题

**子集问题**

子集问题相比组合/切割问题来说比较简单。从树形结构的角度出发，我们只需要保存树中所有的节点即可，而组合和切割问题都是需要收集树形结构中的叶子节点。因此，这道子集问题就是纯纯模版题，也不需要剪枝，因为我们求的就是所有节点 


**代码**

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #子集问题--其实是将树形结构中的每个节点都记录下来
        result=[]
        def backTracking(startIdx,path):#入参
            if startIdx>len(nums):#终止条件
                return
            result.append(path[:])

            #单次遍历条件
            for i in range(startIdx,len(nums)):
                path.append(nums[i])
                backTracking(i+1,path)
                path.pop()
        backTracking(0,[])
        return result
```
### [《代码随想录》回溯算法：子集II](https://notes.kamacoder.com/questions/502032)
#### 任务要求

#### 90.子集II


大家之前做了 40.组合总和II 和 78.子集 ，本题就是这两道题目的结合，建议自己独立做一做，本题涉及的知识，之前都讲过，没有新内容。 

题目链接/文章讲解：https://programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html    
视频讲解：https://www.bilibili.com/video/BV1vm4y1F71J


##### 重要知识点
- 解题思路


**解题思路**

本题的思路很直观：子集问题+去重。回溯的题目相对来说好掌握，因为有固定模版，而且题型分类明确。

本题中的去重也是用到了树层去重的概念 + used数组

**代码**

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #1.排序
        #2.是不是都不需要used数组啊-->什么时候需要used数组，什么时候不需要？
        nums=sorted(nums)
        size=len(nums)
        used=[False]*size
        result=[]
        def backTracking(startIdx,path):#入参
            if startIdx>size:#终止条件    
                return
            result.append(path[:])
 
            #单次遍历条件
            for i in range(startIdx,size):
                if i>0 and nums[i-1]==nums[i] and used[i-1]==False:#去重  
                    continue
                
                path.append(nums[i])
                used[i]=True
                backTracking(i+1,path)
                used[i]=False
                path.pop()
        backTracking(0,[])
        return result
```
