# 06 may 2026
#concept of inheritence(oops)
from abc import ABC, abstractmethod
#parent class
class Animal(ABC):
    def sound(self):
        print("Gutar Gu... Gutar Gu... from Animal")
#here we are inheriting the properties of class animal to class bird
#child class or subclass
class bird(ABC): 
    #@abstractmethod
    @abstractmethod
    def sound(self):
        print("koo.. koo.. from bird")
    def fly(self):
        pass

#derived class 
class pigeon(Animal, bird): #multiple inheritence
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