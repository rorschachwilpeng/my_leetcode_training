# 代码随想录
## 数组
### 《代码随想录》数组：二分查找
#### 数组：二分查找
#### 任务要求
704. 二分查找

题目建议： 大家今天能把 704.二分查找 彻底掌握就可以，至于 35.搜索插入位置 和 34. 在排序数组中查找元素的第一个和最后一个位置 ，如果有时间就去看一下，没时间可以先不看，二刷的时候在看。
先把 704写熟练，要熟悉 根据 左闭右开，左闭右闭 两种区间规则 写出来的二分法。

题目链接： https://leetcode.cn/problems/binary-search/ 

文章讲解： https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html 

视频讲解： https://www.bilibili.com/video/BV1fA4y1o715
##### 重要知识点
- 使用二分查找的前提条件&思路
- 不同边界条件下（左闭右闭/左闭右开），如何构造循环不变量？
- 中间指针(middle)实现的代码小技巧

**使用二分查找的前提条件&思路**

	1. 二分查找的使用前提是数组为 没有重复元素 的 有序数组；
	2. 二分查找的思路：构造两个指针，一个指数组最左边，另一个指数组最右边。根据两个指针可以得到一个中间指针，通过判断中间指针索引所对应元素与目标值的大小关系，我们可以不断地调整左/右指针，从而最后找到目标值。
	
**不同边界条件下（左闭右闭/左闭右开），如何构造循环不变量？**

*左闭右闭*
```Python 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1#右区间是闭区间
        while l<=r:#这里是"<="
            mid=l+(l-r)//2#防止溢出
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1#这里是“-1”
            elif nums[mid]==target:
                return mid
        return -1
```
*左闭右开*
```Python 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)#右区间是开区间
        while l<r:#这里是"<"
            mid=l+(l-r)//2#防止溢出
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid#这里不用“-1”
            elif nums[mid]==target:
                return mid
        return -1
```
**中间指针(middle)实现的代码小技巧**

在构造中间指针时，通常我会习惯将代码写成```middle=(left+right)//2```，但其实```middle = left + (right - left) // 2```这种写法可以避免内存溢出。


### 《代码随想录》数组：移除元素
#### 任务要求
27. 移除元素

题目建议：
暴力的解法，可以锻炼一下我们的代码实现能力，建议先把暴力写法写一遍。 双指针法 是本题的精髓，今日需要掌握，至于拓展题目可以先不看。

题目链接： https://leetcode.cn/problems/remove-element/  

文章讲解： https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html 

视频讲解： https://www.bilibili.com/video/BV12A4y1Z7LP
##### 重要知识点
- 双指针 --> 快慢指针

**双指针 --> 快慢指针**
构造快慢指针，两个指针值都代表索引，快指针比慢指针走得快（废话），快指针在前面读，读到目标值就跳过（依题意），否则加入到数组中。加入时的索引即快指针的值。

```Python 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #构造快慢指针
        #快指针 --> read操作
        #慢指针 --> write操作
        slow=0
        fast=0

        while fast<len(nums):#左闭右开
            if nums[fast]!=val:#如果读到的数据不是目标值
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            else:#如果读到的数据是目标值
                fast+=1
                continue
            
        return slow
```

### 《代码随想录》数组：有序数组的平方
#### 任务要求
##### 977.有序数组的平方


题目建议： 本题关键在于理解双指针思想 

题目链接：https://leetcode.cn/problems/squares-of-a-sorted-array/ 

文章讲解：https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html 

视频讲解： https://www.bilibili.com/video/BV1QB4y1D7ep
##### 重要知识点
- 双指针 --> 对向双指针

**双指针 --> 对向双指针**

由于数组元素是非递减顺序，可能包含负数，平方后顺序会改变。通过对向双指针，左指针从数组起点，右指针从终点开始，比较两端平方值，将较大的值按逆序放入结果数组，然后移动对应指针，最终得到按非递减顺序排列的平方值数组。

```Python 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #双指针 --> 对向双指针
        l=0#左指针
        r=len(nums)-1#右指针
        idx=len(nums)-1#新数值中索引
        res=nums.copy()#新数组

        while l<=r:
            lv=nums[l]**2
            rv=nums[r]**2
            if lv<=rv:#右指针的元素绝对值更大，新元素为右指针对应元素
                res[idx]=rv
                r-=1#更新右指针索引位置
            else:#左指针的绝对值更大，新元素为左指针对应元素
                res[idx]=lv
                l+=1#更新左指针索引位置
            idx-=1

        return res
```

