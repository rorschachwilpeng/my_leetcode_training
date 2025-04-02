from collections import deque


di=[[0,1],[0,-1],[-1,0],[1,0]]

def bfs(grid,visited,x,y):#入参：网格，遍历过的元素，起始坐标
    #加入第一个元素
    que=deque([])
    que.append([x,y])
    visited[x][y]=True
    while(que):
        cur_x, cur_y=que.popleft()
        #遍历当前节点的上下左右
        for i,j in di:
            next_x=cur_x+i
            next_y=cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):#越界
                continue
            if not visited[next_x][next_x] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                que.append([next_x,next_y])


def main():
    #输入图
    N,M=map(int,input().strip().split())
    grid=[]

    for _ in range(N):
        s=list(map(int,input().strip().split()))
        grid.append(s)

    visited=[[False]*M for _ in range(N)]
    res=0
    for i in range(N):
        for j in range(M):
            if grid[i][j]==1 and not visited[i][j]:
                res+=1
                bfs(grid, visited, i, j)
    print(res)
    
main()
