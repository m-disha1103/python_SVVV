#05 may 2026
# Question:
# Create a class Phone with below attributes:
# phoneId - int
# os - String
# brand - String
# price - int
# Write getters, setters and parameterized constructor in the above mentioned attribute sequence as required.
# Create class Solution with main method.
# Implement two static methods - findPriceForGivenBrand and getPhoneIdBasedOnOs in Solution class.
# findPriceForGivenBrand method:
# 1111
# This method will take two input parameters - array of Phone objects and string
# parameter brand. The method will return the sum of the price attribute from phone
# objects for the brand passed
# as parameter. If no phones with the given brand is present in the array of phone
# objects, then the method should return 0.
# getPhoneIdBasedonOs method:
# 1111111111lllll111111111111111111」
# This method will take a String parameter os, along with the array of Phone objects.The method will return the phone object, if the input String parameter matches with the os attribute of the phone
# object and its price attribute is greater than or equal to 50000. If any of the
# conditions are not met, then the method should return null.
# Note :No phone object would have the same value for os attribute. All phone object
#For findPriceForGivenBrand method - The main method should print the price as it is
# if the returned price is greater
# than 0, or it should print "The given Brand is not available".
# For getPhoneIdBasedOnOs method - The main method should print the phoneId of the
# returned phone object. If the returned
# value is null then it should print "No phones are available with specified os and price range".
# Before calling these static methods in main, use Scanner object to read the values of
# four Phone objects referring
# attributes in the above mentioned attribute sequence. Next, read the value for brand and os.
# 111
# i0S
# Apple
# 30000
# 222
# android
# Samsung
# 50000
# 333
# Symbian
# HTC
# 12000
# 444
# Paranoid
# HTC
# 89000
# Blackberry
# aNdRoid
# Output
# The given Brand is not available
# 222
class Phone:
    __phoneId=0
    __os=" "
    __brand=" "
    __price=0

    def __init__(self,phoneId,os,brand,price):
        self.__phoneId=phoneId
        self.__os=os
        self.__brand=brand
        self.__price=price

    def getphoneId(self):
        return self.__phoneId
    def setphoneId(self,phoneId):
        self.__phoneId=phoneId   
    def getos(self):
        return self.__os
    def setos(self,os):
        self.__os=os
    def getbrand(self):
        return self.__brand
    def setbrand(self,brand):
        self.__brand=brand    
    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price=price

class Solution:

    @staticmethod
    def findPriceForGivenBrand(lst, brand):
        total = 0
        for phone in lst:
            if phone.getbrand().lower() == brand.lower():
                total += phone.getprice()
        return total


    @staticmethod
    def getPhoneIdBasedOnOs(lst, os):
        for phone in lst:
            if phone.getos().lower() == os.lower() and phone.getprice() >= 50000:
                return phone
        return None
    
if __name__=="__main__":
        n=int(input())
        lst=[]
        for i in range(n):
            phoneId= int(input())
            os=input()
            brand=input()
            price=int(input())

            phone_obj=Phone(phoneId,os,brand,price)
            lst.append(phone_obj)

            brand_input=input()
            os_input=input()
            print("--------------------------\noutput\n---------------------------------")
            total=Solution.findPriceForGivenBrand(lst, brand_input)
            phone_result=Solution.getPhoneIdBasedOnOs(lst, os_input)

            print(total)
            if phone_result:
                print(phone_result.getbrand(),":",phone_result.getprice())
            else:
                print("No phone found")

            print()
