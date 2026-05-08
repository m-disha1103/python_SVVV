#TCS ninja
#Missing Roll Number
#A college assigns roll numbers from 0 to n for students. Due to an error, one roll
#number is missing in the database. Identify the missing roll number
num=eval(input("enter numbers: "))
n=len(num)  #for length of number list

total_sum=n*(n+1)//2
arr_sum=sum(num)
missing_num= total_sum - arr_sum
print("missing number is: ",missing_num)