## Chapter 2
```
x = 1
t = [x for x in "abc"]
print locals()

# python 2.x
# x == c
print x

# python 3.x
# x == 1
print x
```

如果做的是国际化软件,那么 _ 可能就不是一个理想的占位符,因为它也是gettext.gettext函数的常用别名,gettext 模块的文档(https://docs.python.org/3/library/gettext.html)里提到了这一点。在其他情况下,_ 会是一个很好的占位符。

```
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
```
a. t 变成 (1, 2, [30, 40, 50, 60])。
b. 因为 tuple 不支持对它的元素赋值,所以会抛出 TypeError 异常。
c. 以上两个都不是。
d. a 和 b 都是对的。

##### ***answer*** b 是对的!

* 不要把可变对象放在元组里面。
* 增量赋值不是一个原子操作。我们刚才也看到了,它虽然抛出了异常,但还是完成了操作。
* 查看 Python 的字节码并不难,而且它对我们了解代码背后的运行机制很有帮助。

调用类时会运行类的 __new__ 方法创建一个实例,然后运行 __init__ 方法,初始化实例,最后把实例返回给调用方。因为 Python 没有 new 运算符,所以调用类相当于调用函数。


可调用对象都能通过内置的 callable() 函数检测
\__call\__  method-wrapper  实现 () 运算符;即可调用对象协议