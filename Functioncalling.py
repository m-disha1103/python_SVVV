#29 april 2026
# Function calling

#call by value (immuatable data types)
#def update(value):
#    value="hi"
#    print(value)
#v="hello"
#update(v)
#print(v)
    
#arguments are passed by value, not by reference. So the value of v is not changed outside the function.
#found in function calling and variations of functions.
#parameters are local to the function, so they cannot be accessed outside the function.
# found the function signature

#call by reference (mutable data types)
def update(lst):
    lst[0]=21
lst=[1,2,3]
update(lst)
print(lst)    

