## python share class variables
```
# !usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ClassName1(object):
    """docstring for ClassName1"""
    urls = []

    def add(self, l):
        self.urls.append(l)

a = ClassName1()
a.add("a")
b = ClassName1()
b.add("b")

print a.urls
print b.urls
print a.__dict__
print ClassName1.__dict__
"""
['a', 'b']
['a', 'b']
{}
{'__module__': '__main__', 'add': <function add at 0x7feb765b0668>, 'urls': ['a', 'b'], '__dict__': <attribute '__dict__' of 'ClassName1' objects>, '__weakref__': <attribute '__weakref__' of 'ClassName1' objects>, '__doc__': 'docstring for ClassName1'}
"""
```