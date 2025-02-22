# 代码随想录

## 大厂真题
### [阿里](https://notes.kamacoder.com/questions/502144)
#### 大厂真题
#### 2024年4月8日：阿里云 - 第2题：塔子哥跳格子

https://codefun2000.com/p/P1808

##### 重要知识点
- 解题思路
- 动规五部曲



**解题思路**

这道题考查动态规划，难点主要体现在怎么构造斐波那契数组和推导出动态规划的递推公式
1. 构造斐波那契数组；
2. 动态规划推导。



**动规五部曲**
1. dp数组下标以及含义：dp[i]-->跳到第i个格子最多可以获得多少分；
2. 递推公式：dp[i]= max(dp[i], dp[i-jump]+nums[i]) --> 对于每个i都会有两种情况，即选择当前格子/不选择当前格子
3. 初始化: dp[0]=nums[0]
4. 遍历顺序：两层for循环，外层循环遍历跳多少格子，内层循环遍历可以跳的步数（从构造的斐波那契数组中来选）




```Python
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    # 读取 n 和 nums 数组
    n = int(input_data[0])
    nums = list(map(int, input_data[1:1+n]))
    
    # 初始化 dp 数组，dp[i] 表示跳到第 i+1 个格子时的最大分数
    dp = [-10**18] * n
    dp[0] = nums[0]
    
    # 构造斐波那契数组，存储所有小于 n 的斐波那契跳跃步长
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    # 动态规划：对于每个格子 i，遍历所有合法的跳跃步长
    for i in range(1, n):
        for jump in fib:
            if i - jump >= 0:
                dp[i] = max(dp[i], dp[i - jump] + nums[i])
            else:
                break
    
    print(dp[n - 1])

if __name__ == '__main__':
    main()
```
