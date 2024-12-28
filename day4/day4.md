# 代码随想录
## 链表
### 《代码随想录》链表：两两交换链表中的节点
#### 任务要求
#### 24. 两两交换链表中的节点

用虚拟头结点，这样会方便很多。 

本题链表操作就比较复杂了，建议大家先看视频，视频里我讲解了注意事项，为什么需要temp保存临时节点。

题目链接/文章讲解/视频讲解： https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html

视频讲解：https://www.bilibili.com/video/BV1tZ4y1q7XE
##### 重要知识点
- 基于“虚拟头节点”的两两交换思路
- 循环条件

**基于“虚拟头节点”的两两交换思路**
![截屏2024-12-28 09.21.58.png](http://cdn.kamacoder.com/676fc33982bdc-phpvBf7Jh.png) 

**具体代码实现中的知识点**
- 注意在while循环的判断条件中，要先判断`cur.next`不为空，再判断`cur.next.next`。
- 因为假设遍历到最后一个节点，此时需要退出循环。如果没有`cur.next`的话，`cur.next.next`判断条件会直接操作空指针，从而报错。

**代码**
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy_head=ListNode(next=head)
        cur=dummy_head
        while cur.next and cur.next.next:#非常tricky的循环条件
            #缓存节点
            tmp1=cur.next
            tmp2=cur.next.next.next
            
            cur.next=cur.next.next#第一步
            cur.next.next=tmp1#第二步
            cur.next.next.next=tmp2#第三步

            cur=cur.next.next#更新指针位置
        return dummy_head.next
```

### 《代码随想录》链表：删除链表的倒数第N个节点
#### 任务要求
#### 19.删除链表的倒数第N个节点

双指针的操作，要注意，删除第N个节点，那么我们当前遍历的指针一定要指向 第N个节点的前一个节点，建议先看视频。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.html

视频讲解：https://www.bilibili.com/video/BV1tZ4y1q7XE
##### 重要知识点
- 快慢指针的思路
- 为什么需要‘虚拟头节点’

**快慢指针的思路**

快指针先走n步，然后快慢指针再一起走。两个指针步长都为1，当快指针遍历结束时，慢指针所指向的位置即需要删除的“倒数第n个节点”

**为什么需要‘虚拟头节点’**

避免需要对删除头节点的情况单独进行处理，从而优化了代码

**代码**
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        slow=dummy_head
        fast=dummy_head
        
        #快指针先走n步
        for _ in range(n):
            fast=fast.next
        
        #两个指针一起走
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        #删除倒数第n个节点
        slow.next=slow.next.next
        return dummy_head.next
```

### 《代码随想录》链表：链表相交
#### 任务要求
#### 面试题 02.07. 链表相交

本题没有视频讲解，大家注意 数值相同，不代表指针相同。

题目链接/文章讲解：https://programmercarl.com/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.html
##### 重要知识点
- ‘快慢指针’解题思路

**‘快慢指针’解题思路**
对于两个链表中，长度更长的链表（快指针）先走长度差单位的距离。然后两个链表（快&慢指针）同行，当两指针相同时候，说明找到了交点。否则，没有交点。

	1.获取两个链表的长度

	2.定义快慢指针，快指针指向长链表，慢指针指向短链表

	3.快指针先行“两个链表长度差”单位个的距离

	4.两个指针一起走，当指针相同时 --> 找到起始节点


**代码**
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getLen(self,head):
        l=0
        while head:
            head=head.next
            l+=1
        return l
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #获取两个链表的长度
        la = self.getLen(headA)
        lb = self.getLen(headB)
        dis=abs(la-lb)#长度差

        #快指针先行“两个链表长度差”单位个的距离
        for _ in range(dis):
            if la>lb:
                headA=headA.next
            elif la<lb:
                headB=headB.next
        
        #两个指针一起走，当指针相同时 --> 找到起始节点
        while headA and headB:
            if headA==headB:#找到交点
                return headA

            headA=headA.next
            headB=headB.next
            
        return None#没有交点
```

### 《代码随想录》链表：环形链表II
#### 任务要求
#### 142.环形链表II

算是链表比较有难度的题目，需要多花点时间理解 确定环和找环入口，建议先看视频。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html
##### 重要知识点
-  找到环的思路
- 代码实现

**找到环的思路**
![截屏2024-12-28 10.29.28.png](http://cdn.kamacoder.com/676fd30bb0f2f-phpszmVUo.png) 
- 如果定义一对快慢指针，快指针步长（速度）为2，慢指针步长（速度）为1。如果有环的话，两个指针一定会相遇（联想一下环形操场跑步）。我们假设相遇点为图中的`y`点。

- 当两个指针相遇时候，慢指针走过的距离为:`x+y`，快指针走过的距离为: ` x+y + n*(y+z)`（`n`代表快指针在相遇前在圈内已经走了几圈）。

- 因为`路程=速度*时间`，且对于快慢指针而言：`时间相同`，`速度=1:2（慢指针：快指针）`。可推`路程=2:1（慢指针：快指针）`。

- 所以我们可以得到公式：`2(x+y) = x+y + n*(y+z)` 

- 对公式进行化简：`2(x+y) = x+y + n*(y+z)` --> `x+y = n*(y+z)` --> `x+y = (n-1)*(y+z) + (y+z)` --> `x = (n-1)(y+z)+z` 

 - 对于公式 `x = (n-1)(y+z)+z` ，当`n==1`时（快指针在环内转了一圈），我们不难得到 `x=z`。这个推导公式意味着**从相遇节点和初始节点同时出发一个步长相同的节点，当它们相遇时，相遇节点即环的入口**。

**代码实现**
1. 构造快慢指针
2. 通过快慢指针，找到相遇节点
3. 相遇节点和初始节点同时出发一个步长相同的节点，当它们相遇时，相遇节点即环的入口

**代码**
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:#找到相遇节点
                slow=head#从初始节点重新出发
                while slow and fast:
                    if slow==fast:#找到环的入口
                        return slow
                    slow=slow.next
                    fast=fast.next#从相遇节点重新出发
        return None#没有环
```

