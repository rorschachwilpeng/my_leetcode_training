# 代码随想录
## 二叉树
### 《代码随想录》二叉树：最大二叉树
#### 任务要求
#### 654.最大二叉树


又是构造二叉树，昨天大家刚刚做完 中序后序确定二叉树，今天做这个 应该会容易一些， 先看视频，好好体会一下 为什么构造二叉树都是 前序遍历 

题目链接/文章讲解：https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html   
视频讲解：https://www.bilibili.com/video/BV1MG411G7ox

##### 重要知识点
- 实现思路
- 切片法
- 下标法

**实现思路**：本题和[106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)思路是一样的，同样是构造二叉树。

实现思路 --> 递归+前序遍历（从上到下构造二叉树）

步骤：
1. 找到当前数组中的最大元素
2. 将最大元素作为树中下一层的头节点
3. 在数组中根据最大元素的值将数组切分成左右子树
4. 递归左右子树

**切片法**

个人更倾向于切片法，下标法的边界处理容易出错。
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
       #递归+前序遍历实现-->中左右
        return self.traversal(nums)
    def traversal(self, arr):#入参
        #终止条件
        if not arr:
            return None
        #1.找到当前数组中的最大元素
        root_val=max(arr)
        #2.将最大元素作为下一层子树的头节点
        root=TreeNode(root_val)
        #3.在数组中根据最大元素索引将数组切分成左右子树
        CuttingIdx=arr.index(root_val)

        left_nodes=arr[:CuttingIdx]
        right_nodes=arr[CuttingIdx+1:]

        #4.递归左右子树
        root.left=self.traversal(left_nodes)
        root.right=self.traversal(right_nodes)
        return root
```

**下标法**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
       #下标法
       return self.traversal(nums,0,len(nums))

    def traversal(self,arr,left,right):
        if left>=right:
            return
        #找到最大值，以及数组中其所对应的下标
        maxIdx=left
        for i in range(left+1,right):
            if arr[i]>arr[maxIdx]:
                maxIdx=i
        #构造中间节点
        root=TreeNode(arr[maxIdx])
        #递归左右子树
        root.left=self.traversal(arr,left,maxIdx)
        root.right=self.traversal(arr,maxIdx+1,right)
        return root
```



### 《代码随想录》二叉树：合并二叉树
#### 任务要求
#### 617.合并二叉树


这次是一起操作两个二叉树了， 估计大家也没一起操作过两个二叉树，也不知道该如何一起操作，可以看视频先理解一下。 优先掌握递归。

题目链接/文章讲解：https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html   
视频讲解：https://www.bilibili.com/video/BV1m14y1Y7JK

##### 重要知识点
- 一次错误的尝试
- 正确解法

**一次错误的尝试**
第一次尝试的思路：
- 根据两颗树的值创建一棵新的树，之所以需要创建新的树是为了避免递归构造过程中的空树和另一棵树（假设有值）的相加情况。
- 递归的终止条件一一定义
- 代码出错在当一个节点为空，一个节点不为空的时候。按照代码中构造的循环不变量会继续在空节点中寻找其左/右子节点，从而报错。

--> 上面这个思路出错的地方很明显：1. 二叉树中的空值仍然可以做相加/作为值来返回，这体现了对于二叉树属性掌握还不够熟； 2. 创建新树的思路没错，但是产生了不必要的时间和空间复杂度。

**错误**的代码❌
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #前序遍历

        #遍历过程中的情况分析
            #1.左右子树都有值 --> 相加
            #2.左树有节点&右树没有节点 --> 左树 -->那么之后返回哪颗树呢？
            #3.左树没节点&右树有节点 --> 右树 --> 
            #4.左右树都没有元素 --> 空节点

        #怎么保证循环不变量能将左/右节点为空的情况也囊括
        return self.traversal(root1,root2)
    def traversal(self,left,right):
        if not left and not right:
            return None
        elif left and not right:
            nodeVal=left.val
        elif not left and right:
            nodeVal=right.val
        elif left and right:
            nodeVal=left.val+right.val
        
        root=TreeNode(nodeVal)
        root.left=self.traversal(left.left,right.left)
        root.right=self.traversal(left.right,right.right)
        return root
