---
title: Collection和Arrays
tags: [Java]
created: '2019-03-18T02:57:50.349Z'
modified: '2019-04-02T07:04:08.222Z'
---

# Collection和Arrays

Java中的集合概念是什么？
分为几类？各自有什么？特点是？

## ArrayList和LinkedList的异同

从以下这几个方面去理解：

### 是否保证线程安全

ArrayList和LinkedList都是不同步的，因此都不能保证线程安全。

### 底层数据结构

ArrayList 底层使用的是Object数组；LinkedList 底层使用的是双向链表数据结构（JDK1.6之前为循环链表，JDK1.7取消了循环。注意双向链表和双向循环链表的区别）。

### 插入和删除是否受元素位置的影响

ArrayList 采用数组存储，所以插入和删除元素的时间复杂度受元素位置的影响。LinkedList 采用链表存储，所以插入、删除元素时间复杂度不受元素位置的影响，都是近似 O（1）而数组为近似 O（n）。

### 是否支持快速随机访问

LinkedList 不支持高效的随机元素访问，而 ArrayList 支持。快速随机访问就是通过元素的序号快速获取元素对象(对应于get(int index) 方法)。

### 内存空间占用

ArrayList的空间浪费主要体现在在list列表的结尾会预留一定的容量空间，而LinkedList的空间花费则体现在它的每一个元素都需要消耗比ArrayList更多的空间（因为要存放直接后继和直接前驱以及数据）。

### 补充：`RandomAccess`接口

源码中表明，RandomAccess接口没有定义任何内容，因此，其只起着一个标识的作用：实现这个接口的类具有随机访问的功能。ArrayList 实现了 RandomAccess 接口，而 LinkedList 没有实现。这是因为，ArrayList 底层是数组，而 LinkedList 底层是链表。数组天然支持随机访问，时间复杂度为 O（1），所以称为快速随机访问。链表需要遍历到特定位置才能访问特定位置的元素，时间复杂度为 O（n），所以不支持快速随机访问。ArrayList 实现了 RandomAccess 接口，就就向外表明它具有快速随机访问功能。但是要注意，RandomAccess 接口只是标识，并不是说 ArrayList 实现 RandomAccess 接口才具有快速随机访问功能的。

### 补充：list 的遍历方式选择

+ 实现了RandomAccess接口的list，优先选择普通for循环 ，其次foreach；
+ 未实现RandomAccess接口的list， 优先选择iterator遍历（foreach遍历底层也是通过iterator实现的）。大size的数据，千万不要使用普通for循环。

## ArrayList和Vector的区别

Vector类的所有方法都是同步的。可以由两个线程安全地访问一个Vector对象，但是一个线程访问Vector的话代码要在同步操作上耗费大量的时间。ArrayList不是同步的，所以在不需要保证线程安全时时建议使用ArrayList。





## ArrayList和Array的区别
1. Array可以容纳基本类型和对象，而ArrayList只能容纳对象。
2. Array是指定大小的，而ArrayList大小是固定的。

## ArrayList和HashMap的默认大小？
在Java1.7中，
1. ArrayList的默认大小是10个元素；
2. HashMap的默认大小是16个（必须是2的幂）元素。

## LinkedHashMap和PriorityQueue的区别
PriorityQueue 是一个优先级队列,保证最高或者最低优先级的的元素总是在队列头部，但是 LinkedHashMap 维持的顺序是元素插入的顺序。当遍历一个 PriorityQueue 时，没有任何顺序保证，但是 LinkedHashMap 课保证遍历顺序是元素插入的顺序。


