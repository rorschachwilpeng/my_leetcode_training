# Blind75
## Blind75：#1 两数之和
### #1 两数之和
#### 任务要求
https://leetcode.cn/problems/two-sum/description/
##### 重要知识点
- 考查知识点
- 解法
- 暴露的问题
- 衍生题目

**考查知识点**

哈希表。之所以选择哈希表是因为本题中的数组是无序的，如果利用双指针来解的话，先要对数组进行排序（时间复杂度O(nlog(n))），整个算法的时间复杂度为O(nlog(n))。而利用哈希法的话只需要对数组进行一次遍历即可，时间复杂度为O(n)。
	
**解法**

*双指针解法*
```Python 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #排序法
        nums_sorted=[(idx,val) for idx,val in enumerate(nums)]
        nums_sorted.sort(key=lambda x:x[1])
        l,r=0,len(nums_sorted)-1
        while l<r:
            tmp=nums_sorted[l][1]+nums_sorted[r][1]
            if tmp<target:
                l+=1
            elif tmp>target:
                r-=1
            else:
                return [nums_sorted[l][0],nums_sorted[r][0]]
```
*哈希解法*
```Python 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #哈希法
        seen={}#key:元素值；value:元素在数组中的索引
        for idx,num in enumerate(nums):
            if target-num in seen:#如果互补元素存在
                return [seen[target-num],idx]
            else:#如果互补元素不存在
                #将当前元素加入seen
                seen[num]=idx
```


**暴露的问题**
1. 对二分法使用的场景不熟悉；
2. 对双指针和二分法的区别掌握不熟悉


什么时候用二分法？

1. 单调，有序；
2. 在有序数组中查找某个值；
3. 或者是在数组中找一个/最后一个满足某个条件的位置；
4. 判断两个元素的时候不能用二分法


**衍生题目**
ThreeSum, FourSum


---

## Blind75：#128 最长连续序列
### #128 最长连续序列
#### 任务要求
https://leetcode.cn/problems/longest-consecutive-sequence/
##### 重要知识点
- 考查知识点
- 窗口压缩的范式
- 解法
- 暴露的问题
- 衍生题目

**考查知识点**
窗口压缩+状态更新的while循环

**窗口压缩的范式**
这个两层循环的方法可以总结为一个通用的结构模式：窗口压缩 + 状态更新型while循环
```Python
for right in range(n):
    #右指针扩展窗口（进入新状态）

    while 不满足状态:
        #左指针压缩窗口（移除旧状态）
```

**解法**

```Python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #去重
        set_nums=set(nums)
        ans=0

        # 这个两层循环的方法可以总结为一个通用的结构模式：窗口压缩 + 状态更新型while循环
        # for right in range(n):
        #     #右指针扩展窗口（进入新状态）

        #     while 不满足状态:
        #         #左指针压缩窗口（移除旧状态）

        for num in set_nums:
            if num-1 not in set_nums:#这行代码保证了：我们永远只从连续序列的起点开始拓展
                current_num=num
                current_ans=1

                while current_num+1 in set_nums:
                    current_num+=1
                    current_ans+=1
                ans=max(current_ans,ans)
        return ans
```

**暴露的问题**
1. 对于set的使用理解不够透彻，set除了去重以外，还能降低“增加元素”和“删除元素”的时间复杂度；



----

## Blind75：#3. 无重复字符的最长子串
### #3 无重复字符的最长子串
#### 任务要求
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
##### 重要知识点
- 考查知识点
- 解法
- 暴露的问题
- 衍生题目

**考查知识点**
窗口压缩+状态更新的while循环。这道题其实和#128那道题很像的。#128是尽可能小地压缩滑动窗口，#3是尽可能大地拓展滑动窗口


**解法**

```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口，但是基于set实现
        #之所以基于set实现而不是list数组的原因：set增删的效率为O(1)，而list为O(n)
            #基于list的话，时间复杂度会退化为O(n^2)
        lookup=set()
        res=0
        left=0
        current_len=0

        for l in s:
            current_len+=1
            while l in lookup:#如果当前元素重复，压缩左边窗口
                lookup.remove(s[left])
                left+=1
                current_len-=1
            lookup.add(l)
            res=max(res,current_len)
        return res

```

**暴露的问题**
1. 对于set的使用理解不够透彻，set除了去重以外，还能降低“增加元素”和“删除元素”的时间复杂度；




---


## Blind75：#261. 以图判树
### #261. 以图判树
#### 任务要求
https://leetcode.cn/problems/graph-valid-tree/
##### 重要知识点
- 考查知识点
- 解法
- 暴露的问题
- 衍生题目

**考查知识点**
1. 选择哪种数据结构来存储图；
    这里选用邻接图最好；另外两个可能的选择包括邻接矩阵和链表。邻接矩阵通常在边的数量远大于节点数量时候才用。ChatGPT说LeetCode上大部分的题目都是利用邻接表来解决，fine。

2. 树的合法性的判断条件：
    官方说的是两个条件，但是我个人觉得用三个条件来描述更加准确：
    2.1. 边的数量 == 节点数量 - 1
    2.2. 没有环
    2.3. 整颗树是可达的，即可以从头到尾遍历访问所有的节点
    
3. 如何构建递归来遍历整颗树
    这是本题的难点，因为本题中构建的是无向图，所以我们在单次遍历逻辑中需要对父子节点之间的双向连接（平凡环）情况做特殊处理
    
    递归的伪代码逻辑如下：
    ```Python
    def dfs(node, parent):#入参是当前节点与父节点
        #是否遍历过当前节点
            #遍历过的话直接跳过
        #否则将节点加入到seen（遍历过的元素的集合）
        
        #遍历当前节点的邻居
            #跳过父子节点之间的平凡环
            #如果有非平凡环的话，返回False
            #继续向下递归 -- dfs(neighbour, node)
        return True#遍历到底的话，说明可达性是ok的，递归向上返回结果
    ```

**解法**

```Python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #判断树合法性的两个条件
            #1.没有环
            #2.边的数量==节点数量-1
            #3.树是连通的，遍历的话可以从头到尾

        #首先判断边
        if len(edges)!=n-1:return False

        #构建邻接图
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen=set()

        def dfs(node,parent):#入参：当前节点与父节点
            if node in seen: return#跳过已经遍历过的节点
            seen.add(node)#将当前节点加入seen
            
            #遍历当前节点的邻居节点
            for neighbour in graph[node]:
                if neighbour==parent:#如果邻居节点和父节点之间存在平凡环
                    continue#跳过
                if neighbour in seen:#如果邻居节点已经在seen中出现过了
                    return False#这是一个环，返回False
                #继续向下递归遍历
                ressult=dfs(neighbour,node)
                if not ressult:return False
            return True
        
        #如果到底+无环的话
        return dfs(0,-1) and len(seen)==n
        

```

**暴露的问题**
1. 图论还够得刷呢，对于dij我也还没学呢，这道题还可以用并查集来做，迭代法也没掌握。。。明天继续深挖这道题


