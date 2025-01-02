# 代码随想录
## 字符串
### 《代码随想录》字符串：翻转字符串里的单词
#### 任务要求
#### 151.翻转字符串里的单词

建议：这道题目基本把 刚刚做过的字符串操作 都覆盖了，不过就算知道解题思路，本题代码并不容易写，要多练一练。 

题目链接/文章讲解/视频讲解：https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html

##### 重要知识点
- 一行流
- 另一种思路
- 双指针思路

**一行流**
1. 去掉无效的空格
2. 拆分单词， 并保存到一个新列表中
3. 将新列表中的单词倒序输出出来

我也能写出装逼的一行流了！

```Python 
class Solution:
    def reverseWords(self, s: str) -> str:
       return " ".join(list(s.strip().split())[::-1])
```

**另一种思路**

先删除空白，然后整个反转，最后单词反转。 **因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，然后通过join函数再将其转换成列表，所以空间复杂度不是O(1)**
```Python 
class Solution:
    def reverseWords(self, s: str) -> str:
        #去掉无效空格
        s=s.strip()
        #反转整个字符串
        s=s[::-1]
        #再反转每个单词
        s=" ".join(word[::-1] for word in s.split())
        return s
```

**双指针思路**
```
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()

        left,right=0,len(words)-1

        while left<right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        return " ".join(words)
```

### 《代码随想录》字符串：右旋字符串
#### 任务要求
### 卡码网：55.右旋转字符串

建议：题解中的解法如果没接触过的话，应该会想不到

题目链接/文章讲解：
https://docs.qq.com/scenario/link.html?url=https%3A%2F%2Fprogrammercarl.com%2Fkamacoder%2F0055.%25E5%258F%25B3%25E6%2597%258B%25E5%25AD%2597%25E7%25AC%25A6%25E4%25B8%25B2.html&pid=300000000$PuWJvMizUPsx&cid=144115351357282927&nlc=1

##### 重要知识点
- 思路
- 为什么无法实现 O(1) 空间复杂度？

**思路**
1. 先翻转整个字符串
2. 再独立翻转前“位数”个字符串，和“位数”个数后的字符串

**为什么无法实现 O(1) 空间复杂度？**
- **字符串的不可变性**：
	- Python 中的字符串一旦创建，就无法修改。任何对字符串的操作都会生成一个新的字符串，而不是在原地修改。
	- 例如，`s[::-1]` 会创建一个新的字符串副本，而不是直接对原字符串进行反转。
- **中间结果的开销**：
	- 每次切片（如 `s[:rotNum]` 或 `s[rotNum:]`）和拼接（如 `+` 操作）都会分配新的内存来存储中间结果。
	- 即使逻辑上看似原地操作，实际上会创建多个字符串副本，占用额外空间。

**代码**
```Python 
	def main():
		rotNum=int(input())
		s=str(input())
		s=s[::-1]
		s=s[:rotNum][::-1]+s[rotNum:][::-1]
		print(s)
	main()
```
