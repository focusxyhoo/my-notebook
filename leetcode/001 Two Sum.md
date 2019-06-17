---
tags: [Leetcode/Easy]
title: 001 Two Sum
created: '2019-03-22T01:35:37.224Z'
modified: '2019-03-22T01:36:47.357Z'
---

# 001 Two Sum
## 问题

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9, 

Because nums[0] + nums[1] = 2 + 7 = 9,

 return [0, 1].

## 解决

### 暴力法

直接通过两个for循环遍历所有组合, 得到结果. 注意如果没有符合题意的结果, 则给出错误信息.

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
```

### 两遍哈希表

使用Java中的HashMap. 第一遍循环将数组`nums`中的元素和其序号一同加入HashMap, 第二遍循环遍历数组`nums`, 在HashMap中查找是否存在符合条件的`left`. 注意`if`中的条件.

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int left = target - nums[i];
            if (map.containsKey(left) && (map.get(left) != i)) {
                return new int[] { i, map.get(left) };
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
```



### 一遍哈希表

在将数组`nums`中的元素添加到HashMap时就开始查找符合条件的`left`. 即使刚开始加入HashMap中的元素没有与之对应的`left`, 但是只要存在, 后面也会被添加到HashMap中并检索出来. 这样只需要一遍哈希表就可以完成检索.

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int left = target - nums[i];
            if (map.containsKey(left)) {
                return new int[] {i, map.get(left)};
            }
            map.put(nums[i], i)
        }
        throw new IllegalArgumentException("No Answer!");
    }
}
```

## 总结

### 关于Java中的HashMap

类似于数组`Array`, 利用`int`类型的index来索引其元素, HashMap则相对灵活得多, 其利用键值对来储存元素, 且其类型搭配可以多种多样. **注意**: 在指定类型时, 一定要使用primitive type对应的wrapper class, 而Java中的String是对象.

```java
import java.util.HashMap;

HashMap<String, String> captitalCities = new HashMap<String, String>();
```

操作: 增`put()`、删一项元素`remove()`、删整个哈希表`clear()`、查`get()`、大小`size()`.

遍历

```java
// Print keys
for (String i : capitalCities.keySet()) {
// Print value use capitalCities.values()
  System.out.println(i);
}
```






