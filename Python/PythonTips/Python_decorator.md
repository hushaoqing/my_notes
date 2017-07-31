## Decorator
```
def function(func):
    print func
    def wrapper(*args, **kwargs):
        self = args[0]
        try:
            func(*args, **kwargs)
        except:
            self.log("function {} error.".format(func.__name__))
    return wrapper

class ClassName(object):
    """docstring for ClassName"""
    def log(self, con):
        print con

    @function
    def test_g(self):
        raise TypeError

    def test_loop(self):
        for i in range(10):
            self.test_g()

ClassName().test_loop()
#<function test_g at 0x7fd5fe0140c8>
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
#function test_g error.
```

## Decorator, inspect, functools.wraps
```
import traceback
import inspect
from functools import wraps

def function(func):
    print func
    @wraps(func)
    def wrapper(*args, **kwargs):
        print args
        print kwargs

        for i in inspect.stack():
            print i
        self = args[0]
        try:
            func(*args, **kwargs)
        except:
            self.log("instance {} error;\nfunction {} error.\n {}".format(self, func.__name__, traceback.format_exc()))
    return wrapper

class ClassName(object):
    """docstring for ClassName"""
    def log(self, con):
        print con

    @function
    def test_g(self):
        raise TypeError

    def test_loop(self):
        for i in range(3):
            self.test_g()

class ClassName1(ClassName):
    """docstring for ClassName1"""
    def funct(self):
        super(ClassName1, self).test_loop()

ClassName1().funct()
print ClassName().test_g.__name__

#output
<function test_g at 0x7f493d7770c8>
(<__main__.ClassName1 object at 0x7f493d76a350>,)
{}
(<frame object at 0x7f493d872a00>, '/home/tmp/o.py', 131, 'wrapper', ['        for i in inspect.stack():\n'], 0)
(<frame object at 0x7f493dafc590>, '/home/tmp/o.py', 156, 'funct', ['        super(ClassName1, self).test_g()\n'], 0)
(<frame object at 0x7f494103a050>, '/home/tmp/o.py', 158, '<module>', ['ClassName1().funct()\n'], 0)
instance <__main__.ClassName1 object at 0x7f493d76a350> error;
function test_g error.
 Traceback (most recent call last):
  File "/home/tmp/o.py", line 135, in wrapper
    func(*args, **kwargs)
  File "/home/tmp/o.py", line 147, in test_g
    raise TypeError
TypeError

test_g
```
