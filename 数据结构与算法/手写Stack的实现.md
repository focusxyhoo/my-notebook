# 手写Stack的实现

具体代码如下：

```java
import java.util.LinkedList;
public class MyStack<T> {
    private LinkedList<T> myStack = new LinkedList<T>();
    public void push(T t) {
        myStack.addFirst(t);
    }
    public T pop() {
        return myStack.removeFirst();
    }
    public T peek() {
        return myStack.getFirst();
    }
    public boolean empty() {
        return myStack.isEmpty();
    }
    public String toString() {
        return myStack.toString();
    }
}

```



