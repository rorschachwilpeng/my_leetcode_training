# 大厂真题
## 华为
### [2025年2月19日](https://notes.kamacoder.com/questions/502144)
#### 任务要求
#### 华为-2025年2月19日-留学生-觅食回家路

https://codefun2000.com/p/P2653

##### 重要知识点
- 解题思路
- 重要知识点


**解题思路**

一道DFS的模版模拟题，但是还是有需要注意的知识点



**重要知识点**
1. 记得DFS模版中需要构建遍历表来记住遍历过的格子，从而避免重复遍历；
2. 在遍历过程中，如果当前格子是食物，那么我们不仅需要增加收集的食物数量，还需要修改掉当前格子的值；
3. 每次递归遍历最后需要进行回溯；回溯操作包括取消标记，恢复食物（如果遍历的格子是食物的话）



```Python
import sys
sys.setrecursionlimit(10**7)

def dfs(x, y, collected):
    """
    x, y: 当前坐标
    collected: 当前已收集的食物数量
    """
    global path_count, total_foods

    # 如果到达家（1），且已收集所有食物，则找到一条可行路径
    if x==home_x and y==home_y and collected==total_foods:
        path_count+=1

    # 记录当前格子的原始值-->简化代码
    old_val=grid[x][y]

    # 如果是食物(2)，收集食物
    # TODO: 如果当前格子是食物，则增加收集数量，并临时修改其值
    if grid[x][y]==2:
        collected+=1
        grid[x][y]=0

    # 标记为已访问
    visited[x][y]=True

    # 尝试向四个方向移动（上、下、左、右）
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:# 边界检查
            if not visited[nx][ny] and grid[nx][ny] != 3:
                # 若未访问且不是障碍(3)，则继续 DFS
                dfs(nx,ny,collected)

    # 回溯：恢复现场
    visited[x][y]=False
    if old_val==2:
        grid[x][y]=2

def solve():
    global m, n, grid, visited
    global start_x, start_y, home_x, home_y
    global path_count, total_foods

    # 读取行列大小
    m,n=map(int,input().strip().split())

    # 读取地图
    grid=[]
    for i in range(m):
        row=list(map(int,input().split()))
        grid.append(row)

    # 初始化数据
    visited=[[False]*n for _ in range(m)]
    path_count=0
    total_foods=0

    # 找到起点(0)、家(1)以及食物总数(2)
    for i in range(m):
        for j in range(n):
            #起始位置
            if grid[i][j]==0:
                start_x,start_y=i,j
            #家的位置
            elif grid[i][j]==1:
                home_x,home_y=i,j
            #食物位置
            elif grid[i][j]==2:
                total_foods+=1

    # 从起点开始 DFS
    dfs(start_x,start_y,0)

    # 输出可行路径的数量
    print(path_count)

# 若是直接运行此脚本，可在此调用 solve()
if __name__ == "__main__":
    solve()
```



### [2025年2月19日](https://notes.kamacoder.com/questions/502144)
#### 任务要求
#### 华为-2025年2月19日-留学生-魔法链表

https://codefun2000.com/p/P2653

##### 重要知识点
- 解题思路
- 重要知识点


**解题思路**

我觉得这道题算是模拟题,题目中虽然明确了链表，但是我们其实利用字典来实现数据结构反而比较容易。

整道题的思路如下
```
#遍历字典中的元素
    #创建一个结果数组（类似于BFS的层序遍历）
    #遍历链表
        #如果数字以x结尾的话，将其加y
            #判断这个数字是否还在这链表中
            #如果在的话
                #不操作
            #如果不在的话
                #加入appended数组
        #否则-->跳过
    #将新的数组加入到结果数组中

#将appended数组中的值加入到结果数组中
```



**重要知识点**
1. 利用字典作为数组结构来存储数据；
2. 删除元素的操作不能在原字典上直接操作，而是需要创建新的容器来存储；
3. sorted()函数的排序技巧；
4. ACM模式下的输入和输出惯例。



