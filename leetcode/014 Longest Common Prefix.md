---
tags: [Leetcode/Easy]
title: 14 Longest Common Prefix
created: '2019-03-22T01:37:30.036Z'
modified: '2019-03-22T01:38:07.024Z'
---

## 解决

横向扫描. 

默认数组第一个元素为prefix, 依次和其他元素进行比较, 每次比较后立即修改得到当前的prefix. 直到比较完后得到最终的prefix.

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1 ; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }
}
```

纵向扫描.

以数组中第一个元素中的字符为标准, 从前往后一个一个字符与其他数组元素进行比较,    当遇到字符不一样或有元素到达字符串尾, 即停止扫描.

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i == strs[j].length() || strs[j].charAt(i) != c)
                    return strs[0].substring(0, i);
            }
        }
        return strs[0];
    }
}
```

分而治之.

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        return divide(strs, 0, strs.length - 1);
    }   
    String divide(String[] strs, int left, int right) {
        if (left == right) return strs[left];
        else {
            int mid = (left + right) / 2;
            String leftStr = divide(strs, left, mid);
            String rightStr = divide(strs, mid + 1, right);
            return getPrefix(leftStr, rightStr);
        }
    }
    String getPrefix(String right, String left) {
        int min = Math.min(right.length(), left.length());
        for (int i = 0; i < min; i++) {
            if (left.charAt(i) != right.charAt(i))
                return left.substring(0, i);
        }
        return left.substring(0, min);
    }
}
```

Binary search

先找出数组中元素的最小长度`minLen`, the longest common prefix一定不大于该值. 以数组第一个元素为基准, 判断其前$\frac{1+minLen}{2}$项是否是common prefix, 若是, 往后对半加, 若不是, 往前对半缩.

```java
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0)
        return "";
    int minLen = Integer.MAX_VALUE;
    for (String str : strs)
        minLen = Math.min(minLen, str.length());
    int low = 1;
    int high = minLen;
    while (low <= high) {
        int middle = (low + high) / 2;
        if (isCommonPrefix(strs, middle))
            low = middle + 1;
        else
            high = middle - 1;
    }
    return strs[0].substring(0, (low + high) / 2);
}

private boolean isCommonPrefix(String[] strs, int len){
    String str1 = strs[0].substring(0,len);
    for (int i = 1; i < strs.length; i++)
        if (!strs[i].startsWith(str1))
            return false;
    return true;
}
```

构建前缀树.

```java
public String longestCommonPrefix(String q, String[] strs) {
    if (strs == null || strs.length == 0)
         return "";  
    if (strs.length == 1)
         return strs[0];
    Trie trie = new Trie();      
    for (int i = 1; i < strs.length ; i++) {
        trie.insert(strs[i]);
    }
    return trie.searchLongestPrefix(q);
}

class TrieNode {

    // R links to node children
    private TrieNode[] links;
	// 每个节点都最多有26个子节点
    private final int R = 26;
	// 标记该节点是否是一个终止节点
    private boolean isEnd;

    // number of children non null links
    private int size;    
    public void put(char ch, TrieNode node) {
        links[ch -'a'] = node;
        size++;
    }

    public int getLinks() {
        return size;
    }
    //assume methods containsKey, isEnd, get, put are implemented as it is described
   //in  https://leetcode.com/articles/implement-trie-prefix-tree/)
}

public class Trie {

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

//assume methods insert, search, searchPrefix are implemented as it is described
//in  https://leetcode.com/articles/implement-trie-prefix-tree/)
    private String searchLongestPrefix(String word) {
        TrieNode node = root;
        StringBuilder prefix = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            char curLetter = word.charAt(i);
            if (node.containsKey(curLetter) && (node.getLinks() == 1) && (!node.isEnd())) {
                prefix.append(curLetter);
                node = node.get(curLetter);
            }
            else
                return prefix.toString();

         }
         return prefix.toString();
    }
}
```

方法还有很多: 

以数组第一个元素的前几项作为prefix, 遍历其他数组元素, 若出现不匹配即可中止扫描, 返回真正的prefix.

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";
        if (strs.length == 1)
            return strs[0];
        String commonPrefix = "";
        for (int i = 0; i < strs[0].length(); i++) {
            String pre = strs[0].substring(0, i+1);
            for (int j = 1; j < strs.length; j++) {
                if (!strs[j].startsWith(pre)) {
                    return commonPrefix;
                }
            }
            commonPrefix = pre;
        }
        return commonPrefix;
    }
}
```





## 拓展

Java中关于数组为`null`和数组长度为0的区别

Java中关于`length`属性、`length()`方法以及`size()`方法的使用

Java中字符串的常用操作

Java/Python中的自定义对象如何构建、操作
