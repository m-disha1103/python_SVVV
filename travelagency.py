# 05 may 2026
# Question: 1
# Create a class TravelAgencies with below attributes:

# regNo – int
# agencyName – String
# pakageType – String
# price – int
# flightFacility – boolean

# Write getters, setters for the above attributes . Create constructor which takes parameter in the above sequence.

# Create class Solution with main method. Implement two static methods – findAgencyWithHighestPackagePrice and 
# agencyDetailsforGivenIdAndType in Solution class.

# findAgencyWithHighestPackagePrice method:

# This method will take array of TravelAgencies objects as an input parameter and return the highest package 
# price from the given array of objects.

# agencyDetailsForGivenldAndType method:

# This method will take three input parameters -array of TravelAgencies objects, int parameter regNo and String
# parameter packageType. The method will return the TravelAgencies object based on below conditions.

# FlightFacility should be available.
# The input parameters(regNo and packageType) should matched with the regNo and packageType of TravelAge.0ncies object.
# If any of the above conditions are not met, then the method should return null. Note : Same Travel agency can 
# have more than one package type. Travel agency and package type combination is unique. All the searches should 
# be case insensitive.

# The above mentioned static methods should be called from the main method.


# For findAgencyWithHighestPackagePrice method – The main method should print the highestPackagePrice as it is. 
# For agencyDetailsForGivenldAndType method -The main method should print the AgencyName and price of the returned 
# object.The AgencyName aT
# Input
# ---------
# 4

# 123
# A2Z Agency
# Platinum
# 50000
# true

# 345
# SSS Agency
# Gold
# 30000
# false

# 987
# Cox and Kings
# Diamond
# 40000
# true

# 888
# Global Tours
# Silver
# 20000
# false

# 987
# Diamond
# -------------------------------
# Output
# -------------------------------
# 50000
# Cox and Kings:40000

class TravelAgencies:
    __regno=0
    __agencyname=" "
    __packagetype=" "
    __price=0
    __flightfaculity=False

    def __init__(self,regno,agencyname,packagetype,price,flightfacility):
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
            max=solution.findAgencywithHighestPackagePrice(lst)
            agency=solution.agencyDetailsForGivenldAndType(lst,regno,packagetype)

            print(max)
            print(agency.get__agencyname(),":",agency.get__price())

            print()