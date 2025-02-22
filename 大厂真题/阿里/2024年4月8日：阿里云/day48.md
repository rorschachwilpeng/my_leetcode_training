# 代码随想录
## 真题
### [阿里云真题](https://notes.kamacoder.com/questions/502144)
#### 任务要求
#### 2024年4月8日：阿里云 - 第1题：塔子哥的平方数

https://codefun2000.com/p/P1807

##### 重要知识点
- 解题思路
- 埃氏筛选
- 怎么判断完全平方数
- 怎么判断质数
- 怎么找到最小素因子
- 30mins写的代码
- 正确代码





**解题思路**

几乎可以说是一道模拟题


**埃氏筛选**

1. 概述
	- 定义：一种用于高效筛选所有小于等于正整数 nn 的质数的经典算法。
	- 提出者：古希腊数学家埃拉托斯特尼（Eratosthenes）。
	- 核心思想：通过标记合数的倍数，逐步筛选出质数。
	- 时间复杂度：O(n*log⁡*log⁡n)，空间复杂度：O(n)。

2. 算法步骤
	- 初始化数组：
		- 创建长度为 n+1 的布尔数组 `is_prime`，默认所有元素为 `True`（假设所有数初始为质数）。
		- 手动标记 `is_prime[0] = is_prime[1] = False`（0和1不是质数）。
	-  筛选过程：
		- 从第一个质数 p=2 开始，遍历到 n​：
		- 若 `is_prime[p] == True`，则 p 是质数。

**怎么判断完全平方数**: 

`if sqrt(num)**2==num:`

**怎么判断质数**

代码通过预先生成的质数表（`primes`）进行判断：
- 若目标数 `val` 能被任一质数 `prime` 整除（即 `val % prime == 0`），则 `val` 不是质数。
- 若遍历完所有预存质数仍未被整除，则判定 `val` 为质数。

**怎么找到最小素因子**

代码通过遍历预存质数表 `primes`（按升序排列）：
- 从最小的质数 `prime` 开始，依次检查是否能整除目标数 `num`。
- 第一个满足 `num % prime == 0` 的质数 `prime` 即为最小素因子。

**30min写的代码**❌❌ --> 超时
```Python 
#什么是素数？-->大于1且只能被1和它本身整除的整数
#什么是素因子？-->能够整除数且是素数的数


#需要判断每次操作后是否为完全平方数

#需要判断x是否为素数


#最少操作次数-->感觉可以用动态规划来做


#感觉题目里面说得不清楚啊,每次执行“如下两次操作”是一次操作吗？还是两次操作？


#想复杂了-->这是一道模拟题

def isPrime(num):#判断是否为素数
    for i in range(1,num):
        if i>1 and num%i==0:
            return False
    return True

def minPrime(num):#返回最小素数
    for i in range(1,num):
        if isPrime(i):
            return i

def isPerfectSquare(num):#判断是否为完全平方数
    root=1
    while root**2<num:
        root+=1
        if root**2==num:
            return True
    return False

def main(num):
    result=0
    while not isPerfectSquare(num):#如果num不是完全平方数的话:
        if isPerfectSquare(num):#如果num是素数的话，num-=1
            num-=1
        else:#否则:
            num=num//minPrime(num)#除以自己最小的素因子-->怎么找到最小的素因子
        result+=1
    return result

num=int(input())
ans=main(num)
print(ans)
```

存在的问题：
1. `isPrime`判断素数的方法过于低效；
2. `minPrime`计算最小素因子过于低效；
3. `isPerfectSquare`判断完全平方数的方法不高效；


**正确的代码** ✅✅✅
```Python

from math import sqrt

N=32000
is_p=[True]*(N+1)
primes=[]


def ols(N):#埃氏筛选
    for i in range(2,N):
        if is_p[i]:
            primes.append(i)
        for prime in primes:
            if prime*i>N:#越界
                break
            is_p[prime*i]=False#筛掉非质数
            if i%prime==0:#避免重复判断同一个元素是否是质数
                break

num=int(input())
ols(N)#先找到合法区间中所有质数


def isPrime(val):#判断一个数是否为质数
    for prime in primes:
        tmp=val//prime
        if val==tmp**prime:
            return False
    return True


ans=0
while True:
    if num==sqrt(num)**2:#判断完全平方数
        break
    else:
        if isPrime(num):#如果num是素数
            num-=1
            ans+=1
        else:#num不是素数
            for prime in primes:#遍历所有质数
                if num%prime==0:#找到素因子
                    num//=prime
                    ans+=1
                    break
print(ans)
```
