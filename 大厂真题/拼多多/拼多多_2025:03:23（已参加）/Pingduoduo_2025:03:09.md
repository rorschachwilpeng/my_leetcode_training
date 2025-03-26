# 大厂真题
## 拼多多
### [2025年3月23日](https://codefun2000.com/p/P2736)
#### 任务要求
#### 拼多多-2025年3月23日-算法岗位-推箱子
https://codefun2000.com/p/P2736

##### 重要知识点
- 简单模拟题，没啥好说的

**代码实现**

```Python
T=int(input())

for _ in range(T):
    x,y=map(int,input().strip().split())
    ops=input().strip()
    
    for op in ops:
        if op=='W':#向上
            y+=1
        elif op=='S':#向下
            y-=1
        elif op=='A':#向左
            x-=1
        elif op=='D':#向右 
            x+=1
    
    if x==0 and y==0:
        print('YES')
    else:
        print('NO')

```

### [2025年3月23日](https://codefun2000.com/p/P2738)
#### 任务要求
#### 拼多多-2025年3月23日-算法岗位-身高排列
https://codefun2000.com/p/P2738

##### 重要知识点
- 利用单调栈来实现
- 反思

**利用单调栈来实现**

创建并维护一个单调递增（从栈底-->栈顶）的单调栈，栈中的元素代表了同学的索引。

*伪代码*
```Python
从右往左遍历同学：
    当栈中有元素而且栈顶的同学小于当前同学时候：
        弹出栈顶元素（因为这些同学都比当前同学矮）
    
    接下来我们需要计算，对于当前同学，有多少同学比他矮
    if 栈不为空的话：
        那么栈顶同学就是第一个比当前同学高同学 --> 当前同学能够看到的同学数为：stack[-1]-i (这里的计算体现了利用索引作为栈中元素的巧妙之处)
    if 栈为空的话：
        那么当前同学能看到其之后所有的同学 --> 当前同学能够看到的同学数为: n-i-1 (这里的计算体现了利用索引作为栈中元素的巧妙之处)

    累加数量
    将当前元素加入到栈中
打印结果
```



**反思**

1. 这道题过了60%的样例，主要是因为超时引起的。做的时候一直卡在重复记录元素/漏掉元素上。根本原因是因为没有想到可以利用“索引”作为栈中的元素，而是一直在尝试利用“元组（元素值，比其大的元素数量）”来做。
2. 不要死背题，而是要理解和记住本题中利用单调栈和索引来巧妙解决的思路。



**代码实现**
```Python
#维护一个单调栈
#栈中的元素代表了同学的索引，这个单调栈是一个单调递增栈（从栈尾到栈顶）
n=int(input())
h=list(map(int,input().strip().split()))
stack=[]
res=0

for i in range(n-1,-1,-1):
    cnt=0
    while stack and h[stack[-1]]<h[i]:
        stack.pop()
    if stack:
        cnt=stack[-1]-i
    else:
        cnt=n-i-1
    res+=cnt
    stack.append(i)
print(res)
```



### [2025年3月23日](https://codefun2000.com/p/P2739)
#### 任务要求
#### 拼多多-2025年3月23日-算法岗位-字符串替换
https://codefun2000.com/p/P2739

##### 重要知识点
- 其实可以算一道模拟题

**其实可以算一道模拟题**

这道题的核心其实很简单，如果想要最后S1的字典序小的话，那么就尽可能地将小的字母换到A的前面。
1. 因此，我们需要将字符串B按照字母顺序重新排序。
2. 我们需要将字符尽可能地换到字符串A中的前面的字母。为了达到这个目的，我们首先需要知道字符串A中有哪些位置的元素需要**被替换**。然后我们对需要**被替换**的元素按照索引进行重新排序，即可尽可能地将元素替换到字符串A的前面


**代码实现**
```Python
T=int(input())
for _ in range(T):
    #第一行输入n,m；n-->字符串A的长度；m-->字符串B的长度
    n,m=map(int,input().strip().split())

    strA=str(input())#字符串A
    strB=str(input())#字符串B
    
    X=list(map(int,input().strip().split()))#输入数组

    #利用一个数组来表示，数组索引代表A中元素的位置，而值代表该位置的元素需要被替换的次数
    cnt=[0]*(n+1)
    for i in X:
        cnt[i]+=1

    #再新建一个数组positions，用来记录需要被遍历的元素的位置
    positions=[]
    for j in range(1,n+1):
        if cnt[j]>0:
            positions.append(j)        
    #将positions进行排序-->代表A中需要 被替换 的元素
    positions.sort()

    #2，将B中的元素按升序排序，代表需要替换的元素
    sorted_B=sorted(strB)
    
    #进行替换
    K=len(positions)#需要被替换的元素的数量
    res=list(strA)#初始化结果字符
    for i in range(K):
        pos=positions[i]#需要被替换的位置 from A
        res[pos-1]=sorted_B[i]#替换的元素 from B
    print(''.join(res))
```