# 代码随想录
## 二叉树

### 《代码随想录》二叉树：翻转二叉树
#### 任务要求
#### 226.翻转二叉树 （优先掌握递归）
这道题目 一些做过的同学 理解的也不够深入，建议大家先看我的视频讲解，无论做过没做过，都会有很大收获。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html

##### 重要知识点
这两天要忙其他事情，题解会写比较简单
- 递归实现
- BFS实现

**递归实现（前序）**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #前序
        if not root:
            return None
        
        root.left,root.right=root.right,root.left#中
        self.invertTree(root.left)#左
        self.invertTree(root.right)#右
        return root
```

**BFS实现**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS-层序遍历 - 前序(中左右)
        res=[]
        que=collections.deque([root])
        if root is None:
            return None

        while que:
            level=[]
            level_size=len(que)
            for i in range(level_size):
                cur=que.popleft()
                cur.left,cur.right=cur.right,cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root
```


### 《代码随想录》二叉树：对称二叉树
#### 任务要求
#### 101. 对称二叉树 （优先掌握递归）


先看视频讲解，会更容易一些。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html

##### 重要知识点
- 思路
- 遍历顺序
- 递归实现

**思路**

如果要判断一颗二叉树是否对称，那么我们就需要判断其左右子树是否可以翻转。利用递归三部曲可以分而治之地进行实现。

**遍历顺序**
本题只能用后序遍历，因为要先获取左右子节点的信息，传到父节点进行判断。

**递归实现**
1. 入参：需要判断是否可以对称的左右子树 
2. 终止条件： 左右子树一定不对称的情况（包括：左右子树的状态不同，或者值不同）
3. 单次遍历逻辑：判断左右子树是否对称，这里我们需要判断的是左右子树是否可以进行翻转，所以将“左子树的左子树”与“右子树的右子树”进行比较，将”左子树的右子树“和”右子树的左子树“进行比较。

**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
    
        return self.compare(root.left,root.right)
    
    def compare(self,l,r):#入参
        #终止条件
        if not l and not r:return True#左右为空
        elif not l and r:return False#左空右不空
        elif l and not r:return False#左不空右空
        elif l.val!=r.val: return False#左右都不空，但值不同
		
        #单次遍历逻辑
        outside=self.compare(l.left,r.right)
        inside =self.compare(l.right,r.left)
        SYMMETRIC=outside and inside
    
        return SYMMETRIC
```

### 《代码随想录》二叉树：二叉树的最大深度
#### 任务要求
#### 104.二叉树的最大深度 （优先掌握递归）


什么是深度，什么是高度，如何求深度，如何求高度，这里有关系到二叉树的遍历方式。

大家 要先看视频讲解，就知道以上我说的内容了，很多录友刷过这道题，但理解的还不够。

题目链接/文章讲解/视频讲解： https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html

##### 重要知识点
- 二叉树中的深度和高度
- 遍历顺序
- 一些答疑解惑

**二叉树中的深度和高度**
- 深度：指从根节点到该节点的最长简单路径条数或者节点数 --> **从上到下** --> 如果用深度来描述一个溶洞，那么自然而然是指从上（洞口）往下（洞底）的距离。
- 高度：指从该节点到叶子节点的最长简单路径条数或者节点数 --> **从下到上** --> 如果用高度来描述一棵大树，那么自然而然是指从下（树根）往上（树顶）的距离


**遍历顺序**
- 深度：需要用前序遍历 --> 中左右，才能从上到下
- 高度：需要用后序遍历 --> 左右中，才能从下到上
本道题中可以用求高度的方式AC，因为题目中的高度即深度。

**一些答疑解惑**

Q：所有二叉树中的深度和高度都相等吗？

A: **不一定相等**：

R:
- 在根节点：深度为 0，高度为树的最大高度。
- 在叶节点：深度可能大于 0，但高度总为 0。

*相等的特殊情况*

在一些特殊情况下，深度和高度的概念可以统一，例如： **整棵树的高度等于最大深度**。最大深度是从根到最深节点的距离，整棵树的高度也是从根到叶节点的最长路径。

**代码**

DFS
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que=collections.deque([root])
        res=0

        while que:
            res+=1
            for i in range(len(que)):
                cur=que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res
```

BFS
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que=collections.deque([root])
        res=0

        while que:
            res+=1
            for i in range(len(que)):
                cur=que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res
```
		
		
		

### 《代码随想录》二叉树：二叉树的最小深度
#### 任务要求
#### 111.二叉树的最小深度 （优先掌握递归）


先看视频讲解，和最大深度 看似差不多，其实 差距还挺大，有坑。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.html

##### 重要知识点
-  这可不是求最大深度

**这可不是求最大深度**

本题给出了明确定义：最小深度是从根节点到最近叶子节点的最短路径上的节点数量。叶子节点是指没有子节点的节点。
因此我们不能将空节点看作是最小深度节点。

**DFS**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node):
        if not node:
            return 0
        #后序 --> 方便 --> 左右中
        lh=self.traversal(node.left)
        rh=self.traversal(node.right)
        if not node.left and node.right:
            return 1+rh
        if node.left and not node.right:
            return 1+lh
        return 1+min(lh,rh)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.traversal(root)
```

**BFS**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #BFS
        if not root:
            return 0
        que=collections.deque([root])
        minDepth=0
        
        while que:
            minDepth+=1
            for i in range(len(que)):
                cur=que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if not cur.left and not cur.right:#叶子节点
                    return minDepth
        return minDepth
```
