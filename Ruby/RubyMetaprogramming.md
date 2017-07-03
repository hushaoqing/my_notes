## Ruby metaprogramming

### Chapter 1 The Object Model
1. Open Class
2. Monkeypatch
3. String.instance_methods == "abc".methods # ==> True 一个对象的实例对象存在于对象本身，而一个对象的方法存在于对象自身的类，因此同一个类的对象共享方法，不共享实例变量。

### Chapter 2 Methods
4. Dynamic Dispatch
5. method_missing(), respond_to?(), const_missing(); Module{undef_method(), remove_method()}: Dynamic Proxies

### Chapter 3 Blocks
6. Blocks: block_given?()
7. Closures: Class, Module, def; Class.new(), Module.define_method()
8. Proc Objects
9. DSL
10. instance_eval(), class_eval()

### Chapter 4 Class Definitions
11. self, @, @@
12. Singleton Methods
13. Class Macros
14. eigenclass

### Chapter 5 Code That Writes Code
### Chapter 6 Epilogue
