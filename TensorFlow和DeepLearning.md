
## TensorFlow入门

### 计算模型


```python
import tensorflow as tf
import numpy as np
```

tensorflow 是一个通过计算图的形式来表述计算的编程系统。
tensorflow 中的每一个计算都是计算图上的一个节点，而节点之间的边描述了计算之间的依赖关系。


```python
a = tf.Variable([1.0, 2.0, 3.0], name='a')
b = tf.Variable([2.0, 3.0, 4.0], name='b')
result = a + b
```

在 tensorflow 程序中，系统会自动维护一个默认的计算图，通过 *tf.get_default_graph* 函数可以获得当前默认的计算图。


```python
print(a.graph is tf.get_default_graph())
```

    True
    

除了使用默认的计算图，tensorflow 支持通过 *tf.Graph* 函数来生成新的计算图。
不同计算图上的张量和运算都不会共享。


```python
g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable("v", initializer=tf.zeros_initializer(dtype=tf.float32), shape=[2, 3])

g2 = tf.Graph()
with g2.as_default():
    v = tf.get_variable("v", initializer=tf.ones_initializer(dtype=tf.float32), shape=[2, 3])

with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        print(sess.run(tf.get_variable("v")))

with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        print(sess.run(tf.get_variable("v")))
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    [[1. 1. 1.]
     [1. 1. 1.]]
    

tensorflow 中的计算图除了可以用来隔离张量，还提供了管理张量和计算的机制。计算图可以通过 *tf.Graph.device* 函数指定运行计算的设备（如 GPU）。

在一个计算图中，可以通过**集合**（*collection*）来管理不同类别的资源。比如：
*tf.add_to_collection* 函数可以将资源加入一个或多个集合中。
*tf.get_collection* 函数获取一个集合中的所有资源。
这里的资源指的是张量、变量或者程序运行所需要的队列资源等等。

### 张量

**张量**（tensor）可以简单理解为多维数组。其中，零阶张量表示**标量**（scalar），即一个数；第一阶张量为**向量**（vector），即一个一维数组；第n阶张量可以理解为一个n维数组。但是，在tensorflow中，张量只是对运算结果的引用，其没有真正保存数字，保存的是得到这些数字的计算过程。


```python
print(result)
```

    Tensor("add_2:0", shape=(3,), dtype=float32)
    

一个张量主要保存了三个属性：
+ **名字**（name）：张量的唯一标识符，同时也给出了这个张量是如何计算出来的。命名形式 *node:src_output*，node为节点名称，src_output表示当前张量来自节点的第几个输出。
+ **维度**（shape）：张量的维度信息。
+ **类型**（dtype）：数据类型。tensorflow 会自动对参与运算的所有张量进行类型检查，当发现类型不匹配时会报错。不带小数点默认为int32，带小数点的则为float32。

张量的使用：
+ 对中间计算结果的引用，可以大大提高代码的可读性。
+ 当计算图构造完之后，可以用来获得计算结果。

### 会话

tensorflow 中使用会话的模式一般有两种：
+ 明确调用会话生成函数和关闭会话函数。
+ 通过 python 上下文管理器（**with** 关键字）来使用。只要将所有的计算放在 with 的内部就可以，上下文管理器退出时会自动释放所有资源。


```python
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
...
sess.close()
```


```python
with tf.Session() as sess:
    ...
