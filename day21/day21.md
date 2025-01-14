# 代码随想录
## 二叉树
### 《代码随想录》二叉树：修剪二叉搜索树
#### 任务要求
#### 669. 修剪二叉搜索树

这道题目比较难，比 添加增加和删除节点难的多，建议先看视频理解。

题目链接/文章讲解： https://programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html   
视频讲解： https://www.bilibili.com/video/BV17P41177ud

##### 重要知识点
- 递归的核心思路
- 递归逻辑拆解
- 代码背后的关键点
- 一个生动的比喻

----
**递归的核心思路**

修剪二叉搜索树就像修剪一棵有序的树篱：我们要剪掉不符合范围的枝叶，同时保持整体结构的有序性。利用二叉搜索树的特性，我们可以高效地找到需要修剪的部分。
1. **区间外的节点怎么处理？**
	- 如果当前节点值小于 `low`，那它和它的左子树都太小了，直接“砍掉”，去看看右子树是否有合适的分支。
	- 如果当前节点值大于 `high`，那它和它的右子树都太大了，同样“砍掉”，去看看左子树是否有合适的分支。
2. **区间内的节点怎么办？**
	- 如果当前节点值在 `[low, high]` 区间内，那这段“枝叶”是我们想保留的。
	- 但是它的左右子树还需要继续修剪，递归去修理好它的左右分支，修剪后的结果重新连接到当前节点。

----
**递归逻辑拆解**

- **终止条件**：- 如果当前节点是空的，说明已经修剪到底了，直接返回 `None`。
- **修剪逻辑**：- 如果当前节点值小于 `low`，丢掉当前节点，递归右子树。
	- 如果当前节点值大于 `high`，丢掉当前节点，递归左子树。
	- 如果当前节点值在范围内，递归修剪左右子树，并接回当前节点。

----
**代码背后的关键点**

1. **递归是修剪工具**：
	- 每次递归的结果都是修剪好的子树，最后通过返回值重新连接到父节点上。
2. **二叉搜索树的特性是指南针**：
	- 利用二叉搜索树“左小右大”的特性，可以快速确定哪一边需要修剪，避免不必要的遍历。

----
**一个生动的比喻**

想象你是一位园丁，修剪一棵二叉搜索树：
- 如果某根枝丫太矮（小于 `low`），直接砍掉，从右侧继续寻找。
- 如果某根枝丫太高（大于 `high`），也砍掉，从左侧继续寻找。
- 如果某根枝丫刚好合适，那就留着，并仔细修剪它的左右分支，最终修剪成一棵整齐的、有序的“理想之树”。

这样一层层修剪下去，就能得到一棵完美的二叉搜索树！

---
**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low=low
        self.high=high
        return self.traversal(root)

    def traversal(self,node):
        if not node:return node
        if node.val<self.low:
            return self.traversal(node.right)#如果直接返回node.right不能保证node.right的值就是符合区间要求的，需要一直递归向右寻找。对于大于区间的也是一样的逻辑
        if node.val>self.high:
            return self.traversal(node.left)
        
        node.left=self.traversal(node.left)
        node.right=self.traversal(node.right)
        return node
```

### 《代码随想录》二叉树：将有序数组转换为二叉搜索树
#### 任务要求

#### 108.将有序数组转换为二叉搜索树


本题就简单一些，可以尝试先自己做做。

https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html   
视频讲解：https://www.bilibili.com/video/BV1uR4y1X7qL

##### 重要知识点
- 解题思路

**解题思路**

数组的序列是二叉搜索树中序遍历会得到的结果。所以我们只需要不断切割区间，构造元素即可

**代码**

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        self.size=len(nums)
        return self.traversal(nums)

    def traversal(self,nums):
        if not nums:#终止条件
            return 
        idx=len(nums)//2
        root=TreeNode(nums[idx])

        #递归左区间
        root.left=self.traversal(nums[:idx])
        #递归右区间
        root.right=self.traversal(nums[idx+1:])
        return root

```



### 《代码随想录》二叉树：把二叉搜索树转换为累加树
#### 任务要求
#### 538.把二叉搜索树转换为累加树


本题也不难，在 求二叉搜索树的最小绝对差 和 众数 那两道题目 都讲过了 双指针法，思路是一样的。

https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html   
视频讲解：https://www.bilibili.com/video/BV1d44y1f7wP

##### 重要知识点
- 分析思路

**分析思路**

![截屏2025-01-14 12.04.55.png](http://cdn.kamacoder.com/678652f1c2841-phpwsVLWZ.png) 

**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre=0
        self.traversal(root)
        return root
        
    def traversal(self,node):
        if not node:return node
        
        ##反中序顺序
        self.traversal(node.right)#右
        node.val+=self.pre#中
        self.pre=node.val
        self.traversal(node.left)#左
```

