---
title: 利用Iterator访问Collection
tags: [Java]
created: '2019-03-22T02:58:13.716Z'
modified: '2019-03-22T03:31:36.873Z'
---

# 利用Iterator访问Collection
遍历Collection中每一个元素的一个方法是employ an *iterator*。Iterator类实现了**Iterator**或**ListIterator**接口。ListIterator继承了Iterator，并额外加入了列表的双向遍历，以及对元素的修改。
## 使用Iterator
每一个Collection类都会提供`iterator()`方法，并未返回一个指向collection第一个元素的iterator。
1. 通过调用`iterator()`方法，获得iterator对象；
2. 设置一个循环，对用`hasNext()`方法使循环进行下去，直到每一个元素都遍历完（对应的反向遍历是调用`hasPrevious()`方法）；
3. 在循环内部，通过对用`next()`方法获得每个元素。

对于实现了`List`的Collection类，可以通过调用`listIterator()`方法得到iterator对象。
```java
ArrayList<String> al = new ArrayList<>();
// 假设al中已经添加了元素。
Iterator<String> itr = al.iterator();
while(itr.hasNext()) {
  String element = itr.next();
}
ListIterator<String> litr = al.listIterator();
while(litr.hasNext()) {
  String element = litr.next();
  litr.set(element + "@");
}
// 逆向遍历
// 注意在上一步的修改操作会，litr已经指向了al的最后一个元素
while(litr.hasPrevious()) {
  String element = litr.previous();
}

```
## For-Each
当不需要逆序修改或获取元素时，可以仅使用For-Each循环遍历Collection中的元素，这样比第一种方法要方便。
记住：`for`循环可以遍历任何实现了`Iterable`接口的对象集合（collections of objects）。