```

tensorflow 中的会话和计算图一样，也有一个系统默认会话。但是 tensorflow 不会自动生成默认会话，而是需要手动指定。当默认的会话被指定之后可以通过 *tf.Tensor.eval* 函数来计算一个张量的取值。 

在交互式环境下，通过 *tf.InteractiveSession* 函数创建的会话，可以自动注册为默认会话。

### 前向传播算法

神经网络可以将输入的特征向量经过层层推导得到最后的输出，并通过这些输出解决分类或回归问题。这里介绍最简单的**全连接网络结构**（相邻两层之间的任意两个节点之间都有连接）的前向传播算法。所谓神经网络的结构，就是指不同的神经元之间的连接结构。

一个最简单的神经元结果的输出就是所有输入的加权和，而不同输入的权重就是神经元的参数。神经网络的优化过程就是优化神经元中参数的取值过程。

前向传播算法可以通过矩阵相乘来表示。即 $ y=x*W+b $。其中，$ W $是权重，$ b $是偏置值。
$$
[y]=[x_1,x_2]
\left[
\begin{matrix}
W_{1,1}^{(1)} W_{1,2}^{(1)} W_{1,3}^{(1)}\\
W_{2,1}^{(1)} W_{2,2}^{(1)} W_{2,3}^{(1)}
\end{matrix}
\right]
+[b_1, b_2, b_3]
$$

### 神经网络参数和tensorflow变量

在 tensorflow 中，变量的作用就是保存和更新神经网络中的参数。一般给参数赋予随机初始值。tensorflow 中支持的随机数生成器有：
+ tf.random_normal()：正态分布
+ tf.truncated_normal()：正态分布，但是如果随机出来的数偏离平均值两个标准差，就会重新随机。
+ tf.random_uniform()：平均分布
+ tf.random_gamma()：Gamma 分布

同时，tensorflow 也支持通过常数来初始化一个变量：
+ tf.zeros()：产生全0的数组
+ tf.ones()：产生全1的数组
+ tf.fill()：产生全部为给定数字的数组
+ tf.constant()：产生一个给定值的数组


```python
baises = tf.Variable(tf.ones([3]))
# 以 baises 的初始值来初始化变量 w
w = tf.Variable(baises.initialized_value())
with tf.Session() as sess:
    # 初始化所有变量
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(w))

    
```

    [1. 1. 1.]
    

在 tensorflow 中，一个变量的值在被使用之前，一定先要明确地进行初始化。变量的声明函数 *tf.Variable* 是一个运算，其输出结果就是一个张量。所有的变量都会自动加入到 *GraphKeys.VARIABLES* 这个集合，通过调用 *tf.all_variables* 函数可以拿到当前计算图上的所有变量，有助于持久化整个计算图的运行状态。可以通过变量声明中的 *trainable* 参数来区分需要优化的参数（比如神经网络中的参数）和其他参数（比如迭代次数）。若变量的参数 *trainable* 为 True，那么这个变量就会被加入到 *GraphKeys.TRAINABLE_VARIABLES* 集合，通过 *tf.trainable_variables* 函数可以得到所有需要优化的参数。tensorflow 中提供的神经网络优化算法会将 *GraphKeys.TRAINABLE_VARIABLES* 集合中的变量作为默认的优化对象。

变量的最重要的两个属性是：**维度**和**类型**。变量的类型是不可改的。而维度在程序的运行中是有可能改变的，但是需要修改参数 *validate_shape=False*。

### 反向传播算法

反向传播算法 *backpropagation* 是神经网络优化算法中最常用的方法。反向传播算法实现了一个迭代的过程。在每次迭代的开始，都要选取一小部分训练数据，这一小部分数据叫做一个 *batch*，然后，这个 batch 的样例会通过前向传播算法得到神经网络模型的预测结果。根据计算得到当前神经网络模型的预测答案和正确答案之间的差距，基于这个差距，反向传播算法会相应更新神经网络参数的取值，使得这个batch上神经网络模型的预测结果和真是答案更加接近。

tensorflow 提供了 *placeholder* 机制用于提供输入数据。这样就避免了每轮迭代中都要生成一个选取的数据常量。 placeholder 相当于定义了一个位置，其数据在程序运行时才指定。在 placeholder 定义中，需要指定数据类型且不可更改，维度信息可以根据数据推导得到。


```python
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1))

x = tf.placeholder(tf.float32, shape=(3, 2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
#     print(sess.run(y))
#     会报错，因为没有为 placeholder 提供数据。
    print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
```

    [[ 0.36959141]
     [-0.2422628 ]
     [ 0.09316885]]
    

*feed_dict* 用来指定 $ x $ 的取值。*feed_dict* 是一个字典（map），在字典中需要给出每个用到的 placeholder 的取值。

在得到一个 batch 的前向传播结果之后，需要定义一个损失函数 *loss function* 来刻画当前预测值和真是答案之间的差距。然后通过 *backpropagation* 来调整神经网络参数的取值使得差距可以被缩小。


```python
# 随机生成模拟数据包
from numpy.random import RandomState

# 预定义值
batch_size = 8 # 训练数据 batch 的大小
lr = 0.01

# 
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")

# 定义神经网络的参数
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义神经网络的前向传播算法
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播算法
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(learning_rate=lr).minimize(cross_entropy)

# 生成模拟数据
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# 创建绘画来运行程序
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(w1))
    print(sess.run(w2))

    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})

        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print("After %d training step(s), cross entropy on all data is %g" % (i, total_cross_entropy))

    print(sess.run(w1))
    print(sess.run(w2))
