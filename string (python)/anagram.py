#29 april 2026
# anagram program
# def anagram(s1,s2):
#     dict1=counfrequency(s1)
#     dict2=counfrequency(s2)
#     if dict1==dict2:
#         print("Anagram")
#     else:
#         print("Not an Anagram")
# s1=input("Enter first string: ")
# s2=input("Enter second string: ")   
# palindrome(s1)
# palindrome(s2)          
def counfrequency(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
        return dict
   
# print(palindrome(s))
def anagram(s1,s2):
    dict1=counfrequency(s1) 
    dict2=counfrequency(s2)
    for i in dict1:
        if i in dict2 and dict1[i]==dict2[i]:
            return False
        else:
            dict2.pop(i, None)

    if len(dict2.keys())==0:
        return True
    else:
        return False

s1=input("Enter first string: ")
s2 =input("Enter second string: ")  
anagram(s1,s2)       
