# 代码随想录
## 二叉树
### 《代码随想录》二叉树：找树左下角的值
#### 任务要求
#### 513.找树左下角的值


本题递归偏难，反而迭代简单属于模板题， 两种方法掌握一下 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html

##### 重要知识点
-  思路
- 自己写的递归实现
- 代码随想录上的递归实现
- BFS实现

**思路**

最重要的一点是在于不能一路向左搜索，而是首先找到最底层节点，再在其中找到最左节点。

**自己写的递归实现**

利用递归+回溯，先将所有的路径都加入到结果数据。然后再对结果数组进行判断，找到最深层的节点。思路清晰，但是时间和空间复杂度上都存在优化的空间。
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res=[]
        self.traversal(res,[root.val],root)
        leftMost=0
        MaxLevel=0
        for path in res:
            if len(path)>MaxLevel:
                MaxLevel=len(path)
                leftMost=path[-1]
        return leftMost
        
    def traversal(self,res,path,node):
        if not node:#终止条件
            return
        
        if not node.left and not node.right:#叶子节点
            res.append(path[:])

        if node.left:
            path.append(node.left.val)
            self.traversal(res,path,node.left)
            path.pop()

        if node.right:
            path.append(node.right.val)
            self.traversal(res,path,node.right)
            path.pop()
```

**代码随想录上的递归实现**

在递归遍历的时候就进行了大小比较，不用再创建一个多余的内存空间用于存储所有路径
```Python 
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result
    
    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
```
**BFS实现**

如果用BFS的话，这道题就是模版题，没有太多可说的
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #BFS
        que=collections.deque([root])
        res=[]
        while que:
            level=[]
            for i in range(len(que)):
                cur=que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level)
        return res[-1][0]
```


### 《代码随想录》二叉树：路径总和
#### 任务要求
#### 112.路径总和 & 113.路径总和ii 


本题 又一次涉及到回溯的过程，而且回溯的过程隐藏的还挺深，建议先看视频来理解 

112. 路径总和，和 113. 路径总和ii 一起做了。 优先掌握递归法。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html
##### 重要知识点
- 112. 路径总和
- 112. 路径总和递归精简版
- 113. 路径总和ii
- 相关的问题

**112. 路径总和**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.EXISTED=False
        if not root:
            return self.EXISTED
        self.traversal(targetSum-root.val,root)
        return self.EXISTED


    def traversal(self,res,node):
        #后序遍历
        if not node:
            return
        
        if not node.left and not node.right:#叶子节点
            if res==0:
                self.EXISTED=True

        if node.left:
            res-=node.left.val
            self.traversal(res,node.left)
            res+=node.left.val
        if node.right:
            res-=node.right.val
            self.traversal(res,node.right)
            res+=node.right.val
```
**112. 路径总和递归精简版**

```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```

**113. 路径总和ii**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res=[]
        if not root:
            return []
        self.traversal(targetSum,root,[root.val])
        return self.res


    def traversal(self,target,node,path):
        #后序遍历
        if not node:
            return
        
        if not node.left and not node.right:#叶子节点
            if target==sum(path):
                self.res.append(path[:])

        if node.left:
            path.append(node.left.val)
            self.traversal(target,node.left,path)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.traversal(target,node.right,path)
            path.pop()
```

**相关的问题**
1. 为什么“路径之和”利用递减更好呢？ --> 优化代码，入参少了。但为什么计算量少了呢🤔











### 《代码随想录》二叉树：从中序与后序遍历序列构造二叉树
#### 任务要求
#### 513.从中序与后序遍历序列构造二叉树

本题算是比较难的二叉树题目了，大家先看视频来理解。 

106.从中序与后序遍历序列构造二叉树，105.从前序与中序遍历序列构造二叉树 一起做，思路一样的

题目链接/文章讲解/视频讲解：https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html

##### 重要知识点
- 思路
- 实现方法

**思路**

后序遍历顺序-->左右中；中序遍历顺序-->左中右

关键问题： 我们在中序数组中无法区分哪些节点是左节点，哪些节点是右节点

先通过后序数组找到中间节点，然后我们通过利用中间节点值在中序数组中找到其对应的索引。按照索引位置进行切割，即得到左右子树。当切割后的左右子树中节点数量大于1时，我们又回到了*关键问题*。但是我们现在已经知道了左右子树中有几个元素，于是我们可以利用这个信息再去后序数组中分离左右子树。完成上述步骤后我们就在树中从上往下走了一层了，所以我们只需将剩下的步骤以递归的方式构造好就行了。

--> 在后序数组中找到中间节点 --> 利用中节点在中序数组中切割左右子树 --> 根据左右子树的元素数量又回到后序数组中进行左右子树分离 --> 进行递归  --> 

**实现方法**
1. 若后序数组为0，空节点
2. 后序数组最后一个元素为节点元素
3. 寻找中序数组位置作为切割点
4. 切中序数组
5. 切后序数组
6. 递归处理左右子区间

```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #1.后序数组为0，空节点
        if not postorder:
            return None
        #2.后序数组最后一个元素为节点元素
        val=postorder[-1]
        root = TreeNode(val)
        #3.寻找中序数组位置作为切割点
        cutPoint=inorder.index(val)

        #4.切中序数组
        inorder_left=inorder[:cutPoint]
        inorder_right=inorder[cutPoint+1:]

        #5.切后序数组
        postorder_left=postorder[:len(inorder_left)]
        postorder_right=postorder[len(inorder_left):len(postorder)-1]

        #6.递归处理左区间和右区间
        root.left=self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)
        return root
```
