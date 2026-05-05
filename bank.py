# 05 may 2026
# understanding oops concepts
# understanding class
class Bank:
    accno=0
    name=" "

    def __init__(self,accno,name):  #constructor
        self.accno=accno
        self.name=name

    def show(self):
        print("Account Number:", self.accno)
        print("Name:", self.name)
    

#b=Bank()
b=Bank(599800,"Disha Malviya")  #output : Account Number: 599800    
                             #            Name: Disha Malviya
b2=Bank(599801,"Rohit Sharma")  #output : Account Number: 599801                             
#print(b.name)      # output:Disha Malviya  
b.show()           # output:Account Number: 599800
                   #         Name: Disha Malviya
b2.show()          # output:Account Number: 599801
                   #         Name: Rohit Sharma
