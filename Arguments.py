#29 april 2026
# Arguments in python
# Arguments are the values that we pass to a function when we call it. They are used to provide input to the function, which can then process that input and return a result. There are different types of arguments in Python, including positional arguments, default arguments, keyword arguments, multiple arguments (*args), and multiple keyword arguments (**kwargs). Each type of argument serves a specific purpose and allows for flexibility in how functions are defined and called.
# positional Arguments
def profile(name,age):
    print("name:", name)
    print("age:", age)
    print(name, age)

profile("disha", 20)
#jis position pe argument pass karna hai, us position pe argument pass karna hai.

#default Arguments
def profile(name, age, alive="yes"):
    print("name:", name)
    print("age:", age)
    print("alive:", alive)
    print(name, age, alive)
profile("kunti", 110, "no")    
#isme default argument ka use nahi hua hai, kyunki alive ke liye argument pass kiya gaya hai.

#keyword Arguments
def profile(name,age):
    print("name:", name)
    print("age:", age)
    print(name, age)
profile(age=20, name="disha")  
#ye keyword argument ka use hai, kyunki arguments ko kisi bhi order me pass kiya ja sakta hai.

#multiple Arguments(*args)
def add(*num):
    sum=0
    for i in num:
        sum += i
    print(sum)
add(1, 2, 3, 4, 5)    
#ye multiple arguments ka use hai, kyunki hum kitne bhi arguments pass kar sakte hai, aur unka sum calculate kar sakte hai.

#multiple keyword Arguments(**kwargs)
def profile(**data):
    for i in data:
        print(data[i])
profile(name="Disha",age=24,phone=9425790331)    
#ye multiple keyword arguments ka use hai, kyunki hum kitne bhi keyword arguments pass kar sakte hai, aur unka value print kar sakte hai.
