# 04 may 2026
#a teacher marks but entries are invalid  remove them ane return valid marks   note: invalid means -1
#45 67 -1 89 -1 76  input
#45 67 89 76 output
marks = input("Enter marks: ").split()

valid_marks = []

for i in marks:
    num = int(i)
    if num != -1:
        valid_marks.append(num)

print(";Valid marks:", valid_marks)

#sir wala code
# lst = eval(input("Enter list of prices: "))
# Remove 3 items (0s in this case)  
# ele=int(input("entern no."))

# for i in range(len(lst)-1,0,-1):
#     if lst[i]==ele:
#         lst.pop(i)

# print("List after removing items:", lst)