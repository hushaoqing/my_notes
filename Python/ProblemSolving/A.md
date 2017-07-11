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


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
```
```
# AVL:
class AVLTree(BinarySearchTree):
    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                    rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
    def rebalance(self,node):
      if node.balanceFactor < 0:
             if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
             else:
                self.rotateLeft(node)
      elif node.balanceFactor > 0:
             if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
             else:
                self.rotateRight(node)
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                    self._put(key,val,currentNode.leftChild)
            else:
                    currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                    self._put(key,val,currentNode.rightChild)
            else:
                    currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.rightChild)
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                    node.parent.balanceFactor += 1
            elif node.isRightChild():
                    node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)
```
## Chapter 7 Graph
```
class Vertex(object):
    """docstring for Vertex"""
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def __contains__(self, n):
        return n in self.vertList
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex
    def getVertex(self, n):
        return self.vertList[n] if n in self.vertList else None
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight=cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
```