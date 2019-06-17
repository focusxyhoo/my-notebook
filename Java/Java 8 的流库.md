# Java 8 的流库

## 从迭代到流

流的指导原则是“做什么而非怎么做”，因此能够以其想要的任何方式来调度循环中的操作。

## 流的创建

1. 可以用Collection接口的stream方法将任何集合转换为一个流。
2. 对于一个数组，可以使用静态的Stream.of方法。of方法具有可变长参数，因此可以构建具有任意数量引元的流。
3. Array.stream(array, from, to)可以从数组中位于from（包括）和to（不包括）的元素中创建一个流。
4. 静态的Stream.empty方法可以创建一个不包含任何元素的流。

```java
Stream<String> silence = Stream.empty();
```

5. Stream接口有两个用于创建无限流的静态方法。generate方法会接受一个不包含任何引元的函数。iterate方法可以产生无限序列，例如0 1 2 3……，它接受一个种子值，以及一个函数，并且会反复将该函数应用到之前的结果上。

```java
// 获取一个常量值的流
Stream<String> echos = Stream.generate(() -> "Echo");
// 获取一个随机数的流
Stream<Double> randoms = Stream.generate(Math::random);
// 产生一个无限序列，0 1 2 3……
Stream<BigInteger> integers = Stream.iterate(BigInteger.ZERO, n -> n.add(BigInteger.ONE));
```

**注意**：Java API中有大量方法可以产生流。

如：Pattern类中有一个splitAsStream方法，其按照某个正则表达式来分割一个CharSequence对象。静态的File.lines方法会返回一个包含了文件中所有行的Stream。

## 流的转换

留的转换会产生一个新的流，它的元素派生自另一个流中的元素。

filter转换会产生一个流，它的元素与某种条件相匹配。filter的引元是Predicate<T>，即从T到boolean的函数。

``` java
List<String> wordList = "hello, world";
Stream<String> longWords = wordList.stream().filter(w -> w.length() > 12);
```

通常，当我们想按照某种方式对流中的值全部进行转换，可以使用map方法，并传递执行该转换的函数。

```java
// 带方法引用的map方法
Stream<String> lowercaseWords = words.stream().map(String::toLowerCase);
// 也可以使用lambda表达式来代替
Stream<String> firstLetters = words.stream().map(s -> s.substring(0, 1));
```

有的时候，当我们传入map方法的函数，其返回的不是一个值，而是一个包含众多值的流，那么我们会得到一个包含留的流。为了将其摊平，可以使用flatMap方法。

```java
// 这里letters函数的返回值是一个流
Stream<String> flatResult = words.stream().flatMap(w -> letters(w))
```

## 抽取子流和连接流

调用stream.limit(n)方法会返回一个新的流，它在n个元素之后结束（如果原来的流更短，那么就会在流结束时结束）。这个方法在裁剪无限流的尺寸时会非常有用。

```java
// 产生一个包含100个随机数的流
Stream<Double> randoms = Stream.generate(Math::random).limit(100);
```

