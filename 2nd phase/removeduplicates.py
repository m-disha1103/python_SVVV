# WAP to remove all the duplicate elements from the given string
#  "Hello i love python" Now remove all the duplicate elements in the string Except white spaces in python.
# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch == " ":          # Keep all spaces
#         result += ch
#     elif result.count(ch) == 0:   # Check if character already exists
#         result += ch

# print("String after removing duplicates:", result)
# helo i v pytho

word = input("Enter a string: ")
result=" "
for ch in word:
    if ch not in result:
        result+=ch
print(result)        