```

    [[-0.8113182   1.4845988   0.06532937]
     [-2.4427042   0.0992484   0.5912243 ]]
    [[-0.8113182 ]
     [ 1.4845988 ]
     [ 0.06532937]]
    After 0 training step(s), cross entropy on all data is 0.065389
    After 1000 training step(s), cross entropy on all data is 0.00119688
    After 2000 training step(s), cross entropy on all data is -0
    After 3000 training step(s), cross entropy on all data is -0
    After 4000 training step(s), cross entropy on all data is -0
    [[-2.4540348  3.022714   2.922476 ]
     [-3.9022913  1.4489784  3.4259934]]
    [[-2.1807733]
     [ 3.2438502]
     [ 2.4208493]]
    

训练神经网络的过程可以分为以下3个步骤：
1. 定义神经网络的结构和前向传播的输出结果
2. 定义损失函数以及选择反向传播优化的算法
3. 生成会话并且在训练数据上反复运行反向传播优化算法

### 深层神经网络

深度学习的定义：一类通过***多层非线性变换***对高复杂性数据建模算法的合集。而**深层神经网络**是实现***多层非线性变换***的常用方法，因此可以说，深度学习约等于深层神经网络。

#### 线性模型的局限性

只通过线性变换，任意层的全连接神经网络和单层神经网络模型的表达能力没有任何区别，它们都是线性模型。因此需要强调非线性变换来解决更复杂的问题。

#### 激活函数实现非线性

将每一个神经元的输出通过一个非线性函数，那么整个神经网络的模型就不再是线性的了。这个非线性函数就是激活函数。
$$ A_1=f(xW^{(1)}+b) $$
$$
A_1=[a_{11},a_{12},a_{13}]
=f(xW^{(1)}+b)
=f([x_1,x_2]
\left[
\begin{matrix}
W_{1,1}^{(1)} W_{1,2}^{(1)} W_{1,3}^{(1)}\\
W_{2,1}^{(1)} W_{2,2}^{(1)} W_{2,3}^{(1)}
\end{matrix}
\right]
+[b_1, b_2, b_3])
$$

tensorflow 目前提供了七种不同的非线性激活函数，*tf.nn.relu*、*tf.sigmoid*、*tf.tanh*是比较常用的几个。当然，*tf* 也支持使用自己定义的激活函数。

#### 多层网络解决异或运算

异或问题是神经网络发展史上一个很重要的问题。

#### 损失函数

神经网络的效果以及优化的目标是通过损失函数来定义的。

#### 分类问题

通过 *NN* 来解决多分类问题最常用的方法是设置 $n$ 个输出节点，其中 $n$ 为类别的个数。对于每一个样例，*NN* 可以得到一个 $n$ 维数组作为输出结果。数组中的每一个维度（即每一个输出节点）对应一个类别。那么输出向量越接近期望向量，即可认为其属于该类别。**交叉熵** *cross entropy* 是常用的评判方法之一，其用来刻画两个概率分布之间的距离。

给定两个概率分布 $p$ 和 $q$，通过 $q$ 来表示 $p$ 的交叉熵为：
$$H(p,q)=-\sum{p(x)\log{q(x)}}$$
为了应用交叉熵，可以将分类问题中“一个样例属于某一类别”看成一个概率事件。那么训练数据的正确答案就符合一个概率分布。而通过前向传播算法得到的结果可以通过 *Softmax* 回归来变成概率分布。

在 *tf* 中，*Softmax* 回归的参数被去掉了，只是一层额外的处理层，将 *NN* 的输出变成一个概率分布。

假设原始 *NN* 的输出为 $y_1,y_2,\dots,y_n$，那么经过 *Softmax* 回归处理后的输出为：
$$softmax(y)_i = y_i^{'} = \frac{e^{y_i}}{\sum_{j=1}^n{e^{y_j}}} $$
从交叉熵的公式可以看到，交叉熵函数是不对称的，即 $H(p,q)\neq H(q,p)$，因此，在作为 *NN* 的损失函数时，$p$ 代表的是正确答案，$q$ 代表的是预测值。

交叉熵的值越小，表示两个概率分布越接近。


```python
# 我们再来看一下前面使用 tf 实现过的交叉熵
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
# tf.clip_by_value 函数将张量中的数值限定在一个范围内，从而避免一些运算错误
# tf.log 函数对张量中的每一个元素依次求对数
# 矩阵元素之间的乘法运算，这里没有使用 tf.matmul 函数（矩阵乘法）
# 通过上述三步计算，得到一个 nxm 的二维矩阵，其中 n 为一个 batch 中样例的数量，m 为分类的类别数量
# tf.reduce_mean 函数直接对整个矩阵求平均
```

*tf* 对交叉熵和 *softmax* 进行了封装，提供 *tf.nn.softmax_cross_entropy_with_logits* 函数。在只有一个正确答案的分类问题中，*tf* 还提供了 *tf.nn.softmax_cross_entropy_with_logits_v2* 函数来进一步加速计算过程。


```python
# y 是 NN 的输出结果，y_ 是正确答案
# 参数形式必须是 labels=和logits=
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_)
cross_entropy_ = tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=y_)
```

#### 回归问题

回归问题是对具体数值的预测。因而解决回归问题的神经网络一般只有一个输出节点，且其输出值就是预测值。常用的损失函数是**均方误差** *MSE，mean squared error*。定义如下:
$$MSE(y,y^{'})=\frac{\sum^n_{i=1}{(y_i-y_i^{'})^2}}{n}$$
其中，$y_i$ 为一个 batch 中的第 $i$ 个数据的正确答案，而 $y_i^{'}$ 为 *NN* 给出的预测值。


```python
mse = tf.reduce_mean(tf.square(y_ - y))
```

#### 自定义损失函数

略。

#### 神经网络优化算法

采用 *backpropagation + gradient descent* 来调整 *NN* 中参数的取值。*gradient descent* 主要用于优化单个参数的取值，而 *backpropagation* 提供了一个高效的方式在所有参数上使用 *gradient descent*，从而使 *NN* 在训练数据集上的损失函数尽可能小。

#### gradient descent

假设 $\theta$ 表示 *NN* 中的参数，$J(\theta)$ 表示在给定参数值的情况下，训练数据集上损失函数的大小。那么整个优化过程可以抽象为，寻找参数 $\theta$，使得 $J(\theta)$ 最小。

目前常用的方法是 *gradient descent*，其会迭代式更新参数 $\theta$，不断沿着梯度相反的方向让参数朝着总损失更小的方向更新。定义一个学习率 $\eta$ *learning rate* 来表示每次参数更新的幅度。

缺点：
1. 不一定能得到全局最优解，而只是局部最优解
2. 计算时间太长，每次迭代都需要计算在**全部训练数据**上的损失函数

实际问题中，问题一不算一个问题，因为得到局部最优解就已经可以满足要求了。而问题二，可以使用**随机梯度下降算法***stochastic gradient descent* 来解决。即：每轮迭代中，随机优化**某一条训练数据**上的损失函数。缺点是：在某一条数据上损失函数更小不代表在全部数据上损失函数更小，可能连局部最优解也达不到。综合考虑：每次计算**一小部分训练数据**（称为一个 batch）的损失函数。


```python
batch_size = 60
STEPS = 5000

#准备数据
x = tf.placeholder(tf.float32, shape=(batch_size, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(batch_size, 1), name="y-input")

# 定义神经网络的结构和优化算法
loss = ...
train_step = tf.train.AdadeltaOptimizer(0.01).minimize(loss)

# 训练神经网络
with tf.Session() as sess:
    # 初始化参数
    ...
    for i in range(STEPS):
        # 准备 batch_size 个训练数据
        # 一般需要将训练数据随机打乱
        current_X, current_Y = ...
        sess.run(train_step, feed_dict={x: current_X, y_: current_Y})
```

#### 学习率的优化

#### 过拟合

#### 滑动平均模型

### 卷积神经网络

### 循环神经网络

*recurrent neural network, RNN* 和 *long short-term memory, LSTM*

*RNN* 主要用于处理和预测序列数据，其隐藏层之间的节点是有连接的，隐藏层的输入不仅包括输入层的输出，还包括上一时刻隐藏层的输出。


```python

```
