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