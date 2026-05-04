#tuple
# >> A tuple is a collection of elements (like a list).
# >> It is ordered (items have a fixed position).
# >> It is immutable (cannot be changed after creation).
# >> Written using parentheses ().
# >> Can store different data types (int, string, float, etc.).
# >> Allows duplicate values.
# >> Faster than lists for fixed data.

tpl=(10,20,30)
# t1=tpl
# tpl=1 #because of this output will be datatype (10, 20, 30)
# # <class 'int'>
# print(t1)
# print(type(tpl))

# tpl=tuple(input())
# print(type(tpl))
# print(tpl)
#output
# <class 'tuple'>
# ('1',)

tpl=(1,2,3)

#tuple don't have those function which modify the data like append(), insert(), extend(), pop(), remove(), clear() etc. because tuple is immutable.
#it have only two functions count() and index() which are used to count the number of occurrences of a value and to find the index of a value respectively.

#count() method is used to count the number of occurrences of a value in a tuple. It takes one argument, which is the value to be counted, and returns the count as an integer.
# t = (1, 2, 2, 3)
# print(t.count(2))  # Output: 2

#index() method is used to find the index of the first occurrence of a value in a tuple. It takes one argument, which is the value to be searched for, and returns the index as an integer. If the value is not found, it raises a ValueError.
t = (1, 2, 3)
print(t.index(2))  # Output: 1

# Built-in functions that work with tuples:
# len() → Returns number of elements
# max() → Returns largest value
# min() → Returns smallest value
# sum() → Returns sum of elements (numeric only)
