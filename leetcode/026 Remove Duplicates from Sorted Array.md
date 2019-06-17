---
tags: [Leetcode/Easy]
title: 26 Remove Duplicates from Sorted Array
created: '2019-03-22T01:37:30.038Z'
modified: '2019-03-22T01:38:23.629Z'
---

## 解决

使用两个指针, 一个指向数组中不同的元素, 另一个用来跳过重复的元素.

```java
public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
```

另外两种只使用一个指针的方法.

```java
public int removeDuplicates(int[] nums) {
    int i = nums.length > 0 ? 1 : 0;
    for (int n : nums)
        if (n > nums[i-1])
            nums[i++] = n;
    return i;
}
```

```java
public int removeDuplicates(int[] nums) {
    int i = 0;
    for (int n : nums)
        if (i == 0 || n > nums[i-1])
            nums[i++] = n;
    return i;
}
```



## 拓展

Java中数组, Array类的常用操作
