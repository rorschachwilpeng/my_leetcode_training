N=int(input())
a=list(map(int,input().strip().split()))

#字典用于记录”元素被遍历次数“
cnt={x: 0 for x in range(1,N+1)}

#双指针
slow,fast=0,1

while fast<=N-1:
    while a[fast]>a[slow] and cnt[a[fast]]<2 and cnt[a[slow]]<2:
        #持续交换元素，直到条件不符合
        tmp=a[fast]
        a[fast]=a[slow]
        a[slow]=tmp

        #更新元素被遍历次数
        cnt[a[slow]]+=1
        cnt[a[fast]]+=1


        if slow<1:
            break
        slow-=1
        fast-=1
    slow+=1
    fast+=1
print(a)


