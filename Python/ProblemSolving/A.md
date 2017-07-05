## Chapter 3 [Stack, Queue, Deque, Orderd List, Linked List]

```
class Stack(object):
  """docstring for Stack"""
  def __init__(self):
    self.stack = []
  def pop(self):
    return self.stack.pop()
  def push(self, i):
    self.stack.append(i)
  def isEmpty(self):
    return self.stack == []
  def peek(self):
    return self.stack[-1]
  def lenth(self):
    return len(self.stack)
```

* Chapter 3.7

```
def StackTest():
  tag = True
  s = Stack()
  for i in "([{":
    if i in "([{":
      s.push(i)
    else:
      if s.isEmpty():
        tag = False
      else:
        if not "([{".index(s.pop()) == ")]}".index(i):
          tag = False
  if tag and s.isEmpty():
    print True
  else:
    print False
```

* Chapter 3.8

```
def binay(n, base):
  s = Stack()
  while n > 0:
    n, mod = divmod(n, base)
    s.push(mod)
  tt = ""
  while not s.isEmpty:
    tt += str(s.pop)
  return tt
```

* Chapter 3.9

```
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty and prec[opStack.peek()] >= prec[token]:
                  postfixList.append(opStack.pop())
            opStack.push(token)

    print opStack.stack
    while not opStack.isEmpty:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

def postfixEval(postfixExpr):
  import operator as op
  opStack = Stack()
  list_token = postfixExpr.split()
  for token in list_token:
    if token in "0123456789":
      opStack.push(int(token))
    else:
      a = opStack.pop()
      b = opStack.pop()
      resilt = {"*": op.mul,
                "+": op.add,
                "-": op.sub,
                "/": op.div}[token](a, b)
      opStack.push(resilt)
  return opStack.pop()
print(postfixEval('7 8 + 3 2 + +'))
```

## Chapter 4 Recursion

## Chapter 5 Searching and Sorting

### Searching
```
class HashTable(object):
    """docstring for HashTable"""
    def __init__(self):
        self.size     = 11
        self.slots    = [None] * self.size
        self.data     = [None] * self.size
        self.hashfunc = lambda key,size: key % size
        self.rehash   = lambda oldhash,size,: (oldhash + 1) % size
    def put(self, key, data):
        oldhash = self.hashfunc(key, self.size)
        if self.slots[oldhash] is None:
            self.slots[oldhash] = key
            self.data[oldhash]  = data
        else:
            if self.slots[oldhash] == key:
                self.data[oldhash] = data
            else:
                nextslot = self.rehash(oldhash, self.size)
                while nextslot is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, self.size)
                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot]  = data
                else:
                    self.data[nextslot] = data
    def get(self, key):
        oldhash = self.hashfunc(key, self.size)
        data = None
        found = False
        stop = False
        p = oldhash
        while self.slots[p] is not None and not found and not stop:
            if self.slots[p] == key:
                found = True
            else:
                oldhash = self.rehash(p, self.size)
                if p == oldhash:
                    stop = True
        return data
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
if __name__ == '__main__':
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[77] = "bird"
    print h.slots
    print h[77]
    # [77, None, None, None, 26, None, None, None, None, None, 54]
    # ['bird', None, None, None, 'dog', None, None, None, None, None, 'cat']
    # bird
```
### Sorting
```
def bubbleSort(alist):
    for pas in range(0, len(alist)):
        for j in range(pas):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

def selectionSort(alist):
    for pas in range(len(alist)-1,0,-1):
        pos = 0
        for l in range(1, pas + 1):
            if alist[l] > alist[pos]:
                pos = l
        alist[pas], alist[pos] = alist[pos], alist[pas]

def insertSort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        p = i
        while p > 0 and alist[p - 1] > current:
            alist[p] = alist[p - 1]
            p -= 1
        alist[p] = current
```