---
tags: [Leetcode/Easy]
title: 09 Palindrome Number
created: '2019-03-22T01:37:30.034Z'
modified: '2019-03-22T01:37:56.110Z'
---

## 解决

第一种思路是, 将`int`类型的变量转化为`String`, 直接套用判断字符串是否是回文的方法来解决;

第二种想法是, 直接将数字倒转过来, 但是会出现越界的情况; 

第三种情况是, 只倒转一半的数字, 但难点在于, 如何判断我们转换了后半部分数字?

```java
class Solution {
    public boolean isPalindrome(int x) {
        // 负数和以0结尾的(0除外)都直接判断不是回文
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int revert = 0;
        // 判断条件是x > revert
        while (x > revert) {
            revert = revert * 10 + x % 10;
            x /= 10;
        }
        return x == revert || x == revert / 10;
    }
}
```

### 判断回文

对于字符类

对于数字, 倒转过来之后容易出现越界问题, 因此需要特别注意.

### Java中的==和equals


