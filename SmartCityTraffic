# 06 may 2026
#Smart City Traffic Analyzer
#scenario:
# you are working as a java developer in a smart city project.
#cameras record the number of cars passing through a toll game every minute.
#you're given an array where each element represents the number of cars in that minute.
#problem :
# find the maximum number of cars that passed through the toll gate in any k consecutive minutes.
lst=eval(input())
k=int(input())
sum,max = 0,0
for ele in range(k):
    sum+=lst[ele]
if max<sum:
    max=sum
for i in range(k,len(lst)):
    sum-=lst[i-k]
    sum+=lst[i]
    if max<sum:
        max=sum
print(max)