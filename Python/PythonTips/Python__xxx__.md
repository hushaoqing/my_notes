# Python 用下划线作为变量前缀和后缀指定特殊变量
_xxx 不能用’from module import *’导入
\__xxx__ 系统定义名字
__xxx 类中的私有变量名
核心风格：避免用下划线作为变量名的开始。
```
object.__class__
object.__delattr__
object.__doc__
object.__format__
object.__getattribute__
object.__hash__
object.__init__
object.__new__
object.__reduce__
object.__reduce_ex__
object.__repr__
object.__setattr__
object.__sizeof__
object.__str__
object.__subclasshook__
```

## 类的基础方法
```
x = MyClass()      x.__init__()
repr(x)            x.__repr__()
str(x)             x.__str__()
bytes(x)           x.__bytes__()
format(x)          x.__format__()

1. 对__init__() 方法的调用发生在实例被创建 之后 。如果要控制实际创建进程，请使用__new__() 方法。
2. 按照约定__repr__()方法所返回的字符串为合法的 Python 表达式。
3. 在调用 print(x) 的同时也调用了__str__()方法。
4. 由于 bytes 类型的引入而从 Python 3 开始出现。
```

## 行为方式与迭代器类似的类
```
iter(seq)       seq.__iter__()
next(seq)       seq.__next__()
reversed(seq)   seq.__reversed__()
1. 无论何时创建迭代器都将调用__iter__()方法。这是用初始值对迭代器进行初始化的绝佳之处。
2. 无论何时从迭代器中获取下一个值都将调用__next__()方法。
3. __reversed__() 方法并不常用。它以一个现有序列为参数，并将该序列中所有元素从尾到头以逆序排列生成一个新的迭代器。
```

## 计算属性
```
x.my_property           x.__getattribute__('my_property')
x.my_property           x.__getattr__('my_property')
x.my_property = value   x.__setattr__('my_property',value)
del x.my_property       x.__delattr__('my_property')
dir(x)                  x.__dir__()

1. 如果某个类定义了__getattribute__() 方法，在 每次引用属性或方法名称时Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。
2. 如果某个类定义了__getattr__() 方法，Python 将只在正常的位置查询属性时才会调用它。如果实例 x 定义了属性color，x.color 将不会 调用x.__getattr__('color')；而只会返回x.color已定义好的值。
3. 无论何时给属性赋值，都会调用__setattr__()方法。
4. 无论何时删除一个属性，都将调用__delattr__()方法。
5. 如果定义了__getattr__() 或__getattribute__() 方法，__dir__() 方法将非常有用。通常，调用 dir(x) 将只显示正常的属性和方法。如果__getattr()__方法动态处理color 属性，dir(x) 将不会将color 列为可用属性。可通过覆盖__dir__() 方法允许将color 列为可用属性，对于想使用你的类但却不想深入其内部的人来说，该方法非常有益。
```
## 行为方式与函数类似的类
```
my_instance()   my_instance.__call__()


zipfile 模块 通过该方式定义了一个可以使用给定密码解密 经加密 zip 文件的类。该 zip解密 算法需要在解密的过程中保存状态。通过将解密器定义为类，使我们得以在 decryptor 类的单个实例中对该状态进行维护。状态在__init__() 方法中进行初始化，如果文件经加密 则进行更新。但由于该类像函数一样“可调用”，因此可以将实例作为map() 函数的第一个参数传入，代码如下：
# excerpt from zipfile.py 
class _ZipDecrypter:  
    def __init__(self, pwd):  
        self.key0 = 305419896 
        self.key1 = 591751049 
        self.key2 = 878082192  
        for p in pwd:  
             self._UpdateKeys(p) 
    def __call__(self, c):   
         assert isinstance(c, int)  
         k = self.key2 | 2 c = c ^ (((k * (k^1)) >>  & 255)  
         self._UpdateKeys(c) 
         return c   
zd = _ZipDecrypter(pwd)  
bytes = zef_file.read(12)  
h = list(map(zd, bytes[0:12]))  
 
1. _ZipDecryptor 类维护了以三个旋转密钥形式出现的状态，该状态稍后将在 _UpdateKeys()方法中更新（此处未展示）。
2. 该类定义了一个 __call__() 方法，使得该类可像函数一样调用。在此例中，__call__()对 zip 文件的单个字节进行解密，然后基于经解密的字节对旋转密码进行更新。
3. zd 是 _ZipDecryptor 类的一个实例。变量 pwd 被传入 __init__()方法，并在其中被存储和用于首次旋转密码更新。
4. 给出 zip 文件的头 12 个字节，将这些字节映射给 zd 进行解密，实际上这将导致调用 __call__() 方法 12 次，也就是 更新内部状态并返回结果字节 12 次。
```

