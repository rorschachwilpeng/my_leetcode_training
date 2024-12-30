# 代码随想录
## 哈希表
### 《代码随想录》哈希表：有效的字母异位词
#### 任务要求
#### 242.有效的字母异位词

建议： 这道题目，大家可以感受到 数组 用来做哈希表 给我们带来的便利之处。 

题目链接/文章讲解/视频讲解： https://programmercarl.com/0242.%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.html

##### 重要知识点
- 哈希表的不同数据结构实现
- 本题解题思路

**哈希表的不同数据结构实现**

哈希表三种数据结构：
1. 数组:通常用于范围可控的情况；
2. set：通常用于范围很大的情况；
3. dict：通常用于key和value的情况；

- 拓展知识点： python中的ord()函数，可以直接返回一个字符（字符串）的整形表示


**本题解题思路**

这道题的核心是判断两个字符串是否是字母异位词，可以通过哈希表统计字符频次来实现。具体步骤如下：
1. 构造一个长度为 26 的数组 `hashList`，对应字母表的 26 个字母，初始值均为 0。
2. 遍历字符串 `s`，根据字符的索引（通过 `ord(letter) - ord('a')` 计算）更新哈希表，增加对应字符的频次。
3. 遍历字符串 `t`，对应索引位置的频次减 1。
4. 最后检查哈希表，若所有值都为 0，则 `t` 是 `s` 的字母异位词，否则不是。

这种方法的时间复杂度为 O(n)，空间复杂度为 O(1)（常数级空间）。

**代码**
```Python 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        NUM_OF_ALPHABET=26
        NO_ITEMS=0
        hashList=[0]*NUM_OF_ALPHABET

        for letter in s:
            idx=ord(letter)-ord('a')
            hashList[idx]+=1

        for letter in t:
            idx=ord(letter)-ord('a')
            hashList[idx]-=1

        return True if any(hashList)==NO_ITEMS else  False
```

### 《代码随想录》哈希表：两个数组的交集
#### 任务要求
####  349. 两个数组的交集

建议：本题就开始考虑 什么时候用set 什么时候用数组，本题其实是使用set的好题，但是后来力扣改了题目描述和 测试用例，添加了 0 <= nums1[i], nums2[i] <= 1000 条件，所以使用数组也可以了，不过建议大家忽略这个条件。 尝试去使用set。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0349.%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.html

##### 重要知识点
- set的实现

**set实现**

根据题意，不难利用set的特性找到每个数组中的唯一值，然后将公共值加入结果数组中。

```Python 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=set(nums1)
        n2=set(nums2)
        res=[]
        for n in n1:
            if n in n2:
                res.append(n)
        return res
```

### 《代码随想录》哈希表：快乐数
#### 任务要求
#### 202. 快乐数

建议：这道题目也是set的应用，其实和上一题差不多，就是 套在快乐数一个壳子 

题目链接/文章讲解：https://programmercarl.com/0202.%E5%BF%AB%E4%B9%90%E6%95%B0.html

##### 重要知识点
- 解题思路
- 循环结束条件

**解题思路**
1. 构造循环来判断数字是否为快乐数
2. 循环中，每次将数字转换为字符串以方便拆分。计算拆分后数字的平方和，同时记录下平方和，直到找到快乐数/陷入无限循环。

**循环结束条件**

其实题目中已经给了提示，**“无限循环”**。这意味着如果一个数不是快乐数，那么进行如此循环最终会和之前某一次的计算平方和重复。所以我们只需要维护一个全局记录数组，用于记录已经出现过的值，当平方和在找到快乐数之前出现重复，返回`False`。

**代码**
```Python 
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        while n!=1:
            n=sum(int(num)**2 for num in str(n))
            if n in seen:
                return False
            seen.append(n)
        return True
```

### 《代码随想录》哈希表：两数之和
#### 任务要求
#### 1. 两数之和

建议：本题虽然是 力扣第一题，但是还是挺难的，也是 代码随想录中 数组，set之后，使用map解决哈希问题的第一题。 

建议大家先看视频讲解，然后尝试自己写代码，在看文章讲解，加深印象。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html

##### 重要知识点
- 什么时候用哈希法？
- 解题思路
- 时间&空间复杂度

**什么时候用哈希法**

当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候，就要第一时间想到哈希法。

**解题思路**
- **利用哈希集合（`set`）加速查找**：
	- 通过一个集合 `seen` 动态维护已遍历的元素。
	- 对于当前元素 `val`，计算目标差值 `complement = target - val`。
	- 检查差值 `complement` 是否已经出现在集合 `seen` 中：- 如果存在，则说明找到一组满足条件的数对，返回它们的索引。
		- 如果不存在，将当前元素加入集合，继续遍历。
- **索引的获取**：
	- 在找到满足条件的数对后，通过 `nums.index(complement)` 获取差值的索引，并返回结果。

**时间复杂度**
- 遍历数组一次，时间复杂度为 O(n)。
- 集合的查找和插入操作平均时间复杂度为 O(1)，整体复杂度为O(n)。
 
	
**空间复杂度**： 使用一个集合 `seen` 存储已遍历的元素，空间复杂度为 O(n)。

**代码**
```Python 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        for idx,val in enumerate(nums):
            complement=target-val
            if complement in seen:
                return [nums.index(complement),idx]
            seen.add(val)
```