# 代码随想录
## 二叉树
### 《代码随想录》二叉树：二叉搜索树的最近公共祖先
#### 任务要求
### 235. 二叉搜索树的最近公共祖先


相对于 二叉树的最近公共祖先 本题就简单一些了，因为 可以利用二叉搜索树的特性。 

题目链接/文章讲解：https://programmercarl.com/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html   
视频讲解：https://www.bilibili.com/video/BV1Zt4y1F7ww

##### 重要知识点
-  解题思路
-  递归，递归，还是递归
-  迭代法

**解题思路**

看到二叉搜索树+遍历寻点的信息，很难不想到利用二叉搜索树+中序遍历-->有序数组的特性。正因如此，我们在对二叉搜索树进行遍历的时候，不需要像对普通二叉树那样，递归整颗树。而是利用其有序性即可。

当我们从上向下去递归遍历，第一个在p和q区间之内的值就是最近公共祖先。

![截屏2025-01-13 10.21.16.png](http://cdn.kamacoder.com/6784e91fad179-phphB5DGc.png) 

``` Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val<p.val:
            self.left=q
            self.right=p
        else:
            self.left=p
            self.right=q
        return self.traversal(root)

    def traversal(self,cur):
        if not cur:
            return cur

        if cur.val<self.left.val:#值小了
            return self.traversal(cur.right)
        elif cur.val>self.right.val:#值大了
            return self.traversal(cur.left)
        else:
            return cur
```

**递归，递归，还是递归**

递归中搜索一条路径的写法：
```
if (递归函数(root.left)) return
if (递归函数(root.right)) return
```

递归中搜索整颗树的写法：
```
left=递归函数(root.left)
right=递归函数(root.right)
left与right的逻辑判断
```

**迭代法**
```Python 
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None
```

### 《代码随想录》二叉树：二叉搜索树中的插入操作
#### 任务要求
#### 701.二叉搜索树中的插入操作


本题比想象中的简单，大家可以先自己想一想应该怎么做，然后看视频讲解，就发现 本题为什么比较简单了。

题目链接/文章讲解：https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html   
视频讲解：https://www.bilibili.com/video/BV1Et4y1c78Y

##### 重要知识点
- 错误的思路
- 正确思路
- 怎么插入新节点？

**错误的思路**

刚开始可能会联想到通过二叉搜索树的有序性质，从根节点开始查找插入位置，然后直接修改结构，但往往会卡在如何将新节点正确插入的逻辑上。

**正确思路**

1. **本质**：
	- 二叉搜索树的插入操作本质上是在叶子节点的位置新增一个节点。
	- 题目只要求返回一个有效结果，因此只需找到适当的插入位置即可。
2. **递归思想**：
	- 通过递归下探到叶子节点：- 如果当前节点为空，则创建新节点作为子节点返回。
	- 否则，递归进入左右子树，根据值的大小决定插入方向。

**怎么插入新节点？**

1. 递归的终止条件：
	- 当遍历到空节点时，创建并返回新节点。
2. 递归的逻辑：
	- 如果 `val` 比当前节点值小，则递归处理左子树。
	- 如果 `val` 比当前节点值大，则递归处理右子树。
3. 返回结果：
	- 通过递归，最终将新的子树连接到原树的相应位置。

**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
        self.val=val
        return self.traversal(root)
    def traversal(self,node):
        if not node:
            nn=TreeNode(self.val)
            return nn

        if node.val<self.val:
            node.right=self.traversal(node.right)
        if node.val>self.val:#值大了
            node.left=self.traversal(node.left)
        return node
```

### 《代码随想录》二叉树：删除二叉搜索树中的节点
#### 任务要求
#### 450.删除二叉搜索树中的节点

相对于 插入操作，本题就有难度了，涉及到改树的结构 

题目链接/文章讲解：https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html   
视频讲解：https://www.bilibili.com/video/BV1tP41177us

##### 重要知识点
- 情况分析
- 删除节点同时构造节点
- 左子树继位

**情况分析**

删除节点时，需要根据二叉搜索树的性质处理不同情况：
1. **目标节点不存在**：直接返回 `None`。
2. **目标节点存在**：- **左右子树均为空**：删除后返回 `None`。
	- **左子树为空，右子树不为空**：删除后返回 `node.right`。
	- **右子树为空，左子树不为空**：删除后返回 `node.left`。
	- **左右子树均不为空**：需要额外处理，选择左子树或右子树中的某个节点继位。

**删除节点同时构造节点**

在目标节点左右子树均不为空的情况下：
- 可以选择**右子树的最左节点**或**左子树的最右节点**作为继位节点。
- 保证二叉搜索树的有序性：- 如果选择右子树继位，将目标节点的左子树接到右子树的最左节点的左边。
	- 如果选择左子树继位，将目标节点的右子树接到左子树的最右节点的右边。

 **左子树与右子树继位的逻辑**

- **右子树继位**：
	- 找到右子树中最左节点（即右子树的最小值）。
	- 将目标节点的左子树挂到这个最左节点的左子树位置。
- **左子树继位**：
	- 找到左子树中最右节点（即左子树的最大值）。
	- 将目标节点的右子树挂到这个最右节点的右子树位置。

两种方式等价，具体选择取决于实现习惯。


**右子树继位代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #删除情况：
        #1.左不空右不空
        #2.左空右不空
        #3.左不空右空
        #4.左右都空
        #5.不存在目标节点
        self.key=key

        return self.traversal(root)


    def traversal(self,node):
        if not node:#终止条件
            return node
        
        if node.val>self.key:#值大了-->向左遍历
            node.left=self.traversal(node.left)    
        elif node.val<self.key:#值小了
            node.right=self.traversal(node.right)
        else:
            if node.left and node.right:
                # nn=TreeNode(node.left.val,None,node.right)
                # return nn
                cur=node.right
                while cur.left:
                    cur=cur.left
                cur.left=node.left
                return node.right
            elif not node.left and node.right:
                return node.right
            elif node.left and not node.right:
                return node.left
            elif not node.left and not node.right:
                return None
        return node
```

**左子树继位代码**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #删除情况：
        #1.左不空右不空
        #2.左空右不空
        #3.左不空右空
        #4.左右都空
        #5.不存在目标节点
        self.key=key
        return self.traversal(root)

    def traversal(self,node):
        if not node:#终止条件
            return node
        
        if node.val>self.key:#值大了-->向左遍历
            node.left=self.traversal(node.left)    
        elif node.val<self.key:#值小了
            node.right=self.traversal(node.right)
        else:
            #左子树继位情况
            if node.left and node.right:
                cur=node.left
                while cur.right:
                    cur=cur.right
                cur.right=node.right
                return node.left
            elif not node.left and node.right:
                return node.right
            elif node.left and not node.right:
                return node.left
            elif not node.left and not node.right:
                return None
        return node
```

