# 代码随想录
## 哈希表
### 《代码随想录》哈希表：四数相加II
#### 任务要求
#### 454.四数相加II

建议：本题是 使用map 巧妙解决的问题，好好体会一下 哈希法 如何提高程序执行效率，降低时间复杂度，当然使用哈希法 会提高空间复杂度，但一般来说我们都是舍空间 换时间， 工业开发也是这样。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html

##### 重要知识点
- 哈希法思路
- 哈希表实现

**哈希表思路**
- 将前两个数组的所有和存储在哈希表中，哈希表的键是数组之和，值是该和出现的次数。
- 遍历后两个数组，计算它们的和的相反数，检查该值是否存在于哈希表中。如果存在，说明找到了满足条件的四元组。
- 构造哈希表的复杂度为 O(n^2)，遍历后两个数组的复杂度也是 O(n^2)，总复杂度为 O(n^2)。

**哈希表实现**
- 哈希表用于快速查找前两个数组之和是否存在，避免重复计算，提升效率。
- 本题的哈希表实现我选择了`collections.defaultdict` 来创建一个带有默认值的字典，可以优化代码。

**代码**
```Python 
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #这个值是否出现过 --> 哈希表
        target=defaultdict(int)
        result=0
        for item1 in nums1:
            for item2 in nums2:
                target[item1+item2]+=1

        for item3 in nums3:
            for item4 in nums4:
                complement=-(item3+item4)
                if complement in target:
                    result+=target[complement]
        return result
```

### 《代码随想录》哈希表：赎金信
#### 任务要求
####  383. 赎金信

建议：本题 和 242.有效的字母异位词 是一个思路 ，算是拓展题 

题目链接/文章讲解：https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html

##### 重要知识点
- 哈希法思路

**哈希法思路**

因为题目只有小写字母，那可以利用空间换时间的哈希思路。用一个长度为26的数组来记录`ransomNote`所需要的各个字符数量。然后再检验`magazine`能否提供数组中所需要的字符和数量。


```Python 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap=[0]*26
        
        for word in ransomNote:
            idx=ord(word)-ord('a')
            hashMap[idx]+=1
        
        for word in magazine:
            idx=ord(word)-ord('a')
            hashMap[idx]-=1
            
        ENOUGH_WORDS=all(val<=0 for val in hashMap) 
        return True if ENOUGH_WORDS else False
```

### 《代码随想录》哈希表：三数之和
#### 任务要求
#### 15. 三数之和

建议：本题虽然和 两数之和 很像，也能用哈希法，但用哈希法会很麻烦，双指针法才是正解，可以先看视频理解一下 双指针法的思路，文章中讲解的，没问题 哈希法很麻烦。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html

##### 重要知识点
- 为什么不用哈希法
- 双指针立大功
- 难搞的去重逻辑

**为什么不用哈希法**

利用哈希法实现去重逻辑非常复杂，得不偿失。

**双指针立大功**

- 这道题的核心在于将问题简化为有序数组上的双指针问题（和`二分查找`有相似之处）。通过对数组进行升序排序，我们可以利用排序的性质快速定位可能满足条件的三元组。以每个数字作为三元组的第一个数，通过双指针分别从当前数字之后的位置向中间收缩，动态计算当前三数之和。当和大于目标值 0 时，右指针左移以减小和；当和小于目标值 0 时，左指针右移以增大和；如果和等于 0，则记录当前三元组并跳过重复值以避免结果重复。
- 为了避免冗余计算，基准指针在遍历过程中会跳过相邻重复的值，同时在双指针移动时也会跳过重复元素。特殊情况下，如果当前基准指针指向的数已经大于 0，则可以直接终止，因为后续的三数之和必然大于 0。
- 该方法通过排序和双指针有效地降低了时间复杂度，排序操作为 O(nlog⁡n)，双指针遍历为 O(n^2)。

**难搞的去重逻辑**

本题中有两个去重逻辑点需要注意
1. 基准指针去重
	- 在构造左右指针之前，先对基准指针所指元素进行判断。如果值与上一个元素相同，那跳过本次循环。
	- 判断条件只能是与“上一个元素”比较，而不能和“下一个元素”。举个例子，当前的数组元素为{-1,-1,0}且基准指针指向第一个"-1"，如果是与“下一个元素”比较那么我们会错过三元组[-1,-1,0]。