```Python
#首先输入要输入几行链表
m=int(input())

#输入链表，
#链表利用字典来存储，字典的key是关键字，valued是数组
#关键字通过每个链表的第一个元素计算获取得到
dic={}
for _ in range(m):
    arr=list(map(int,input().strip().split()))
    key=(arr[0]*2+1)%m
    dic[key]=arr

x,y=map(int,input().strip().split())

res={}#结果字典
appended={}#待追加的元素

for key,arr in dic.items():
    new_data=[]
    for item in arr:
        if item%10==x:#如果数字以x结尾的话，将其加y
            update=item+y
            new_key=(update*2+1)%m
            if new_key==key:
                new_data.append(update)
            else:
                if new_key not in appended:
                    appended[new_key]=[]
                appended[new_key].append(update)
        else:#否则-->跳过
            new_data.append(item)
    res[key]=new_data

if appended:
    for key,val in appended.items():
        if key not in res:
            res[key]=[]
        res[key].extend(val)

#排序
sorted_items=sorted(res.items(),key=lambda item:(len(item[1]),item[0]))

for val in sorted_items:
    print(" ".join(map(str,val[1])))
```



### [2025年2月19日](https://codefun2000.com/p/P2653)
#### 任务要求
#### 华为-2025年2月19日-留学生-一种抢票系统
https://codefun2000.com/p/P2653

##### 重要知识点
- 解题思路
    - 订单入队
    - 助力处理
    - 票务分配

第一次做工程应用题，每个知识点都不难，但是总代码量非常吓人！

**解题思路**

可以将整道题的任务拆解成三个子任务：1. 订单入队；2.助力处理；3.票务分配

1. **订单入队**
    创建一个Orders类来维护订单的信息，类中的各个变量含义：      

    - self.uid=uid #输入的第一个元素，用户的唯一标识
    - self.orderID=orderID #输入的第三个元素，代表订单的ID
    - self.ticket=ticket #该订单要订几张票
    - self.arrivalIndex=arrivalIndex #全局索引
    
    除此之外，我们还需要以下数据结构作为容器来存储之后需要用的数据
    - orders=[] #模拟订单队列
    - orderIndexMap={}#key:订单号;value:在队列中对应的索引
    - helperUsed=set()#记录已经使用过助力的用户UID


2. **助力处理**
 对于输入是订单的情况，我们直接将数据存到容器中，对应的代码是
    ```Python
            if len(tokens)==4:#订单处理
                uid=tokens[0]#UID
                #token[1]代表标记，可以忽略
                orderID=tokens[2]#订单号
                ticket=int(tokens[3])#订了几张票
                newOrder=Order(uid, orderID, ticket, globalIndex)
                orders.append(newOrder)
                orderIndexMap[orderID]=len(orders)-1#记录当前队列中的位置(即当前列表的最后位置)
    ```

 对于输入是助力请求的情况，我们记录下数据，并判断该请求的合法性，对应代码是：
```Python
        ##助力处理
        elif len(tokens)==3:
            #这里不用声明类，而是用一个额外的数组来记录助力的信息
            helperUID=tokens[0]#助力人的UID
            targetOrderID=tokens[2]#被助力的订单号
            
            #查找目标订单是否存在
            if targetOrderID not in orderIndexMap:
                continue

            #获取目标订单在队列中的位置
            pos=orderIndexMap[targetOrderID]
            targetOrderID=orders[pos]#获取目标订单的信息

            #判断助力请求是否在订单请求后30个请求内
            if globalIndex-targetOrderID.arrivalIndex>30:
                continue

            #判断不能给自己助力
            if helperUID==targetOrderID.uid:
                continue

            #判断同一用户只能助力一次
            if helperUID in helperUsed:
                continue

            #满足条件，记录该用户已助力
            helperUsed.add(helperUID)

            #如果目标订单已经在队列头部，则无法上移
            if pos==0:
                continue

            #向前移动一位，与前一个订单交换（双指针实现）
            posPrev=pos-1
            orders[pos],orders[posPrev]=orders[posPrev],orders[pos]

            #更新交换后两个订单的映射关系-->why?
            orderIndexMap[orders[pos].orderID]=pos
            orderIndexMap[orders[posPrev].orderID]=posPrev
```

