#怎么将孤岛标记出来？


#慢就是快
#Step1:遍历一遍地图，然后将和周边相连的陆地标记为2
#Step2:再遍历一边地图，将值为2的陆地调整为1，将值为1的陆地调整为0


di=[[0,1],[0,-1],[1,0],[-1,0]]
boundary=False

def dfs(grid,x,y):
    grid[x][y]=2
    for i,j in di:
        next_x=x+i
        next_y=y+j

        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
            continue

        #Step1:遍历一遍地图，然后将和周边相连的陆地标记为2
        if grid[next_x][next_y]==1:
            dfs(grid,next_x,next_y)
    



def main():
    global boundary
    N,M=map(int,input().strip().split())
    grid=[]
    for _ in range(N):
        grid.append(list(map(int,input().strip().split())))
    visited=[[False]*M for _ in range(N)]
    
    #从上下左右四个周边
    for i in range(N):#从左和右
        if grid[i][0]:#左边
            dfs(grid,i,0)
        if grid[i][M-1]:#右边
            dfs(grid,i,M-1)
    
    for j in range(M):#从上和下
        if grid[0][j]:#上边
            dfs(grid,0,j)
        if grid[N-1][j]:#下边
            dfs(grid,N-1,j)

    #Step2:再遍历一边地图，将值为2的陆地调整为1，将值为1的陆地调整为0
    for i in range(N):
        for j in range(M):
            if grid[i][j]==2:#将周边陆地标记为1
                grid[i][j]=1
            elif grid[i][j]==1:#将孤岛标记为0
                grid[i][j]=0
    
    for i in range(N):
        print(" ".join(map(str,grid[i])))
        


main()