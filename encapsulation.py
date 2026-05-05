# 05 may 2026
# understanding oops concepts
# understanding encapsulation
class Bank:
    __accno=0
    __name=" "
    __balance= 0 # private variable(underscore lagake banate h)

    def __init__(self,accno,name,balance):  #constructor it uses to initialize the object
        self.__accno=accno
        self.__name=name
        self.__balance=balance

    #getter and setter used to access private variable
    #accno
    def getaccno(self):
        return self.__accno
    def setteraccno(self,accno):
        self.__accno=accno

    #name     
    def getname(self):
        return self.__name
    def settername(self,name):
        self.__name=name

    #balance
    def getbalance(self):
        return self.__balance
    def setterbalance(self,balance):
        self.__balance=balance
 
b=Bank(12345,"disha",10000)
# print(b.getaccno()) #output: 12345
# b.setteraccno(599800)
# print(b.getaccno()) #output: 599800
# print(b.getname()) #output: disha
# b.settername("Disha Malviya")
# print(b.getname()) #output: Disha Malviya
# print(b.getbalance()) #output: 10000

# print(b.__accno)
print(b._Bank__accno) #output: 12345