#24 june 2026
#stock span problem
#stack previous equal or smaller element
#[100,80,60,70,60,75,85] input
#[1,1,1,2,2,4,6] output
lst=[100,80,60,70,60,75,85]
res=[]
st=[]
for i in range(0,len(lst)):
    curr = lst[i]
    temp=[]
    count=1
    while len(st)!=0:
        if curr>=st[-1]:
            count+=1
            temp.append(st.pop())
        else:
            break
    res.append(count)
    st.append(curr)
    temp.reverse()
    st.extend(temp)       


print(res)   