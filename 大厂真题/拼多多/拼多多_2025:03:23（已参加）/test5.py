import bisect
#1.构建两位数的非幸运数组
valid=[]
for i in (1,2,4,5,7,8):
    for j in (1,2,4,5,7,8):
        if i%3==j%3:
            valid.append(i*10+j)
valid.sort()

#2.前提：根据鸽巢原理可推，三位数及以上的连续子串一定包含3的倍数
T=int(input())
for _ in range(T):
    #3.计算一位数中的非幸运数字
    L,R=map(int,input().strip().split())
    total=R-L+1
    start1=max(L,1)
    end1=min(R,9)
    if start1<=end1:#保证在一位数的范围内
        count1=0
        total1=end1-start1+1
        unlucky_cnt=(end1//3)-((start1-1)//3)
        count1=total1-unlucky_cnt#计算一位数范围中的非幸运数字
    
    #4.计算两位数中的非幸运数字
    start2=max(L,10)
    end2=min(R,99)
    if start2<=end2:#保证在二位数的范围内
        count2=0
        l=bisect.bisect_left(valid,start2)
        r=bisect.bisect_right(valid,end2)
        count2=r-l
    #幸运数字数量 = 总数量 - 非幸运数量（一位数非幸运数量 + 两位数幸运数量）
    lucky=total-(count1+count2)
    print(lucky)
