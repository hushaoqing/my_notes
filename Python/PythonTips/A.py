# !usr/bin/python
# coding=utf-8


def function1():
    co = [0]
    def function3():
        co[0] += 1
    def function2():
        co[0] += 1

    function2()
    function3()
    return co[0]
if __name__ == '__main__':
    print function1() # 2

class lazyproperty(object):
    """docstring for lazyproperty"""
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            print instance
            value = self.func(instance)
            print self.func.__name__
            setattr(instance, self.func.__name__, value)
            return value
import math
class circle(object):
    """docstring for circle"""
    def __init__(self, arg):
        self.arg = arg

    @lazyproperty
    def area(self):
        print "Computing area"
        return math.pi * self.arg ** 2

class ClassName(object):
  """docstring for ClassName"""
  def __init__(self):
    self.l = []
    self.le = 0

  @property
  def __len__(self):
    return self.le

  def add(self, a):
    self.l.append(a)
    self.le += 1
# you can use len() on ClassName because of __len__

if __name__ == '__main__':
    c = circle(4)
    print vars(c)
    print c.area
    print "*" * 10
    print vars(c)
    print c.area
# {'arg': 4}
# <__main__.circle object at 0x7fd19254e390>
# Computing area
# area
# 50.2654824574
# **********
# {'area': 50.26548245743669, 'arg': 4}
# 50.2654824574
# [Finished in 0.0s]