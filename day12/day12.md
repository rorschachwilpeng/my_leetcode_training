# 代码随想录
## 栈与队列
### 《代码随想录》栈与队列：前K个高频元素
#### 任务要求
#### 347.前 K 个高频元素  （有点难度，可能代码写不出来，一刷至少需要理解思路）

大/小顶堆的应用， 在C++中就是优先级队列 

本题是 大数据中取前k值 的经典思路，了解想法之后，不算难。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html

##### 重要知识点
- 优先级队列的概念
- 大顶堆和小顶堆的概念
- Python中的小顶堆
	- `headq.heappush()`的入参说明
	- Python中`heapq`默认小顶堆的属性

**优先级队列的概念**

优先级队列是一种特殊的队列数据结构，其中元素的出队顺序不是按照插入顺序，而是按照优先级来决定的：
- **高优先级的元素先出队**。
- 可以用堆来高效实现优先级队列，堆的性质保证了每次出队操作都是当前优先级最高或最低的元素。

	常见的应用场景：
	- 任务调度（如操作系统中任务的优先级处理）。
	- 动态获取数据流中的最大值或最小值（如实时数据流中的前 K 大问题）。
	- 图算法（如 Dijkstra 最短路径、Prim 最小生成树）。

**大顶堆和小顶堆的概念**

**堆**是一种特殊的完全二叉树，可以用数组高效表示。根据堆顶元素的大小关系，堆分为两种：
1. **大顶堆（Max Heap）**：
	- 每个父节点的值都大于或等于其子节点的值。
	- 堆顶是整个堆中的最大值。
	- 常用于动态获取最大值的场景。
2. **小顶堆（Min Heap）**：
	- 每个父节点的值都小于或等于其子节点的值。
	- 堆顶是整个堆中的最小值。
	- 常用于动态获取最小值的场景。
	- **Python 的 `heapq` 模块默认实现的是小顶堆。**
 
 **Python中小顶堆的实现方式**
 
 Python提供了内置的`heaq`模块，用于实现堆操作。
1. `heapq.heappush()`的入参说明

	`heapq.heappush()`是用来向堆中插入元素的函数，保持堆的性质不变（即最小堆的堆顶是最小值）。
	```
	heapq.heappush(heap, item)
	```
	- **`heap`**：
		- 表示目标堆，必须是一个列表（`list`）。
		- 该列表需要事先满足堆的性质。
		- 如果列表不是堆，调用 `heappush` 后堆的性质将不被保证。
	- **`item`**：
		- 要插入堆的元素。
		- `heapq` 会根据堆的规则自动将该元素放到合适的位置。
		- 如果`item`为元组，堆会按照元组中第一个元素大小进行排序。

	示例：
	```
	import heapq

	heap = []  # 创建一个空堆
	heapq.heappush(heap, 5)
	heapq.heappush(heap, 2)
	heapq.heappush(heap, 8)
	print(heap)  # 输出: [2, 5, 8]，堆顶始终是最小值
	```

2. Python中`heapq`默认小顶堆的属性
- **默认实现为最小堆**：
	- 堆顶元素是当前堆中的最小值。
	- 对于动态获取最小值的问题，可以直接使用默认的 `heapq`。
- **实现大顶堆的方法**：
	- Python 没有直接支持大顶堆的功能，但可以通过对元素的值取反来间接实现：
		 ```
		import heapq
		heap = []  # 模拟大顶堆
		heapq.heappush(heap, -5)  # 插入 -5
		heapq.heappush(heap, -2)  # 插入 -2
		heapq.heappush(heap, -8)  # 插入 -8
		print(-heapq.heappop(heap))  # 输出: 8，堆顶是最大值
		```
- **时间复杂度**：
	- 插入和删除操作的时间复杂度为 O(log⁡n)，其中 nnn 是堆的大小。
	- 构造堆的时间复杂度为 O(n)。

**代码**
```Python 
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #构造词典
        wordDic=defaultdict(int)
        for num in nums:
            wordDic[num]+=1

        #构造小顶堆（优先级队列），大小为k
        pri_que=[]
        for key,val in wordDic.items():
            heapq.heappush(pri_que, (val,key))
            if len(pri_que)>k:
                heapq.heappop(pri_que)


        #从小顶堆中弹出元素
        res=[0]*k
        for idx in range(k-1,-1,-1):
            res[idx] = heapq.heappop(pri_que)[1]
        return res
```


