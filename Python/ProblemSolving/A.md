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

```
class Node(object):
    """docstring for Node"""
    def __init__(self, initdata):
        self.data = initdata
        self.next = Node

class UnorderedList(object):
    """docstring for UnorderedList"""
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is Node
    def add(self, item):
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
    def remove(self, item):
        current = self.head
        pre = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                pre = current
                current = current.next
        if pre is None:
            self.head = current.next
        else:
            pre.next = current.next
```

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

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    print("Merging ",alist)

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        pp = quick(alist, first, last)
        quickSortHelper(alist, first, pp - 1)
        quickSortHelper(alist, pp + 1, last)
def quick(alist, first, last):
    tag = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= tag:
            left_mark += 1
        while alist[right_mark] >= tag and right_mark >= left_mark:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    print alist
    return right_mark
```

## Chapter 6 Tree
```
myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]
def BinaryTreeUseList(r):
    return [r, [], []]
def insertLeft(root, item):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [item, t, []])
    else:
        root.insert(1, [item, [], []])
    return root
def insertRight(root, item):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [item, [], t])
    else:
        root.insert(2, [item, [], []])
    return root

class BinaryTree:
    """docstring for BinaryTree"""
    def __init__(self, arg):
        self.key = arg
        self.left = None
        self.right = None
    def insertLeft(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.left = self.left
            self.left = t
    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.right = self.right
            self.right = t
            
def buildParseTree(flist):
    fl = flist.split()
    fstack = Stack()
    eTree = BinaryTree("")
    fstack.push(eTree)
    current = eTree
    for f in fl:
        print f
        print "*" * 20
        print fstack.lenth()
        if f == "(":
            current.insertLeft("")
            fstack.push(current)
            current = current.left
        elif f.isdigit(): # numbers: 3, 6; elif f.isdigit()
            current.root = int(f)
            parent = fstack.pop()
            current = parent
        elif f in ['+', '-', '*', '/']:
            current.root = f
            current.insertRight("")
            fstack.push(current)
            current = current.right
        elif f == ')':
            current = fstack.pop()
        else:
            raise ValueError
        print fstack.lenth()
    return eTree
pt = buildParseTree("( ( 10 + 5 ) * 3 )")

class BinHeap:
    """docstring for BinHeap"""
    def __init__(self):
        self.heapList = [0]
        self.size = 1

    def insert(self, item):
        self.heapList.append(item)
        self.size += 1
        self.readjust(self.size)
    def readjust(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.heapList[i] < self.heapList[parent]:
                self.heapList[i], self.heapList[parent] = self.heapList[parent], self.heapList[i]
            i = i // 2

    def delMin(self):
        data = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.perDown(1)
        return data
    def perDown(self, i):
        while (i * 2) < self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.perDown(i)
            i -= 1
bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

```