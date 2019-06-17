---
tags: [Leetcode/Easy]
title: 13 Roman to Integer
created: '2019-03-22T01:37:30.035Z'
modified: '2019-03-22T01:42:33.293Z'
---

## 解决

```java
class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('M', 1000);
        map.put('D', 500);
        map.put('C', 100);
        map.put('L', 50);
        map.put('X', 10);
        map.put('V', 5);
        map.put('I', 1);
        int result = 0, max = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int curr = map.get(s.charAt(i));
            if (curr >= max) {
                max = curr;
                result += curr;
            } else {
                result -= curr;
            }
        }
        return result;
    }
}
```
注意`HashMap`的用法就可以了。


