#infosys
#Shift Corrupted Data
#A sensor records values, but some readings are corrupted and stored as 0. Move all
#corrupted readings to the end while maintaining the order of valid readings.
lst=eval(input())
result=[]

for ele in lst: # iterate through the list and check if the element is not 0, if it is not 0 then append it to the result list
    if ele!=0: 
        result.append(ele)
for ele in lst:
    if ele==0:
        result.append(ele)
print(result)