# 05 may 2026
# question 1
# create a class TravelAgencies with below attributes:
# regno - int
# agencyName - string
# pakageType - string
# price - 

class TravelAgencies:
    __regno=0
    __agencyname=" "
    __packagetype=" "
    __price=0
    __flightfaculity=False

    def __init__(self,regno,agencyname,packagename,price,flightfacility):
        self.__regno =regno
        self.__agencyname=agencyname
        self.__packagetype=packagetype
        self.__price=price
        self.__flightfaculity=flightfacility

    def getregno(self):
        return self.__regno
    def setregno(self,regno):
        self.__regno=regno   
    def getagencyname(self):
        return self.__agencyname
    def setagencyname(self,agencyname):
        self.__agencyname=agencyname   
    def getpackagetype(self):
        return self.__packagetype
    def setpackagetype(self,packagetype):
        self.__packagetype=packagetype     
    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price=price
    def getflightfacility(self):
        return self.__flightfaculity
    def setflightfacility(self,flightfacility):
        self.__flightfaculity=flightfacility  

class solution:
    @staticmethod
    def findAgencywithHighestPackagePrice(self,lst):
        max=0
        for agency in lst:
            if agency.getprice()>max:
                max= agency.getprice

        return max 
    @staticmethod
    def agencyDetailsForGivenldAndType(self,lst,regno,packagetype):
        for agency in lst:
            if agency.getflightfscility() and agency.getregno()==regno and agency.getpackagetype()==packagetype:
                return agency
        return None    
    
    if __name__=="__main__":
        n=int(input())
        lst=[]
        for i in range(n):
            regno= int(input())
            agencyname=input()
            packagetype=input()
            price=int(input())
            flightfacility=bool(input())

            agency=TravelAgencies(regno,agencyname,packagetype,price,flightfacility)
            lst.append(agency)

            regno=int(input())
            packagetype=input()
            print("--------------------------\noutput\n---------------------------------")
            max=Solution.findAgencywithHighestPackagePrice(lst)
            agency=Solution.agencyDetailsForGivenldAndType(lst,regno,packagetype)

            print(max)
            print(agency.get__agencyname(),":",agency.get__price())

            print()