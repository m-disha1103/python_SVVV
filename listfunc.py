#04 may 2026
# list:
# >> A list is a collection of elements.
# >> It is ordered (items have positions/index).
# >> It is mutable (can be changed after creation).
# >> Written using square brackets [].
# >> Can store different data types.
# >> Allows duplicate values.
# >> Supports indexing and slicing.
# Commonly used because it is flexible.
#list functions
# lst=[10,20,30]
# l=list(lst)    #if we put l=lst output would be [15, 20, 30]
#                                     #           [15, 20, 30]
# l[0]=15
# print(l)
# print(lst)

# lst=list(input("enter a list: "))
# print(lst)
#output
# enter a list: today is monday
# ['t', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'm', 'o', 'n', 'd', 'a', 'y']

# lst=eval(input("enter a list: "))
# print(type(lst))
# output
# enter a list: [1,2,3,4]
# <class 'list'>

#append()  Add value in the end of list
# lst=[10,20,30]
# lst.append(40)
# print(lst)
#output
#[10,20,30,40]

#insert(i,value)  Add value on particular index mention (i,value)
# lst=[10,20,30]
# lst.insert(2,25)
# print(lst)

#extend() Add collection in list
# lst=[10,20,30]
# lst.extend([50,60,70])
# print(lst)

#pop()
# lst=[10,20,30]
# del.lst[0:2]
# print(lst)

#remove()
# lst=[10, 20, 30, 50, 60, 70]
# lst.remove(40)
# print(lst)

# clear()
# lst=[10, 20, 30, 50, 60, 70]
# lst.clear()
# print(lst)

#sort()
lst=[10,20,30,40,50,60]
lst.sort(reverse=True) #sort in reverse order  method
lst2=[5,2,0,9,3,1,4]
lst3=sorted(lst2) #sort in normal order  function
lst3=sorted(lst2, reverse=True) #sort in reverse order  function #output would be [9, 5, 4, 3, 2, 1, 0]
# print(lst2)
# print(lst3)
#output
# [5, 2, 0, 9, 3, 1, 4]
# [0, 1, 2, 3, 4, 5, 9]
lst4=[1,2,3,4,5]
print(lst4*2) #output would be [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] replication of list