# Mro
一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：

* 子类永远在父类前面
* 如果有多个父类，会根据它们在列表中的顺序被检查
* 如果对下一个类存在两个合法的选择，选择第一个父类
```
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"

class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"

class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"

class C(A, B):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"
print C.mro() # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <type 'object'>]
```


## super 原理  
[Python Mro](https://www.python.org/download/releases/2.3/mro/)
```
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```
其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

* 获取 inst 的 MRO 列表
* 查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro\[index + 1]

Summary:

* 事实上，super 和父类没有实质性的关联。
* super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。