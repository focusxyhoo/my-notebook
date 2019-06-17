---
tags: [Leetcode/Easy]
title: 27 Remove Element
created: '2019-03-22T01:37:30.039Z'
modified: '2019-03-22T01:38:27.257Z'
---

## 解决

缺点: 当需要remove的元素不多时, 需要进行大量不必要的赋值操作.

```java
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int n : nums) {
    if (n != val) {
    nums[i] = n;
            i++;
        }
    }
    return i;
}
```

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int n = nums.length;
        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[n - 1];
                // reduce array size by one
                n--;
            } else {
                i++;
            }
        }
        return n;
    }
}
```



## 拓展


