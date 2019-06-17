---
tags: [Leetcode/Easy]
title: 07 Reverse Integer
created: '2019-03-22T01:37:30.033Z'
modified: '2019-03-22T01:37:50.599Z'
---

## 问题

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-$2^{31}$, $2^{31}$ - 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## 解决

```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && pop > 7))
                return 0;
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && pop < -8))
                return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

重点在于需要考虑**越界**问题, 注意Java中`int`类型对应的对象是`Integer`, 其上界和下界分别储存在变量`MAX_VALUE`和`MIN_VALUE`中, 且有:

```java
System.out.println(Integer.MAX_VALUE % 10);
// 7
System.out.println(Integer.MIN_VALUE % 10);
// -8
```


