#读取测试数据
T=int(input())

#处理每组测试数据
for _ in range(T):
    n,m=map(int,input().strip().split())
    A=str(input())
    B=str(input())
    X=list(map(int,input().strip().split()))

    #统计X中的元素值-->需要知道A中每个元素被替换的次数
    cnt=[0]*(n+1)
    for i in X:
        cnt[i]+=1
    
    #收集被A中替换的位置，这代表着这些位置的元素需要被替换
    positions=[]
    for j in range(1,n+1):
        if cnt[j]>0:
            positions.append(j)#这里错了❌

    
    positions.sort()#将升序排列被替换的位置
    sorted_B=sorted(B)#对字符串B进行排序

    #初始化结果为字符串A的列表
    k=len(positions)
    res=list(A)

    #遍历position和sorted_B
    for i in range(k):
        pos=positions[i]#获取需要被替换的位置
        res[pos-1]=sorted_B[i]
    #将sorted_B的字符按序分配给对应位置
    #生成最终字符&输出
    print("".join(res))





