# 24 june 2026
# staack previous greater element
lst=[5,7,1,2,10,9]  #input list
ans=[]
st=[]
for i in range(0,len(lst)):
    curr = lst[i]
    while len(st)!=0:
        if curr<st[-1]:
            ans.append(st[-1])
            st.append(curr)
            break
        st.pop()
    if len(st)==0:
        ans.append(-1)    
        st.append(curr)

print(ans)   
#output : [-1, -1, 7, 7, -1, 10]
