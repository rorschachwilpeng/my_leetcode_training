##并查集
#1.初始化
#2.计算相似度
#3.相似度排序
#4.输出结果


#并查集的class

class unionFind:
    def __init__(self,n):
        self.father=list(range(n+1))

    def find(self,u):
        if u!=self.father[u]:
            self.father[u]=self.find(self.father[u])#路径压缩
        return self.father[u]
    
    def isSame(self,u,v):
        u=self.find(u)
        v=self.find(v)
        return u==v
    
    def join(self,u,v):#将u->v加入到集合
        fax=self.find(u)
        fay=self.find(v)
        if fax==fay:
            return
        self.father[fax]=fay

def main():
    #输入
    n=int(input().strip())
    matrix=[list(map(int,input().strip().split())) for _ in range(n)]
    uf=unionFind(n)
    ans=[0]*(n+1)

    #读取相似度矩阵并构建并查集
    for i in range(1,n+1):
        for j in range(1,n+1):
            if matrix[i-1][j-1]!=0:
                uf.join(i,j)
    
    #计算每个相似类的相似度之和
    for i in range(1,n+1):
        for j in range(1,n+1):
            if matrix[i-1][j-1]!=0 and uf.isSame(i,j):
                ans[uf.find(i)]+=matrix[i-1][j-1]#将相似度累加到根节点的相似度和中
                matrix[i-1][j-1]=0#为防止重复计算，将相似度置为0
                matrix[j-1][i-1]=0#对称位置也置为0

    
    #输出相似度之和，先排序
    sorted_ans=sorted(ans[1:], reverse=True)#排序并去掉第0个元素
    for score in sorted_ans:
        if score<=0:#只输出正值
            break
        print(score,end=' ')#打印相似度和

main()
