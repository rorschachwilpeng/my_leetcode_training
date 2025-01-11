# 代码随想录
## 二叉树
### 《代码随想录》二叉树：二叉搜索树的最小绝对差
#### 任务要求
#### 530.二叉搜索树的最小绝对差

需要领悟一下二叉树遍历上双指针操作，优先掌握递归 

题目链接/文章讲解：https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html  

视频讲解：https://www.bilibili.com/video/BV1DD4y11779

##### 重要知识点
- 还是二叉搜素树
- 二叉树递归到底什么时候返回值，什么时候不返回值

**还是二叉搜素树**

还是利用二叉搜索树+中序遍历 --> 升序数组的特性。还可以用**双指针**的方法实现，只是在代码实现过程中，在返回值的问题上卡了很久。

**二叉树递归到底什么时候返回值，什么时候不返回值**

递归函数是否需要返回值，主要取决于**递归过程的需求**。一般情况下：
1. **需要返回值的场景**：- 需要通过递归返回值来传递信息（如路径、目标值等）。
	- 需要对递归的结果进行判断或进一步处理。
2. **不需要返回值的场景**：- 递归的目的是遍历整棵树，而不需要在递归结束时传递结果。
	- 结果通过其他变量（如全局变量、类属性）进行记录和维护。
	
 **本题分析：不需要返回值的原因**

1. **任务目标**
	- 本题的目的是在**二叉搜索树**中找到节点值之间的最小绝对差。
	- 在递归过程中，只需要逐个比较相邻节点的值，并更新 `minVal`，无需返回值来辅助递归。
2. **中序遍历的特性**
	- **二叉搜索树的中序遍历结果是有序的**，直接利用这一特性可以逐步比较相邻节点。
	- 递归过程中，比较相邻节点的值是否更接近目标，无需通过返回值将信息传递给上一层递归。
3. **全局变量的维护**
	- 通过 `self.pre` 和 `self.minVal` 来保存当前遍历过程中需要的信息：
		- `self.pre`：记录上一个访问的节点。
		- `self.minVal`：存储当前的最小绝对差。
	- 这些变量是类的属性，可以在递归过程中共享，避免使用返回值传递信息。
4. **递归的遍历性质**
	- 递归的目的是访问树中的每个节点并执行某些逻辑：- **左子树**：递归调用 `self.traversal(cur.left)`。
		- **当前节点**：计算当前节点和前一个节点的差值。
		- **右子树**：递归调用 `self.traversal(cur.right)`。
	- 每次递归结束后，只需要返回到上一层继续遍历，而不需要将结果作为返回值传递。

**双指针实现代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minVal=float('inf')
        self.pre=None
        self.traversal(root)
        return self.minVal

    def traversal(self,cur):
        if not cur:
            return
        #中序 - 左中右
        self.traversal(cur.left)
        if self.pre is not None:
            self.minVal=min(self.minVal, abs(cur.val-self.pre.val))
        self.pre=cur#移动双指针

        self.traversal(cur.right)
```

### 《代码随想录》二叉树：二叉搜索树中的众数
#### 任务要求
#### 501.二叉搜索树中的众数


和 530差不多双指针思路，不过 这里涉及到一个很巧妙的代码技巧。

可以先自己做做看，然后看我的视频讲解。

https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html   
视频讲解：https://www.bilibili.com/video/BV1fD4y117gp

##### 重要知识点
- 遍历两次的直白思路
- 利用动态数组，遍历一次的思路

**遍历两次的直白思路**
第一个思路很直白。遍历两次二叉树，第一次获取二叉树中的最高频次，第二次获取最高频次所对应的元素值。

**遍历两次的实现代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #解法2--遍历两次--
        self.dict=defaultdict(int)
        self.searchBST(root)
        result=[]
        maxVal=max(self.dict.values())
        for key,val in self.dict.items():
            if val==maxVal:
                result.append(key)
        return result
        
    def searchBST(self,node):
        if not node:
            return 
        self.dict[node.val]+=1
        self.searchBST(node.left)
        self.searchBST(node.right)
```

**利用动态数组，遍历一次的思路**

只遍历一次二叉树，在遍历过程中利用一个全局最大频次以及动态数组来记录对应的元素值。当全局最大频次被刷新时，重置动态数组中的元素值。

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #解法1：只遍历一遍
        self.pre=None
        self.maxCount=float('-inf')
        self.count=0
        self.res=[]


        self.traversal(root)
        return self.res

    def traversal(self,cur):
        if not cur:return

        #中序
        #左
        self.traversal(cur.left)

        #中
        if not self.pre:
            self.count+=1
        elif self.pre and self.pre.val==cur.val:
            self.count+=1
        else:#换元素了
            self.count=1

        #判断是否需要更新数组
        if self.count==self.maxCount:
            self.res.append(cur.val)
        elif self.count>self.maxCount:
            self.maxCount=self.count
            self.res=[cur.val]
        
        self.pre=cur

        #右
        self.traversal(cur.right)

```

### 《代码随想录》二叉树：二叉树的最近公共祖先
#### 任务要求
#### 236. 二叉树的最近公共祖先


本题其实是比较难的，可以先看我的视频讲解 

https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html  
视频讲解：https://www.bilibili.com/video/BV1jd4y1B7E2

##### 重要知识点
- 整体思路
- 为什么要用后序遍历
- 递归过程中是否需要返回值
- 递归过程中，左空右不空 / 左不空右空的情况怎么处理？
- 当根节点为目标值的情况

**整体思路**

利用后序遍历，递归判断目标节点，如果当前节点为目标节点的父节点/为目标节点本身，那么将该节点向上传递。

**为什么要用后序遍历**

如果使用前序/中序进行递归遍历的话，在对中节点进行条件判断时候左右节点可能还没有进行状态判断。因此需要增加其他的变量来进行判断，增加了代码复杂度。而对于后序遍历，我们就天然实现了回溯思路，每次都可以根据左右子树的状态来对中节点进行判断处理。


**递归过程中是否需要返回值？**

因为我们需要根据左右子树的状态来决定中节点的状态，所以本题需要在递归过程中构造返回值。


**递归过程中，左空右不空 / 左不空右空的情况怎么处理？**

左空右不空 / 左不空右空其实是同一种情况，我们直接将不为空的子树向上返回就行了。


**当根节点为目标值的情况**

该情况已经被包括在终止条件 ```if node==self.node1 or node==self.node2:return node```了。

**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #后序遍历-->因为要从下往上找
        self.node1=p
        self.node2=q
        return self.travesal(root)

    def travesal(self, node):#入参
        #终止条件
        if not node: return None
        if node==self.node1 or node==self.node2:return node #如果遇到了目标节点，那么就向上返回
            

        #单次遍历逻辑 -- 中序遍历
        lt=self.travesal(node.left)#左
        rt=self.travesal(node.right)#右
        ##中
        if lt and rt:return node#左右树都不为空
        elif not lt and rt: return rt#左空右不空
        elif lt and not rt: return lt#左不空右空
        else: return None#左右都空
```
