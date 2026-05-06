# 06 may 2026
#Create a class Institution with below attributes:
# institutionId - int 
# institutionName-String 
# noofstudentsplaced -int 
# noofstudentscleared-int 
# location - String 
# grade - string

# Write getters, setters for the above attributes.
# Create constructor which takes parameter in the above sequence except grade.
# Create class Solution with main method.
# Implement two static methods - FindNumclearancedByLoc and UpdateInstitutionGrade in Solution class.
# FindNumClearancedByLoc method:
# This method will take two input parameters -array of Institution objects and string parameter location.
# The method will return the sum of the noofstudentscleared attribute from institution objects for the location passed as parameter. If no institution with the given location is present in the array of institution objects, then the method should return 0.
# UpdateInstitutionGrade method:
# This method will take a string parameter institutionName, along with the array of Institution objects.
# The method will return the institution object, if the input string parameter matches with the institutionName attribute of the institution object. Before returning the object, the grade should be arrived based on the rating calculation mentioned below.
# This grade value should be assigned to the object. If any of the above conditions are not met, then the method should return null.
# The grade attribute should be calculated as follows:
# Rating= (noofstudentsplaced * 100)/noofstudentscleared
# If the rating greater than equal to 80, then grade should be A'.
# Else, then grade should be 'B'
# *Note:*
# No institution object would have the same value for institutionName attribute.
# All institution object would have the noofstudentsPlaced value lesser than noofstudentscleared value.
# All the searches should be case insensitive.
# The above mentioned static methods should be called from the main method.
# The above mentioned static methods should be called from the main method.
# Eer Finduce a ty print There are od are prints he tois parant ete
# if the returned value is
# For UpdateInstitutiongrade method - The main method should print the institutionName and grade of the returned Instituti object. The instituationhame and grade should be concatinated with :: while printing. eg:- TCS:A, where TCS is ti institution name and A is the grade
# If the returned value is nullthen it should print "No Institute is available with the specified name".
# Before calling these static methods in main, use scanner object to read the values of four Phone objects referring attribute: in the above mentioned attribute sequence (except grade attribute). Next, read the value for location and institutionName.

# All the searches should be case insensitive.
# The above mentioned static methods should be called from the main method.
# For FindNumclearancedByLoc method - The main method should print the noofclearance as it is, if the returned value is greater than o, or it should print "There are no cleared students in this particular location".
# For UpdateInstitutionGrade method - The main method should print the institutioname and grade of the returned Institution object. The instituationName and grade should be concatinated with :: while printing. eg: - TCS::A, where TCS is the institution name and A is the grade.
# If the returned value is nullthen it should print "No Institute is available with the specified name".
# Before calling these static methods in main, use Scanner object to read the values of four Phone objects referring attributes in the above mentioned attribute sequence (except grade attribute). Next, read the value for location and institutionName.
class Institution:
    def __init__(self, institutionId, institutionName, noofstudentsplaced, noofstudentscleared, location):
        self.institutionId = institutionId
        self.institutionName = institutionName
        self.noofstudentsplaced = noofstudentsplaced
        self.noofstudentscleared = noofstudentscleared
        self.location = location
        self.grade = None
# Getters and Setters for institutionId, institutionName, noofstudentsplaced, noofstudentscleared, location, grade
    def get_institutionId(self):
        return self.institutionId

    def set_institutionId(self, institutionId):
        self.institutionId = institutionId

    def get_institutionName(self):
        return self.institutionName

    def set_institutionName(self, institutionName):
        self.institutionName = institutionName

    def get_noofstudentsplaced(self):
        return self.noofstudentsplaced

    def set_noofstudentsplaced(self, noofstudentsplaced):
        self.noofstudentsplaced = noofstudentsplaced

    def get_noofstudentscleared(self):
        return self.noofstudentscleared

    def set_noofstudentscleared(self, noofstudentscleared):
        self.noofstudentscleared = noofstudentscleared

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

# child class or subclass for Institution class 
class Solution:
    @staticmethod
    def FindNumclearancedByLoc(institutions, location):
        total_cleared = 0
        for institution in institutions:
            if institution.get_location().lower() == location.lower():
                total_cleared += institution.get_noofstudentscleared()
        return total_cleared

    @staticmethod
    def UpdateInstitutionGrade(institutionName, institutions):
        for institution in institutions:
            if institution.get_institutionName().lower() == institutionName.lower():
                rating = (institution.get_noofstudentsplaced() * 100) / institution.get_noofstudentscleared()
                if rating >= 80:
                    institution.set_grade('A')
                else:
                    institution.set_grade('B')
                return institution
        return None
if __name__ == "__main__":  
    institutions = []
    for _ in range(4):
        institutionId = int(input("Enter institution ID: "))
        institutionName = input("Enter institution name: ")
        noofstudentsplaced = int(input("Enter number of students placed: "))
        noofstudentscleared = int(input("Enter number of students cleared: "))
        location = input("Enter location: ")
        institutions.append(Institution(institutionId, institutionName, noofstudentsplaced, noofstudentscleared, location))

    location_input = input("Enter location to find number of cleared students: ")
    cleared_students = Solution.FindNumclearancedByLoc(institutions, location_input)
    if cleared_students > 0:
        print(cleared_students)
    else:
        print("There are no cleared students in this particular location")

    institutionName_input = input("Enter institution name to update grade: ")
    updated_institution = Solution.UpdateInstitutionGrade(institutionName_input, institutions)
    if updated_institution is not None:
        print(f"{updated_institution.get_institutionName()}::{updated_institution.get_grade()}")
    else:
        print("No Institute is available with the specified name")
