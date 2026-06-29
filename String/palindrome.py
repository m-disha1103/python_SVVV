#29 april 2026
# palindrome program
# def palindrome(s):
#     n=len(s)
#     #abcba indexing: 01234
#     #abccba indexing: 012345
#     for i in range(0,(n-1)//2+1): #to check only till middle of the string
#         if s[i]!=s[n-1-i]: #comparing first and last character, second and second last character and so on
#             print("Not a Palindrome..")
#             return
#     print("Palindrome")

def counfrequency(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
        return dict
        
s=input("Enter a string: ")
print(counfrequency(s))    
# print(palindrome(s))
