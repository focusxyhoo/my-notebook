# transient 关键字

## 什么是序列化

>序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换成可取用格式（例如存成文件，存于缓冲，或经由网络中发送），以留待后续在相同或另一台计算机环境中，能恢复原先状态的过程。依照序列化格式重新获取字节的结果时，可以利用它来产生与原始对象相同语义的副本。从一系列字节提取数据结构的反向操作，是反序列化（也称为解编组、deserialization、unmarshalling）。

以上来自于维基百科对序列化的定义。我们可以将序列化于反序列化这两个概念简单做以下理解：
**把对象转换为字节序列的过程称为对象的序列化。**
**把字节序列恢复为对象的过程称为对象的反序列化。**

对象序列化的主要用途有两种：
1. 把对象的字节序列永久地保存到硬盘上，通常是存放在一个文件中；
2. 在网络上传送对象的字节序列。

## Java 中的序列化

在 Java 中，只有实现了`Serializable`和`Externalizable`接口的类的对象才能被序列化。Externalizable 接口继承自 Serializable 接口，实现 Externalizable 接口的类完全由自身来控制序列化的行为。而实现 Serializable 接口的类，其所有属性和方法都会自动实现序列化。

对象序列化过程：
1. 创建一个对象输出流，它可以包装一个其他类型的目标输出流，如文件输出流；
2. 通过对象输出流的`writeObject()`方法写对象。

对象反序列化过程：
1. 创建一个对象输出流，他可以包装一个其他类型的源输入流，如文件输入流；
2. 通过对象输入流的`readObject()`方法度对象。

Java 中相关的 API：
1. `java.io.ObjectOutputStream`代表对象输出流，其`writeObject(Object o)`方法可以对参数指定的对象进行序列化，把得到的字节序列写到一个目标输出流中。
2. `java.io.ObjectInputStream`代表对象输入流，其`readObject(Object o)`方法从一个源输入流中读取字节序列，再把它们反序列化为一个对象，并将其返回。


## transient 关键字

当我们让某个类继承`Serializable`接口后，这个类将会采用默认的序列化方法，即其所有的属性和方法均会实现序列化。但现实情况是，对于某些敏感性字段，为了安全我们不希望其在网络中传输或存储到本地。transient 关键字就是用来解决这类问题的。被 transient 修饰的变量，在其生命周期中仅会存在于调用者的内存中。

当然，我们也可以通过继承`Externalizable`来自定义序列化行为。

transient 关键字总结：
1. 被 transient 修饰的变量将不再是对象序列化的一部分，该变量的内容在序列化后无法获得访问；
2. transient 关键字只能修饰变量，不能修饰类和方法。注意：本地变量是不能被 transient 修饰的。变量如果是用户自定义类变量，则该类必须实现`Serializable`接口。
3. 被 transient 修饰的变量不再被序列化。静态变量无论是否有 transient 关键字修饰，均不能被序列化。

关于第三点，可以理解为：静态变量不属于某个对象，而是属于类的，而序列化是针对对象而言的。

## serialVersionUID 的作用

serialVersionUID 字面上的意思就是序列化的版本号，凡是实现了 Serializable 接口的类都有一个表示序列化版本标识符的静态变量。


```java
private static final long serialVersionUID = 1L;
```

serialVersionUID 有两种方法来生成，一种是上面的形式，默认值为`1L`。另一种是根据类名、接口名、方法名和属性等来生成的。

当没有指定 serialVersionUID 时，Java 编译器会自动为这个 class 进行一个摘要算法，得到一个 serialVersionUID。只要这个文件被修改，相应的 serialVersionUID 就会完全不同，这样出于安全考虑，程序就会抛出错误。为此，需要主动指定一个 serialVersionUID， 这样在序列化后，添加或删除某一个字段或方法，不会影响到后期的还原。还原后的对象仍然可以使用，并且新增的方法或属性也可以使用。


## 参考资料

1. [序列化-维基百科](https://zh.wikipedia.org/wiki/%E5%BA%8F%E5%88%97%E5%8C%96)
2. [Java基础学习总结——Java对象的序列化和反序列化](https://www.cnblogs.com/xdp-gacl/p/3777987.html)
3. 


