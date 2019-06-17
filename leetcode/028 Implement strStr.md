---
tags: [Leetcode/Easy]
title: 28 Implement strStr
created: '2019-03-22T01:37:30.040Z'
modified: '2019-03-22T01:38:31.397Z'
---

就是字符串匹配问题

#####  暴力法

```java
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        int s = haystack.length();
        int p = needle.length();

        int i = 0;
        int j = 0;
        while (i < s && j < p) {
            // 若当前字符匹配成功, 则指针均往后移一位
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            } else {
                // 否则, 字符串指针回退, 模式串指针置0
                i = i - j + 1;
                j = 0;
            }
        }
        if ( j == p)
            return i - j;
        else 
            return -1;
    }
}
```

##### KMP算法


