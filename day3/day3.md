# 代码随想录
## 链表
### 《代码随想录》链表：移除链表元素
#### 任务要求
#### 203.移除链表元素

建议： 本题最关键是要理解 虚拟头结点的使用技巧，这个对链表题目很重要。

题目链接/文章讲解/视频讲解：：https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.htm

##### 重要知识点
- 虚拟头节点
	1. 为什么需要虚拟头节点
	2. 如何实现
- 尾节点的处理
- 调试发现的行为

**虚拟头节点**

虚拟头节点是人为创建的一个节点，用于简化链表操作。
1. 为什么需要虚拟头节点？

		如果需要删除链表的头节点（首节点），没有虚拟头节点时需要单独处理逻辑。通过设置虚拟头节点，可以保证循环逻辑的统一性，避免特殊情况处理。
2. 如何实现？

		创建一个新节点 `dummy_head`，其 `next` 指针指向链表的头节点。

**尾节点的处理**

如果最后一个节点需要删除，虚拟头节点依然有效。
1. **为什么将虚拟头节点赋值给 cur 可以处理尾节点删除？**

	虚拟头节点通过 `dummy_head.next` 管理整个链表。 即使尾节点被删除，链表的引用依然通过虚拟头节点保留。
	
2. **为什么直接用 `head` 赋值给 cur 不行？**

	`head` 是链表的起点，删除头节点后需要单独更新 `head`，而虚拟头节点则不需要。

**调试发现的行为**
 
- `cur = cur.next` 逻辑：仅改变 `cur` 的指针指向，不会修改链表结构。

- `cur.next = cur.next.next` 逻辑：修改了链表节点的 `next` 指针，跳过当前节点，直接影响链表结构。

**代码**		
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None
        dummy_head=ListNode(next=head)
        cur=dummy_head
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy_head.next
```

### 《代码随想录》链表：设计链表
#### 任务要求
#### 707.设计链表

建议： 这是一道考察 链表综合操作的题目，不算容易，可以练一练 使用虚拟头结点

题目链接/文章讲解/视频讲解: https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html
##### 重要知识点
～

**代码**
```Python 
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    #需要创建一个指针来遍历链表的原因：
    # 因为操作完链表后，需要返回头节点
    # 如果上来就操作头节点，之后无法返回头节点
    #单链表
    def __init__(self):
        self.dummy_head=ListNode()
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>self.size:
            return -1
        cur=self.dummy_head.next
        for _ in range(index):
            cur=cur.next
        return cur.val
     
        
    def addAtHead(self, val: int) -> None:
        newHead=ListNode(next=self.dummy_head.next)#新节点
        self.dummy_head.next=newHead#更新新头节点和虚拟头节点关系
        self.size+=1
      
      
    def addAtTail(self, val: int) -> None:
        newNode=ListNode(val)
        cur=self.dummy_head
        while cur.next:
            cur=cur.next
        cur.next=newNode
        self.size+=1
       
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        cur=self.dummy_head
        for _ in range(index):
            cur=cur.next
        cur.next=ListNode(val,next=cur.next)
        self.size+=1
       
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>self.size:
            return
        cur=self.dummy_head
        for _ in range(index):
            cur=cur.next
        cur.next=cur.next.next#删除索引为index节点
        self.size-=1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

### 《代码随想录》链表：翻转链表
#### 任务要求
#### 206.反转链表

建议先看我的视频讲解，视频讲解中对 反转链表需要注意的点讲的很清晰了，看完之后大家的疑惑基本都解决了。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html

##### 重要知识点
-  双指针思想

**双指针思想**

构造两个指针，一前一后，初始位置分别是`None`和`head`。两个指针从左往右进行移动，每次移动前需缓存下一个节点指针，然后翻转当前两个指针，再更新双指针的位置。最后当‘后指针’遍历到末尾`None`位置时，返回'前指针'即翻转链表。

**代码**
```Python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #双指针
        prev=None
        cur=head
        while cur:
            tmp=cur.next#缓存下一个节点
            cur.next=prev#翻转指针
            prev=cur#更新双指针
            cur=tmp
        return prev
```

