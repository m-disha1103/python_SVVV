# 05 may 2026
#abstraction concept
class Meal:
    def __cookbutterPaneer(self):
        print("Butter Paneer Prepared")
    def __cookLachaParatha(self):
        print("Lacha Paratha Prepared") 
    def __cookpyaaz(self):
        print("pyaaz prepared")
    def __cookkitkatShake(self):
        print("kitkat shake Prepared")    

    def cookMeal(self):
        Meal.__cookbutterPaneer(self)
        Meal.__cookLachaParatha(self)
        Meal.__cookpyaaz(self)
        Meal.__cookkitkatShake(self)

if __name__=="__main__":
    m=Meal()
    m.cookMeal()
       
