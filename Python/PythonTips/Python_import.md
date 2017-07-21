## 在Python中使用import语句导入模块时，python通过三个步骤来完成这个行为。
1. 在python模块加载路径中查找相应的模块文件
2. 将模块文件编译成中间代码
3. ***执行模块文件中的代码***

因为这个特性，假如模块中有一个print语句 ， 那么， 当该模块被第一次加载的时候，该输出语句就会将内容输出，但是由于模块只能被import一次，所以，当模块第二次被加载的时候，上面这三个步骤都不会被执行，那么，这个输出不会再次出现。

## file A.py:
```
# !usr/bin/python
# coding=utf-8

from B import loa

class A(object):
    """docstring for ClassName"""
    def __init__(self):
        pass

    def a(self):
        raise NotImplementedError()

    def aa(self):
        raise NotImplementedError()

print "start"
loa(A)
```

## file B.py:
```
# !usr/bin/python
# coding=utf-8

def loa(ooo):
    ooo.a = ad

def ad(self):
    print "sss"
```

## file C.py:
```
# !usr/bin/python
# coding=utf-8

from A import A
A().a()
# start
# sss
```

如何实现python -m 参数的功能？
```
# !usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import click
import pdir

@click.command()
@click.option("-m", default="pdir")
def imp_package(m):
    p = __import__(m)
    print pdir(p)

if __name__ == '__main__':
    imp_package()
```