2. 左右指针去重
	- 错误的去重逻辑
		- 提前去重，`while right > left` 和 `if nums[i] + nums[left] + nums[right] == 0` 的条件本身也会自动避免重复计算。
		- 这种提前去重逻辑只是将原来的重复判断提前了，但并没有减少程序的复杂度。
			```
			while (right > left) {
				if (nums[i] + nums[left] + nums[right] > 0) {
					right--;
					// 去重 right
					while (left < right && nums[right] == nums[right + 1]) right--;
				} else if (nums[i] + nums[left] + nums[right] < 0) {
					left++;
					// 去重 left
					while (left < right && nums[left] == nums[left - 1]) left++;
				} else {
				}
			}
			```
	- 正确的去重逻辑
		- *去重的目的*：
			- 在找到三元组后进行去重，是为了跳过与当前三元组完全相同的其他组合。
			- 这在逻辑上直接作用于结果的正确性和完整性。
		- *去重的位置*：
			- 在找到三元组后再去重，只对需要避免重复的部分进行优化，而不会对原有逻辑造成多余的干扰。
			```
			if nums[i] + nums[left] + nums[right] == 0:
				result.append([nums[i], nums[left], nums[right]])

				# 找到三元组后，跳过重复元素
				while left < right and nums[left] == nums[left + 1]:
					left += 1
				while left < right and nums[right] == nums[right - 1]:
					right -= 1

				# 移动指针
				left += 1
				right -= 1
			```



**代码**
```Python 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        size=len(nums)
        result=[]
        TARGET=0

        def CurIsDuplicated(arr,idx):
            return True if idx>0 and arr[idx-1]==arr[idx] else False

        for cur in range(size):
            #特殊情况判断
            if nums[cur]>TARGET:return result#第一个元素都比0大，指定无法构成三元组
            if CurIsDuplicated(nums,cur):continue#去重判断
            
            #构造指针
            left=cur+1
            right=size-1
            while left<right:
                sumVal=nums[cur]+nums[left]+nums[right]
                if sumVal>TARGET:
                    right-=1
                elif sumVal<TARGET:
                    left+=1
                else:
                    result.append([nums[cur],nums[left],nums[right]])
                    while left<right and nums[left+1]==nums[left]:left+=1
                    while left<right and nums[right-1]==nums[right]:right-=1

                    left+=1
                    right-=1
        return result
```

### 《代码随想录》哈希表：四数之和
#### 任务要求
#### 18. 四数之和

建议： 要比较一下，本题和 454.四数相加II 的区别，为什么 454.四数相加II 会简单很多，这个想明白了，对本题理解就深刻了。 本题 思路整体和 三数之和一样的，都是双指针，但写的时候 有很多小细节，需要注意，建议先看视频。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html

##### 重要知识点
-  思路
- 去重逻辑依然难搞

**思路**

本题和"ThreeSum"的思路一样，只是多了一个基准指针。

**去重逻辑依然难搞**

这道题仍然很难。对我而言，难点主要在两个基准指针的去重判断上。具体可见**代码实现**中的四个子函数。

```Python 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        size=len(nums)

        def PrevValueInvalid(arr,idx):
            return True if arr[idx]>target and target>0 else False

        def PrevValueIsDuplicated(arr,idx):
            return True if idx>0 and arr[idx-1]==arr[idx]else False
        
        def CurValueInvalid(arr,idx,prev):
            return True if arr[idx]+arr[prev]>target and target>0 else False

        def CurValueIsDuplicated(arr,idx,prev):
            return True if idx>prev+1 and arr[idx-1]==nums[idx] else False
        

        for prev in range(size):
            if PrevValueInvalid(nums,prev): break
            if PrevValueIsDuplicated(nums,prev):continue

            for cur in range(prev+1,size):
                #特殊情况处理
                if CurValueInvalid(nums,cur,prev):break
                if CurValueIsDuplicated(nums,cur,prev):continue
                left=cur+1
                right=size-1

                while left<right:
                    sumVal=nums[prev]+nums[cur]+nums[left]+nums[right]
                    if sumVal>target:#大了，右指针左移
                        right-=1
                    elif sumVal<target:#小了,左指针右移
                        left+=1
                    else:
                        result.append([nums[prev],nums[cur],nums[left],nums[right]])
                        
                        while left<right and nums[right-1]==nums[right]:right-=1
                        while left<right and nums[left+1]==nums[left]:left+=1
                        left+=1
                        right-=1

        return result
```
