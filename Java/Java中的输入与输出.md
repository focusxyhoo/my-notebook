# Java中的输入与输出

## 输入/输出流

注意，读入一个字节序列的对象称为**输入流**，写入一个字节序列的对象称做**输出流**。这两个概念不要混淆了，是相对Java而言的。抽象类InputStream和OutputStream构成了输入/输出类层次结构的基础。

但是，面向字节的流不便于处理以Unicode形式存储的信息（因为Unicode中每个字符都使用了多个字节来表示），因此从抽象类Reader和Writer中继承出来了一个专门用于处理Unicode字符的单独的类层次结构。这些类拥有的读入和写出操作都是基于两字节的Char值的（即Unicode码元），而不是基于byte值的。

### 读写字节

InputStream类有一个抽象方法，该方法读入一个字节，并返回读入的字节，或者在遇到输入源结尾时返回-1。

```java
abstract int reaad()
```

在设计具体输入流类时（即继承InputStream类），必须覆盖这个方法以提供适用的功能。同时，InputStream类中还有其他非抽象方法，且这些方法都是调用抽象的read方法来实现不同的功能的。因此，子类必须且只需覆盖着一个方法。

同样的，OutputStream类也定义了一个抽象方法，它可以向某个输出位置写出一个字节。

```java
abstract void write(int b)
```

**注意**：read和write方法在执行时都将**阻塞**，直至字节确实被读入或者写出。这意味着如果流不能立即被访问，那么当前线程会被阻塞，在等待可用的这段时间里其他线程就有机会被执行。

### 层次结构

InputStream和OutputStream类可以读写单个字节或者字节数组，其构成了下图所示层次结构的基础。如果想要读写字符串和数字，就需要使用功能更强大的子类了。

![Java输入输出流层次结构](/Users/huxiaoyang/Pictures/知识类/Java输入输出流层次结构.png)

对于Unicode文本，可以使用抽象类Reader和Writer的子类。Reader和Writer类的基本方法与InputStream和OutputStream类中的方法类似。其中，read方法返回一个Unicode码元（0到65535之间的一个整数），或者在碰到文件结尾时返回-1，write方法在被调用时，需要传递一个Unicode码元。Reader和Writer抽象类的层次结构如下图。

![Reader和Writer层次结构](/Users/huxiaoyang/Pictures/知识类/Reader和Writer层次结构.png)

**注意**：所有在java.io中的类都将相对路径名解释为以用户工作目录开始。通过调用`System.getProperty("user.dir")`来获得这个信息。

**举例说明**：FileInputStream可以通过提供的文件名或者文件完整路径名来进行字节级别的读入，但是其无法读入数值类型。其子类DataInputStream只能读入数值类型，且没有任何从文件中获取数据的方法。那么如何从文件中读取数值类型呢？

Java提供了一个机制：某些输入流可以从文件或其他更外部的位置获取字节，而其他的输入流可以将字节组装到更有用的数据类型中。在上面这个例子中，为了从文件中读入数字，需要先创建一个FileInputStream，然后将其传递给DataInputStream的构造器。

```java
FileInputStream fin = new FileInputStream("hello.txt");
DataInputStream din = new DataInputStream(fin);
double x = din.readDouble();
```

由此，**可以通过嵌套过滤器来添加多重功能**。

比如，输入流默认下是不会被缓冲区缓存的，这就说明每个对read的调用都会请求操作系统在分发一个字节。相比之下，请求一个数据块并将其置于缓冲区会更加高效。如果我们想要使用这种缓冲机制，那么需要使用下面的构造器序列：

```java
DataInputStream din = new DataInputStream(
	new BufferedInputStream(
   	new FileInputStream("hello.txt")));
```

我们将DataInputStream置于构造器链的最后，这是因为我们希望使用DataInputStream的方法，并且希望他们能使用带缓冲机制的read方法。

通过上面的分析，可以发现Java为了实现真正有用的输入/输出流序列，需要将多个流过滤器组合起来，相比其他语言来说，比较麻烦，但是可以带来极大的灵活性。

## 文本输入与输出

在保存数据时，可以选择二进制格式或者文本格式。二进制格式的I/O高速且高效，但是不宜人来阅读。而在存储文本字符串时，需要考虑**字符编码**方式。Java内部使用的是UTF-16编码方式。

OutputStreamWriter类将使用选定的字符编码方式，把Unicode码元的输出流转换为字节流。而InputStreamReader类将包含字节（用某种字符编码方式表示的字符）的输入流转换为可以产生Unicode码元的读入器。

**注意**：`System.in`是InputStream的一个子类的预定义对象，是从"标准输入"中读入信息，即控制台或者重定向的文件。

```java
// 从控制台读入键盘敲击信息，并将其转为Unicode。使用主机系统使用的默认字符编码方式
Reader in = new InputStreamReader(System.in);
// 选择一种具体的编码方式
Reader in2 = new InputStreamReader(new FileInputStream("hello.txt"),StandardCharsets.UTF_8);
```

### 如何写出文本输出

对于文本输出，可以使用PrintWriter类。这个类拥有以文本格式打印字符串和数字的方法，

### 如何读入文本输入