## 行为方式与序列类似的类
```
len(seq)    seq.__len__()
x in seq    seq.__contains__(x)


cgi 模块 在其FieldStorage 类中使用了这些方法，该类用于表示提交给动态网页的所有表单字段或查询参数。
# A script which responds to http://example.com/search?q=cgi 
import cgi fs = cgi.FieldStorage() 
if 'q' in fs:  
    do_search() 

# An excerpt from cgi.py that explains how that works class FieldStorage: . . .
def __contains__(self, key): 
     if self.list is None:  
          raise TypeError('not indexable')  
     return any(item.name == key for item in self.list) 

def __len__(self): 
 return len(self.keys()) 
 
1. 一旦创建了 cgi.FieldStorage 类的实例，就可以使用 “in” 运算符来检查查询字符串中是否包含了某个特定参数。
2. 而 __contains__()方法是令该魔法生效的主角。
3. 如果代码为 if 'q' in fs，Python 将在 fs 对象中查找 __contains__() 方法，而该方法在cgi.py 中已经定义。'q' 的值被当作key 参数传入__contains__()方法。
4. 同样的 FieldStorage 类还支持返回其长度，因此可以编写代码 len(fs) 而其将调用FieldStorage 的__len__()方法，并返回其识别的查询参数个数。
5. self.keys() 方法检查 self.list is None 是否为真值，因此 __len__ 方法无需重复该错误检查。
```

## 行为方式与字典类似的类
```
x[key]              x.__getitem__(key)
x[key] = value      x.__setitem__(key, value)
del x[key]          x.__delitem__(key)
x[nonexistent_key]  x.__missing__(nonexistent_key)


cgi 模块 的FieldStorage 类 同样定义了这些特殊方法，也就是说可以像下面这样编码：
# A script which responds to http://example.com/search?q=cgi import cgi fs = cgi.FieldStorage() 
if 'q' in fs:  
    do_search(fs['q']) 

# An excerpt from cgi.py that shows how it works class FieldStorage: . . . 
def __getitem__(self, key):  
    if self.list is None:  
          raise TypeError('not indexable')  
    found = [] 
    for item in self.list:  
          if item.name == key:  
          found.append(item) 
    if not found: 
          raise KeyError(key) 
    if len(found) == 1:
          return found[0]  
    else:  return found 
 
1. fs 对象是 cgi.FieldStorage 类的一个实例，但仍然可以像 fs['q']这样估算表达式。
2. fs['q'] 将 key 参数设置为 'q' 来调用 __getitem__() 方法。然后它将在其内部维护的查询参数列表 (self.list) 中查找一个.name 与给定键相符的字典项。
```

## 可比较的类
```
x == y      x.__eq__(y)
x != y      x.__ne__(y)
x < y       x.__lt__(y)
x <= y      x.__le__(y)
x > y       x.__gt__(y)
x >= y      x.__ge__(y)
if x:       x.__bool__()

1. 如果定义了__lt__() 方法但没有定义__gt__() 方法，Python 将通过经交换的算子调用__lt__() 方法。然而，Python 并不会组合方法。例如，如果定义了__lt__() 方法和__eq()__方法，并试图测试是否 x <= y，Python 不会按顺序调用__lt__() 和__eq()__ 。它将只调用__le__() 方法。
```
## 可序列化的类
```
copy.copy(x)                            x.__copy__()
copy.deepcopy(x)                        x.__deepcopy__()
pickle.dump(x, file)                    x.__getstate__()
pickle.dump(x, file)                    x.__reduce__()
pickle.dump(x, file, protocol_version)  x.__reduce_ex__(protocol_version)
x = pickle.load(file)                   x.__getnewargs__()
x = pickle.load(file)                   x.__setstate__()

1. 要重建序列化对象，Python 需要创建一个和被序列化的对象看起来一样的新对象，然后设置新对象的所有属性。__getnewargs__()方法控制新对象的创建过程，而__setstate__() 方法控制属性值的还原方式。
```

## 可在 with 语块中使用的类
```
with x:          x.__enter__(), x.__exit__()
```

## 如果知道自己在干什么，你几乎可以完全控制类是如何比较的、属性如何定义，以及类的子类是何种类型。

```
x = MyClass()                       x.__new__()
del x                               x.__del__()
                                    x.__slots__()
hash(x)                             x.__hash__()
x.color                             type(x).__dict__['color'].__get__(x, type(x))
x.color = 'PapayaWhip'              type(x).__dict__['color'].__set__(x, 'PapayaWhip')
del x.color                         type(x).__dict__['color'].__del__(x)
isinstance(x, MyClass)              MyClass.__instancecheck__(x)
issubclass(C, MyClass)              MyClass.__subclasscheck__(C)
issubclass(C, MyABC)                MyABC.__subclasshook__(C)
```