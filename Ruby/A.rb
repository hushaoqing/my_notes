class Greet
    def initialize(text)
        @text = text
    end
    def welcome
        @text
    end
end

# my_object = Greet.new("Hello")
# p my_object.class
# p my_object.class.instance_methods(false)
# p my_object.instance_variables
# p -1.abs
# p Greet.methods
# p String.methods == "abc".methods
# p String.instance_methods == "abc".methods
class MyClass;end
obj1= MyClass.new
obj2= MyClass.new
p obj1.class
p MyClass.class
p Class.class
p Module.class
p Object.class
p Class.superclass
p Module.superclass
p Object.superclass
p BasicObject.class
p BasicObject.superclass
# ==> MyClass
# ==> Class
# ==> Class
# ==> Class
# ==> Class
# ==> Module
# ==> Object
# ==> BasicObject
# ==> Class
# ==> nil
p MyClass.ancestors
# ==> [MyClass, Object, Kernel, BasicObject]