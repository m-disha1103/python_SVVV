#cognizant
#duplicate Entry Check
#scenario:A sensor records values, but some readings are corrupted and stored as 0. Move all
# corrupted readings to the end while maintaining the order of valid readings
lst=eval(input("enter a list: "))
duplicate=[]
unique=False
for ele in lst:
    if ele not in duplicate:
        duplicate.append(ele)
    else:
        unique=True
        break
if unique:
    print("True")
else:    
    print("False")

#input given :enter a list: [1,2,3,1]
#output: True

