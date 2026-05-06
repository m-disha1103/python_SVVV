# 06 may 2026
#concept of method overriding in python
#Method overriding is a feature in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its superclass.
# When a method in a subclass has the same name, same parameters or signature, and same return type (or sub-type) as a method in its superclass, then the method in the subclass is said to override the method in the superclass.
# The version of a method that is executed will be determined by the type of the object that is used to call the method, not the type of the reference variable. This is known as dynamic method dispatch.
from tracemalloc import start


class A:
    def start(self):
        print("start method from class A")
class B(A):
    def start(self):
        super().start() # calling the start method of class A
        print("start method from class B")
if __name__ == "__main__":
    b = B()
    b.start() 

#output:
    #start method from class A
    #start method from class B