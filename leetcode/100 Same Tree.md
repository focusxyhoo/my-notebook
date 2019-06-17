---
title: 100 Same Tree
tags: [Leetcode/Easy]
created: '2019-03-18T07:25:10.623Z'
modified: '2019-03-22T01:40:13.091Z'
---

# 100 Same Tree
题目很简单，判断两个二叉树是否一样。当且仅当该节点的值相同、且该节点左右子树也分别对应相同时，两个二叉树一样。
## Recursion
最简单的方法就是**递归**。那么如何写递归代码呢？
我所理解的一般步骤是：
1. 首先罗列递归问题最里层的简单情况。在这道题中，二叉树叶子结点是最简单的情况。
2. 其次将当前问题表示成上一个问题即可。对于本题，判断两个二叉树是否相同即判断其对应的左子树和右子树是否相同即可。
```java
public boolean isSameTree(TreeNode p, TreeNode q) {
    // recurision method
    if (p == null && q == null) return true;
    if (p == null && q != null || p != null && q == null) return false;
    if (p.val != q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```
## Iteration
通常递归的效率不高，这时可以考虑自己写**迭代**的方法。
```java
public boolean isSameTree(TreeNode p, TreeNode q) {
    // iteration method
    if (p == null && q == null) return true;
    if (p == null && q != null || p != null && q == null) return false;
    Stack<TreeNode> stackP = new Stack<>();
    Stack<TreeNode> stackQ = new Stack<>();
    stackP.add(p);
    stackQ.add(q);
    while (!stackP.isEmpty() && !stackQ.isEmpty()) {
        TreeNode tmpP = stackP.pop();
        TreeNode tmpQ = stackQ.pop();
        if (tmpP.val != tmpQ.val) return false;
        if (tmpP.left != null && tmpQ.left != null) {
            stackP.push(tmpP.left);
            stackQ.push(tmpQ.left);
        } else if (tmpP.left == null && tmpQ.left == null) {
          //当左子树均为空时，不进行任何操作。
        } else {
            return false;
        }
        if (tmpP.right != null && tmpQ.right != null) {
            stackP.push(tmpP.right);
            stackQ.push(tmpQ.right);
        } else if (tmpP.right == null && tmpQ.right == null) {
        } else {
            return false;
        }
    }
    if (!stackP.isEmpty() || !stackQ.isEmpty()) return false;
    return true;
}
```
