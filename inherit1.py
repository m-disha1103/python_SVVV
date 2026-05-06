# 06 may 2026
#concept of inheritence(oops)
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#here we are inheriting the properties of class animal to class bird
class bird(Animal, ABC):
    @abstractmethod
    def fly(self):
        pass

class pigeon(bird):
    def sound(self):
        print("Gutar Gu... Gutar Gu...")
    def fly(self):
        print("pigeon can fly")
p = pigeon()
p.sound()
p.fly()
#output:
#Gutar Gu... Gutar Gu...
#pigeon can fly