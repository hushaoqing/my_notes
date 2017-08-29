## Scrapy engine

### CallLaterOnce (基于twisted reactor)每次调用重新赋值，用于不断获取下一个request
```
# !usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from twisted.internet import reactor

class CallLaterOnce(object):
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """

    def __init__(self, func, *a, **kw):
        self._func = func
        self._a = a
        self._kw = kw
        self._call = None

    def schedule(self, delay=0):
        if self._call is None:
            self._call = reactor.callLater(delay, self)

    def cancel(self):
        if self._call:
            self._call.cancel()

    def __call__(self):
        self._call = None
        return self._func(*self._a, **self._kw)

def function():
    print "a"

a = CallLaterOnce(function)
print a.schedule()
a = CallLaterOnce(function)
print a.schedule()
a = CallLaterOnce(function)
print a.schedule()
reactor.run()
# None
# None
# None
# a
# a
# a
```