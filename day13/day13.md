# 代码随想录
## 二叉树
### 《代码随想录》二叉树：二叉树的递归遍历
#### 任务要求
#### 递归遍历 （必须掌握）


二叉树的三种递归遍历掌握其规律后，其实很简单 

题目链接/文章讲解/视频讲解：https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html

##### 重要知识点
- 前序
- 中序
- 后序

**前序遍历 - 递归法**
```Python 
## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        #前序遍历
        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)#中
            dfs(node.left)#左
            dfs(node.right)#右
        dfs(root)
        return res
```

**中序遍历 - 递归法**
```Python 

```# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #递归法 -- 中序
        res=[]

        def dfs(node):
            if not node:
                return
            dfs(node.left)#左
            res.append(node.val)#中
            dfs(node.right)#右
        dfs(root)
        return res
```

**后序遍历 - 递归法**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #递归法 - 后序
        res=[]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
```