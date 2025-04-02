# 代码随想录
## 图论
### 《代码随想录》图论：DFS模版
#### 任务要求
##### DFS模版

##### 重要知识点
- DFS模版


**DFS模版**

DFS就是不撞南墙不回头

```Python

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 四个方向：上、右、下、左


def dfs(grid, visited, x, y):
    """
    对一块陆地进行深度优先遍历并标记
    """
    for i, j in direction:
        next_x = x + i
        next_y = y + j
        # 下标越界，跳过
        if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
            continue
        # 未访问的陆地，标记并调用深度优先搜索
        if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
            visited[next_x][next_y] = True
            dfs(grid, visited, next_x, next_y)


if __name__ == '__main__':  
    # 版本一
    n, m = map(int, input().split())
    
    # 邻接矩阵
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # 访问表
    visited = [[False] * m for _ in range(n)]
    
    res = 0
    for i in range(n):
        for j in range(m):
            # 判断：如果当前节点是陆地，res+1并标记访问该节点，使用深度搜索标记相邻陆地。
            if grid[i][j] == 1 and not visited[i][j]:
                res += 1
                visited[i][j] = True
                dfs(grid, visited, i, j)
    
    print(res)
```

# 代码随想录
## 图论
### 《代码随想录》图论：BFS模版
#### 任务要求
##### BFS模版

##### 重要知识点
- BFS模版


**BFS模版**

```Python
from collections import deque


#需要定义四个方向
di=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(grid,visited,x,y):
    que=deque([])
    que.append([x,y])
    while(que):
        cur_x,cur_y=que.popleft()
        for x_move,y_move in di:
            next_x=cur_x+x_move
            next_y=cur_y+y_move

            #判断是否越界
            if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                continue
            
            #如果没有越界 & 没有访问过 & 是岛屿的话（这里和main函数中的判断条件虽然一样，但是含义却不同。这里的含义是将已经判定为岛屿所包含的岛屿面积全部mark掉）
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                que.append([next_x,next_y])
                

def main():
    N,M=map(int,input().strip().split())
    grid=[]
    visited=[[False]*M for _ in range(N)]
    for _ in range(N):
        grid.append(list(map(int,input().strip().split())))
    res=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j]==1:#如果找到一个岛屿的话
                res+=1#更新岛屿数量
                bfs(grid,visited,i,j)#利用BFS来查询该岛屿所包含的面积，将属于该岛屿的面积全部mark掉
    print(res)


main()

```





