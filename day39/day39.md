# 代码随想录
## 动态规划
### [《代码随想录》动态规划：打家劫舍](https://notes.kamacoder.com/questions/502084)
#### 任务要求
#### 198.打家劫舍

视频讲解：https://www.bilibili.com/video/BV1Te411N7SX 
https://programmercarl.com/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.html

##### 重要知识点

- 重点知识点
- 动规五部曲

**重点知识点**

打家劫舍的第一题。

关键在于dp数组的定义以及递推公式的构造，首先需要明确dp数组 --> dp[i]:考虑下标为i（包括i）在内的房屋，能够偷窃到的最高金额为dp[i]。然后分析递推关系，对于房屋 **i** 而言，我们有两个状态，偷还是不偷。偷的话，当前状态 **i** 只能是通过 **i-2** 房屋推出来的，因为我们在同一晚偷相邻的房屋。不偷的话，当前状态 **i** 则是通过 **i-1** 房屋推出来的。根据分析，不难写出递推公式： ```dp[j]=max(dp[i-2]+nums[i],dp[i-1])```。

初始化的话，是根据递推公式来做的，将dp[0]初始化为第一个元素，dp[1]初始化为前两个元素中的最大值。



**动规五部曲**

- 打家劫舍问题
- dp数组下标以及定义:考虑下标为i（包括i）在内的房屋，能够偷窃到的最高金额为dp[i]
- 递推公式：dp[i]=max(dp[i-2]+num,dp[i-1])
- 初始化：dp[0]=0,dp[1]=max(dp[0],dp[1])
- 遍历顺序：从左到右

**代码**
```Python 
class Solution:
    def rob(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[0]*size
        if size==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,size):
            dp[i]=max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
```
### [《代码随想录》动态规划：打家劫舍II](https://notes.kamacoder.com/questions/502085)
#### 任务要求
#### 213.打家劫舍II

视频讲解：https://www.bilibili.com/video/BV1oM411B7xq 
https://programmercarl.com/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

本题的难点是首尾相连的情况讨论，最直白的思路就是将首尾情况分类讨论，根据这种分而治之的策略我们可以得到三种情况：

情况一：考虑除了尾以外的元素

情况二：考虑除开首尾的中间元素

情况三：考虑除了头以外的元素

注意：这里是考虑，并不代表选择！


**动规五部曲**

- dp数组下标以及定义: 具体的代码实现里面我们不用dp数组了，否则空间复杂度很高
- 递推公式：和打家劫舍一样，只是这里我们用的双指针来实现
- 初始化：和“打家劫舍I”逻辑一样，dp[0]=nums[0], dp[1]=max(nums[0], nums[1])
- 遍历顺序：-

**代码**
```Python 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end+1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max
```
### [《代码随想录》动态规划：打家劫舍III](https://notes.kamacoder.com/questions/502086)
#### 任务要求
#### 337.打家劫舍III

视频讲解：https://www.bilibili.com/video/BV1H24y1Q7sY 
https://programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html

##### 重要知识点

- 解题思路
- 动规五部曲

**解题思路**

1. 二叉树的遍历顺序：本题一定要用后序遍历，因为我们需要利用子节点返回值做判断
2. 打家劫舍的思路：对于每个节点都有两个状态：偷 / 不偷
3. 我们从下到上递归整颗二叉树，对于每个节点都进行判断，如果偷当前节点的话，就不偷其子节点；如果不偷当前节点的话，偷子节点。递归函数的终止条件是遇到空节点。


**代码**
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)
    def traversal(self, node):
        if not node:
            return (0,0)
        
        #后序遍历
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        #不偷当前节点，偷子节点
        val_0 = max(left[0],left[1])+max(right[0], right[1])

        #偷当前节点，不偷子节点
        val_1 = node.val+left[0]+right[0]

        return (val_0, val_1)
```

