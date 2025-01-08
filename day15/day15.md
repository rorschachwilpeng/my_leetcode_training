# 代码随想录
## 二叉树
### 《代码随想录》二叉树：平衡二叉树
#### 任务要求
#### 110.平衡二叉树 （优先掌握递归）
再一次涉及到，什么是高度，什么是深度，可以巩固一下。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html

##### 重要知识点
- 求高度和求深度的复习

**求高度和求深度的复习**

求深度 --> 从上往下 --> 前序遍历 （中左右）；

求高度 --> 从下往上 --> 后序遍历（左右中）。


**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #求深度 --> 前序遍历 --> 中左右 --> 从上到下
        #求高度 --> 后序遍历 --> 左右中 --> 从下到上
        if not root:
            return True
        return False if self.getHeight(root)==-1 else True  

    def getHeight(self,node):#入参
        if not node:#终止条件
            return 0
        #单次遍历逻辑-->后序-->左右中
        lt=self.getHeight(node.left)#左
        rt=self.getHeight(node.right)#右
        if lt==-1 or rt==-1 or abs(lt-rt)>1:#中
            return -1
        else:
            return 1+max(lt,rt)
```

### 《代码随想录》二叉树：二叉树的所有路径
#### 任务要求
#### 257. 二叉树的所有路径 （优先掌握递归）


这是大家第一次接触到回溯的过程， 我在视频里重点讲解了 本题为什么要有回溯，已经回溯的过程。 

如果对回溯 似懂非懂，没关系， 可以先有个印象。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html

##### 重要知识点
- 回溯思路

**回溯思路**

递归+回溯的思路。其中构建str数组的方法值得关注。

**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res=[]
    
        def traversal(path,node):
            #前序遍历 --> 中左右 --> 因为需要从上到下
            if not node:#终止条件
                return
            if not node.left and not node.right:
                path='->'.join(map(str,path))
                res.append(path[:])

            #单次遍历逻辑
            if node.left:
                path.append(node.left.val)
                traversal(path,node.left)
                path.pop()
            if node.right:
                path.append(node.right.val)
                traversal(path,node.right)
                path.pop()
        
        traversal([root.val],root)
        return res
```
