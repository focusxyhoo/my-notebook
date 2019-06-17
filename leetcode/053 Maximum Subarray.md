---
tags: [Leetcode/Easy]
title: 53 Maximum Subarray
created: '2019-03-22T01:37:30.041Z'
modified: '2019-03-22T01:38:35.206Z'
---

## 解决

暴力法

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int cur = 0;
            for (int j = i; j < nums.length; j++) {
                cur = cur + nums[j];
                if (cur >= max) {
                    max = cur;
                }
            }
        }
        return max;
    }
}
```



```java
public class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0], length = nums.length;
        for(int i = 1; i<length; i++) {
        	if(nums[i-1]>0) nums[i] = nums[i-1]+nums[i];
        	if(maxSum<nums[i]) maxSum = nums[i];
        }
        return maxSum;
    }
}
```


