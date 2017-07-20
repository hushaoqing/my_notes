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


## Chapter 7

函数装饰器在导入模块时立即执行,而被装饰的函数只在明确调用时运行。这突出了 Python 程序员所说的导入时和运行时之间的区别.
闭包 --> 自由变量(free variable)
```
#PY2 and PY3:
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

#PY3:
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
#PY2:
#Python 2 没有 nonlocal,因此需要变通方法,“PEP 3104—Access to Names in Outer Scopes”(nonlocal 在这个 PEP 中引入,http://www.python.org/dev/peps/pep-3104/)中的第三个代码片段给出了一种方法。基本上,这种处理方式是把内部函数需要修改的变量(如 count 和 total)存储为可变对象(如字典或简单的实例)的元素或属性,并且把那个对象绑定给一个自由变量。
```