```

**正确解法**

直接在一颗树的基础上进行构造。当某一个节点为空时，就返回另一个节点。如果两个节点都为空也无所谓，因为那只会返回一个None。

```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #前序遍历
        return self.traversal(root1,root2)
    def traversal(self,lt,rt):
        if not lt:return rt
        if not rt:return lt

        lt.val+=rt.val
        lt.left=self.traversal(lt.left,rt.left)
        lt.right=self.traversal(lt.right,rt.right)
        return lt
```

### 《代码随想录》二叉树：二叉搜索树中的搜索
#### 任务要求
#### 700.二叉搜索树中的搜索


递归和迭代 都可以掌握以下，因为本题比较简单， 了解一下 二叉搜索树的特性

题目链接/文章讲解: https://programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html   
视频讲解：https://www.bilibili.com/video/BV1wG411g7sF

##### 重要知识点
- 二叉搜索树性质
- 递归法
- 迭代法

**二叉搜索树性质**

二叉搜索树: 二叉搜索树中，当前根节点一定比其左子树的值大，比其右子树的值小


**递归法**

本题除了递归三部曲外，在单层遍历时需要直接return；因为题意中要求我们返回子树，所以需要用一个变量来接住返回值，否则指针会丢失，返回值为空。

```
res = self.traversal(node.left/right, tar)
return res
```

或者用简化写法
```
return self.traversal(node.left, tar)
```

**递归法代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traversal(root,val)

    def traversal(self,node,target):
        if not node or node.val==target:#终止条件
            return node
        #二叉搜索树性质
        if target<node.val:
            return self.traversal(node.left,target)
        if target>node.val:
            return self.traversal(node.right,target)
```

**迭代法**
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #迭代法
        if not root:
            return root
        
        while root:
            if val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
            else:
                return root
```

### 《代码随想录》二叉树：验证二叉搜索树
#### 任务要求
#### 98.验证二叉搜索树


遇到 搜索树，一定想着中序遍历，这样才能利用上特性。 

但本题是有陷阱的，可以自己先做一做，然后在看题解，看看自己是不是掉陷阱里了。这样理解的更深刻。

题目链接/文章讲解：https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html  
视频讲解：https://www.bilibili.com/video/BV18P411n7Q4

##### 重要知识点
- 二叉搜索树和中序遍历
- 递归法
- 双指针法

**二叉搜索树和中序遍历**

二叉搜索树具有如下性质：
- 节点的左子树  只包含**小于**当前节点的数。
- 节点的右子树只包含 **大于** 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

所以当我们用中序遍历来遍历一颗二叉搜索树时，返回的数组就是一个增序数组。我们可以利用这个特性来解题。

**递归法**

利用中序遍历遍历二叉树，并维护一个全局最大值。如果这颗树是一颗有效的二叉搜索树的话，那么每个新元素都应该大于前一个值，我们将新的最大值更新为全局最大值。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #利用二叉搜索树的特性+中序遍历
        if not root:
            return True
        self.maxVal=float('-inf')
        return self.traversal(root)
    
    def traversal(self,node):
        if not node:
            return True
        #左中右
        left=self.traversal(node.left)
        if node.val>self.maxVal:
            self.maxVal=node.val
        else:
            return False
        right=self.traversal(node.right)
        return left and right
```

**双指针法**

和在一个数组中利用双指针来判断数组是否为单调递增数组是相同原则。

```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None  # 用来记录前一个节点

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)

        if self.pre is not None and self.pre.val >= root.val:
            return False
        self.pre = root  # 记录前一个节点

        right = self.isValidBST(root.right)
        return left and right
```