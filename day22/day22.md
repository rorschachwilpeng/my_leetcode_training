# 代码随想录
## 回溯算法
### 《代码随想录》回溯算法：组合
#### 任务要求

#### 77. 组合


对着 在 回溯算法理论基础 给出的 代码模板，来做本题组合问题，大家就会发现 写回溯算法套路。

在回溯算法解决实际问题的过程中，大家会有各种疑问，先看视频介绍，基本可以解决大家的疑惑。

本题关于剪枝操作是大家要理解的重点，因为后面很多回溯算法解决的题目，都是这个剪枝套路。 

题目链接/文章讲解：https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html    
视频讲解：https://www.bilibili.com/video/BV1ti4y1L7cv  
剪枝操作：https://www.bilibili.com/video/BV1wi4y157er

##### 重要知识点
- 回溯算法三部曲
- 回溯算法的树形结构
- 剪枝操作

**回溯算法三部曲**

1. 确定入参；
2. 确定终止条件；
3. 单次遍历逻辑

和递归很像，只是“单次遍历逻辑中”是for循环。

**回溯算法的树形结构**

图中可以看到，在树形结构中，树层（横向）是由for循环决定的，树枝（纵向）是由递归决定的。

![截屏2025-01-15 08.33.35.png](http://cdn.kamacoder.com/678772e4b78e1-phpo5VRoA.png) 


**剪枝操作**

如果我们现在有个例子n==4, k==4（上图）
从树形结构角度，我们可以发现。在树的第一层中，对于选2/选3/选4都是没有意义的（荧光色标注的节点都是不必要的，可以剪掉的）。因为我们不可能在这些分支中凑出4个元素，所以这些枝干可以直接剪掉。

怎么在代码中实现呢

![截屏2025-01-15 08.41.57.png](http://cdn.kamacoder.com/678774db1b593-php3b9rqE.png) 

**常规实现**

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n=n+1
        self.k=k
        result=[]
        self.backTracking(result,[],1)
        return result
    

    def backTracking(self,res,path,startIdx):#入参
        #终止条件
        if len(path)==self.k:
            res.append(path[:])
            return

        #单次遍历循环
        #为什么要for循环？
        #startIdx
        for i in range(startIdx,self.n):
            path.append(i)
            self.backTracking(res,path,i+1)
            path.pop()
```

**剪枝优化代码**

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n=n+1
        self.k=k
        result=[]
        self.backTracking(result,[],1)
        return result
    

    def backTracking(self,res,path,startIdx):#入参
        #终止条件
        if len(path)==self.k:
            res.append(path[:])
            return

        for i in range(startIdx,self.n-(self.k-len(path))+1):
            path.append(i)
            self.backTracking(res,path,i+1)
            path.pop()
```



### 《代码随想录》回溯算法：组合优化
#### 任务要求

#### 77. 组合优化


对着 在 回溯算法理论基础 给出的 代码模板，来做本题组合问题，大家就会发现 写回溯算法套路。

在回溯算法解决实际问题的过程中，大家会有各种疑问，先看视频介绍，基本可以解决大家的疑惑。

本题关于剪枝操作是大家要理解的重点，因为后面很多回溯算法解决的题目，都是这个剪枝套路。 

题目链接/文章讲解：https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html    
视频讲解：https://www.bilibili.com/video/BV1ti4y1L7cv  
剪枝操作：https://www.bilibili.com/video/BV1wi4y157er

##### 重要知识点
- 回溯算法三部曲
- 回溯算法的树形结构
- 剪枝操作

**回溯算法三部曲**

1. 确定入参；
2. 确定终止条件；
3. 单次遍历逻辑

和递归很像，只是“单次遍历逻辑中”是for循环。

**回溯算法的树形结构**

图中可以看到，在树形结构中，树层（横向）是由for循环决定的，树枝（纵向）是由递归决定的。

![截屏2025-01-15 08.33.35.png](http://cdn.kamacoder.com/678772e4b78e1-phpo5VRoA.png) 


**剪枝操作**

如果我们现在有个例子n==4, k==4（上图）
从树形结构角度，我们可以发现。在树的第一层中，对于选2/选3/选4都是没有意义的（荧光色标注的节点都是不必要的，可以剪掉的）。因为我们不可能在这些分支中凑出4个元素，所以这些枝干可以直接剪掉。

怎么在代码中实现呢

![截屏2025-01-15 08.41.57.png](http://cdn.kamacoder.com/678774db1b593-php3b9rqE.png) 

**常规实现**

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n=n+1
        self.k=k
        result=[]
        self.backTracking(result,[],1)
        return result
    

    def backTracking(self,res,path,startIdx):#入参
        #终止条件
        if len(path)==self.k:
            res.append(path[:])
            return

        #单次遍历循环
        #为什么要for循环？
        #startIdx
        for i in range(startIdx,self.n):
            path.append(i)
            self.backTracking(res,path,i+1)
            path.pop()
```

**剪枝优化代码**

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n=n+1
        self.k=k
        result=[]
        self.backTracking(result,[],1)
        return result
    

    def backTracking(self,res,path,startIdx):#入参
        #终止条件
        if len(path)==self.k:
            res.append(path[:])
            return

        for i in range(startIdx,self.n-(self.k-len(path))+1):
            path.append(i)
            self.backTracking(res,path,i+1)
            path.pop()
```



### 《代码随想录》回溯算法：组合总和III
#### 任务要求

#### 216.组合总和III


如果把 组合问题理解了，本题就容易一些了。 

题目链接/文章讲解：https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html    
视频讲解：https://www.bilibili.com/video/BV1wg411873x

##### 重要知识点
- 思路

**思路**

和“#77.组合”是一样的思路。


**代码**

```
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #普通实现方法
        self.n=n
        self.k=k
        result=[]
        self.backTracking(result,[],1,0)
        return result

    def backTracking(self,res,path,startIdx,sumVal):
        if sumVal>self.n:
            return
        #终止条件
        if sumVal==self.n and len(path)==self.k:
            res.append(path[:])
            return
        

        #剪枝优化
        for i in range(startIdx,9-(self.k-len(path))+2):
            path.append(i)
            sumVal+=i
            self.backTracking(res,path,i+1,sumVal)
            path.pop()
            sumVal-=i
```



### 《代码随想录》回溯算法：电话号码的字母组合
#### 任务要求

#### 17.电话号码的字母组合


本题大家刚开始做会有点难度，先自己思考20min，没思路就直接看题解。 

题目链接/文章讲解：https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html    
视频讲解：https://www.bilibili.com/video/BV1yV4y1V7Ug

##### 重要知识点
- 解题思路

**解题思路**

本题有两个重点：

1. 利用字典来存储digit和字母之间的映射关系；
2. 利用终止条件和树层遍历的边界设置，构造看似会越界但实则永远不会越界的边界。

``` for item in self.phoneMap[digits[startIdx]]``` --> 之所以不会越界是因为一旦路径长度符合返回条件，立即返回剪枝，值得好好体会。


**代码**

```
class Solution:
    def letterCombinations(self, digits: str) -> L:
        if not digits:
            return []

        self.phoneMap={
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz"
        }
        self.res=[]

        self.backTracking(digits,len(digits),[],0)
        return self.res

    def backTracking(self,digits,size,path,startIdx):
        if len(path)==size:
            self.res.append("".join(path[:]))
            return
        
        for item in self.phoneMap[digits[startIdx]]:
            path.append(item)
            self.backTracking(digits,size,path,startIdx+1)
            path.pop()
```
