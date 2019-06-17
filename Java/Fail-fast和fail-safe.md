---
title: Fail-fast和fail-safe
tags: [Java]
created: '2019-03-18T04:54:42.231Z'
modified: '2019-03-28T07:33:56.370Z'
---

# Fail-fast和fail-safe
熟悉这两个概念的含义，以及区别。
Fail-Fast，快速失败，Iterator的fail-fast属性与当前的集合共同起作用，因此它不会受到集合中任何改动的影响。Java.util包中的所有集合类都被设计为fail->fast的，而java.util.concurrent中的集合类都为fail-safe的。当检测到正在遍历的集合的结构被改变时，Fail-fast迭代器抛出ConcurrentModificationException，而fail-safe迭代器从不抛出ConcurrentModificationException。