3. **票务分配**

创建一个元素值为布尔类型的数组，代表所有的订单所对应的订票状态。遍历数组并分配总票数，能够分配到票的元素标记为True，否则为False。输出时候根据布尔数组的值来决定订单抢票为“success”还是"failure"。

```Python
    ##票数分配:按照最终余票来分配
    remaining=tottalTickets
    isSuccess=[]#存储每个订单是否订票成功

    #录入信息
    for order in orders:
        if order.ticket<=remaining:
            isSuccess.append(True)
            remaining-=order.ticket
        else:
            isSuccess.append(False)
    
    #输出信息
    for i in range(len(orders)):
        result="success" if isSuccess[i] else "failure"
        print(f"{orders[i].uid} {orders[i].orderID} {orders[i].ticket}
```


**代码实现**
```Python
class Order:
    def __init__(self, uid, orderID, ticket, arrivalIndex):
        self.uid=uid#输入的第一个元素，用户的唯一标识
        self.orderID=orderID#输入的第三个元素
        self.ticket=ticket#订单的唯一标识
        self.arrivalIndex=arrivalIndex#全局索引

def main():
    tottalTickets=int(input())#读取总票数
    orders=[]#模拟订单队列
    orderIndexMap={}#订单号-->当前再队列中的索引-->感觉并不是必须的
    helperUsed=set()#记录已经使用过助力的用户UID

    globalIndex=0#请求全局序号

    ##订单入队
    while True:
        try:
            line=input().strip()#读取一行输入
        except EOFError:
            break#当没有更多输入时，跳出循环
        
        if not line:
            continue
        globalIndex+=1#当前请求序号
        tokens=line.split()
        if len(tokens)==4:#订单处理
            uid=tokens[0]#UID
            #token[1]代表标记，可以忽略
            orderID=tokens[2]#订单号
            ticket=int(tokens[3])#订了几张票
            newOrder=Order(uid, orderID, ticket, globalIndex)
            orders.append(newOrder)
            orderIndexMap[orderID]=len(orders)-1#记录当前队列中的位置(即当前列表的最后位置)

        ##助力处理
        elif len(tokens)==3:
            #这里不用声明类，而是用一个额外的数组来记录助力的信息
            helperUID=tokens[0]#助力人的UID
            targetOrderID=tokens[2]#被助力的订单号
            
            #查找目标订单是否存在
            if targetOrderID not in orderIndexMap:
                continue

            #获取目标订单在队列中的位置
            pos=orderIndexMap[targetOrderID]
            targetOrderID=orders[pos]#获取目标订单的信息

            #判断助力请求是否在订单请求后30个请求内
            if globalIndex-targetOrderID.arrivalIndex>30:
                continue

            #判断不能给自己助力
            if helperUID==targetOrderID.uid:
                continue

            #判断同一用户只能助力一次
            if helperUID in helperUsed:
                continue

            #满足条件，记录该用户已助力
            helperUsed.add(helperUID)

            #如果目标订单已经在队列头部，则无法上移
            if pos==0:
                continue

            #向前移动一位，与前一个订单交换（双指针实现）
            posPrev=pos-1
            orders[pos],orders[posPrev]=orders[posPrev],orders[pos]

            #更新交换后两个订单的映射关系-->why?
            orderIndexMap[orders[pos].orderID]=pos
            orderIndexMap[orders[posPrev].orderID]=posPrev

    ##票数分配:按照最终余票来分配
    remaining=tottalTickets
    isSuccess=[]#存储每个订单是否订票成功

    #录入信息
    for order in orders:
        if order.ticket<=remaining:
            isSuccess.append(True)
            remaining-=order.ticket
        else:
            isSuccess.append(False)
    
    #输出信息
    for i in range(len(orders)):
        result="success" if isSuccess[i] else "failure"
        print(f"{orders[i].uid} {orders[i].orderID} {orders[i].ticket} {result}")
        
main()
```

