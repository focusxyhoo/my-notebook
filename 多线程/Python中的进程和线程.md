# Python中的进程和线程

## 多线程与多进程

实现多任务最常见的两种方式就是多进程和多线程了。多进程，顾名思义，多个进程并发执行，可以有效提高程序的执行效率，优点是非常稳定，即使有子进程崩溃了，主进程和其他进程依然可以继续执行，但缺点是在windows下创建进程的开销比较大，而且如果进程太多，往往会影响整个系统的调度。而多线程是指一个进程内多个线程同时执行，进而提高程序执行效率，其优点可能是比多进程稍微快一点，但缺点也很明显，多线程中一个线程出现了问题就会导致整个进程崩溃，因此稳定性不是很高。

## GIL是什么？

首先确定，Python中的多线程是假的多线程。这是由于**全局解释器锁GIL**的存在。

Python代码的执行由Python虚拟机（解释器）来控制。Python在设计之初就考虑要在主循环中，同时只有一个线程在执行，就像单CPU的系统中运行多个进程那样，内存中可以存放多个程序，但任意时刻，只有一个程序在CPU中运行。同样地，虽然Python解释器可以运行多个线程，只有一个线程在解释器中运行。

对Python虚拟机的访问由全局解释器锁（GIL）来控制，正是这个锁能保证同时只有一个线程在运行。在多线程环境中，Python虚拟机按照以下方式执行：

1. 设置GIL，
2. 切换到一个线程去执行，
3. 运行（一般执行100条字节码），
4. 把线程设置为睡眠状态，
5. 解锁GIL，
6. 再次重复以上步骤。

对所有面向I/O的（会调用内建的操作系统C代码的）程序来说，GIL会在这个I/O调用之前被释放，以允许其他线程在这个线程等待I/O的时候运行。如果某线程并未使用很多I/O操作，它会在自己的时间片内一直占用处理器和GIL。也就是说，**I/O密集型**的Python程序比**计算密集型**的Python程序更能充分利用多线程的好处。

## I/O密集型VS计算密集型

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

## 总结

Python多线程相当于单核多线程，多线程有两个好处：CPU并行，IO并行，单核多线程相当于自断一臂。所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

## 参考资料

1. [Python中多进程在爬虫中的使用](https://blog.csdn.net/sinat_22594309/article/details/53727084)
2. [为什么有人说 Python 的多线程是鸡肋呢？ - DarrenChan陈驰的回答 - 知乎](https://www.zhihu.com/question/23474039/answer/269526476)
3. 

