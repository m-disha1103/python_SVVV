#29 april 2026
# Variations of functions
def greet():
    print("namashkar, kaisan baa?!")

greet()
#variation :
#  No return no argument
#  No return with argument
#  Return with no argument
# with return with argument
def greeting(name):
    print(name, "Sb nimmun baa?!",sep="@")
greeting("disha")    

def greetings():
    return "ha nimmum batien?!"
name = greetings()
print(name)

def greets(name):
    print("hello everyone"+name)
name = greets("disha")
print(name)    