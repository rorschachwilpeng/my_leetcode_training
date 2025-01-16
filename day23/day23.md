# 代码随想录
## 回溯算法
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
### [《代码随想录》回溯算法：组合总和](https://notes.kamacoder.com/questions/502027)
#### 任务要求

#### 39. 组合总和


本题是 集合里元素可以用无数次，那么和组合问题的差别 其实仅在于 startIndex上的控制

题目链接/文章讲解：https://programmercarl.com/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.html  
视频讲解：https://www.bilibili.com/video/BV1KT4y1M7HJ


##### 重要知识点
- 解题思路
- 剪枝优化

**解题思路**

通过控制startIdx的位置来实现同个元素可以无限取。

**剪枝优化**

1. 通过组合总和来做文章，一旦总和大于目标值，立刻剪枝；
2. 为了实现第一步，我们首先需要对数组进行排序，这样才能保证剪去的枝中不包含可能是答案的节点。


**代码**

```
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #相当于动态规划里的多重背包
        self.candidates=sorted(candidates)
        self.res=[]
        self.target=target
        size=len(candidates)
        self.backTracking(0,[],size,0)
        return self.res
#怎么保证一个数字可以无限制重复被选取，同时又
#去重？
#
    def backTracking(self,sumVal,path,size,startIdx):
  
        if sumVal==self.target:#返回条件
            self.res.append(path[:])
            return
        
        for i in range(startIdx,size):
            item=self.candidates[i]
            if sumVal+item>self.target:#终止条件
                break
            sumVal+=item
            path.append(item)
            self.backTracking(sumVal,path,size,i)
            sumVal-=item
            path.pop()
```
### [《代码随想录》回溯算法：组合总和II](https://notes.kamacoder.com/questions/502028)
#### 任务要求

#### 40.组合总和II


本题开始涉及到一个问题了：去重。

注意题目中给我们 集合是有重复元素的，那么求出来的 组合有可能重复，但题目要求不能有重复组合。 

题目链接/文章讲解：https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html    
视频讲解：https://www.bilibili.com/video/BV12V4y1V73A


##### 重要知识点
- 怎么去重？
- 为什么树层去重前要对数组进行排序？
- 剪枝优化

**怎么去重**

1. 从树形结构的角度出发理解回溯中的去重比较简单，在树形结构中我们是对于树层进行去重而不是树枝。
2. 去重之前需要对数组进行排序。


**为什么树层去重前要对数组先进行排序**

1. 剪枝优化：排序使得数组递增排列。在递归过程中，如果当前路径上的数值之和已经超过目标值，后续的元素只会比当前值更大，无需继续搜索，直接剪枝可以提高效率；
2. 循环不变量：排序后，可以根据简单的条件判断（当前元素是否和前一个元素相同且未使用过）来构造循环不变量，防止复杂的去重逻辑。


**代码**
```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #重点-->1.先排序；2.我们是对树层去重，树枝不去重
        #3.

        #利用一个used数组来记录
        self.candidates=sorted(candidates)
        self.size=len(candidates)
        self.target=target

        result=[]
        self.used=[False]*self.size
        self.backTracking(0,[],result,0)
        return result


    def backTracking(self,sumVal,path,res,startIdx):#入参
        #终止条件
        if sumVal==self.target:
            res.append(path[:])
            return

        #单次遍历逻辑
        for i in range(startIdx,self.size):
            item=self.candidates[i]

            if i>startIdx and self.candidates[i]==self.candidates[i-1] and not self.used[i-1]:#去重
                continue
            
            if sumVal+item>self.target:#剪枝
                break

            sumVal+=item
            path.append(item)
            self.used[i]=True

            self.backTracking(sumVal,path,res,i+1)

            sumVal-=item
            path.pop()
            self.used[i]=False
```

**剪枝优化**

```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #剪枝优化
        result=[]
        size=len(candidates)
        used=[False]*size
        self.backTracking(sorted(candidates),target,result,[],0,size,used)
        return result


    def backTracking(self,candidates,target,res,path,startIdx,size,used):
        if target==0:
            res.append(path[:])
            return
        
        for i in range(startIdx,size):
            if i>startIdx and candidates[i]==candidates[i-1] and used[i]==False:#去重
                continue
            
            if candidates[i]>target:#剪枝
                break
            
            path.append(candidates[i])
            used[i]=True
            self.backTracking(candidates,target-candidates[i],res,path,i+1,size,used)

            used[i]=False
            path.pop()
```
### [《代码随想录》回溯算法：分割回文串](https://notes.kamacoder.com/questions/502029)
#### 任务要求

#### 131.分割回文串


本题较难，大家先看视频来理解 分割问题，明天还会有一道分割问题，先打打基础。 

https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html   
视频讲解：https://www.bilibili.com/video/BV1c54y1e7k6


##### 重要知识点
- 回溯能解决哪些问题
- 思路
- 难点

**回溯能解决哪些问题**

回溯能解决的问题包括：组合问题，切割问题，子集问题，排列问题，棋盘问题。

**思路**

其实和“组合问题”思路很像，只是我们首先要将切割问题抽象成组合问题，

例如对于字符串abcdef：
- 组合问题：选取一个a之后，在bcdef中再去选取第二个，选取b之后在cdef中再选取第三个.....。
- 切割问题：切割一个a之后，在bcdef中再去切割第二段，切割b之后在cdef中再切割第三段.....。


然后利用```startIdx```来模拟切割线。


**难点**

1. 切割问题中递归如何终止 --> 当递归位置 > 字符串长度
2. 在递归循环中如何截取子串 --> 这点对我个人而言是最难的，因为我对边界处理的掌握一直不够好。这里我们通过```subStr=s[startIdx,i+1]```来递归切割子串。注意⚠️：Python中数组左闭右开的属性。



**代码**

```
class Solution:
    def isPalindrome(self, s):
        return True if s[::-1]==s else False
        
    def partition(self, s: str) -> List[List[str]]:
        result=[]
    
        def backTracking(startIdx,path):#入参
            if startIdx==len(s):
                result.append(path[:])
                return
            
            #单次遍历逻辑 
            for i in range(startIdx,len(s)):            
                subStr=s[startIdx:i+1]
                if self.isPalindrome(subStr):#是回文
                    path.append(subStr)
                    #path.append(s[startIdx:i+1])
                    backTracking(i+1,path)
                    path.pop()

        backTracking(0,[])
        return result
```
