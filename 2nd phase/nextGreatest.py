#24 june 2026
#stack questions
lst=[5,7,1,2,10,9]  #input list
ans=[]
st=[]
for i in range(len(lst)-1, -1, -1):
    while (len(st)!=0):
        curr = lst[i]
        if curr<st[-1]:
            ans.append(st[-1])
            st.append(curr)
            break
        st.pop()
    if len(st)==0:
        ans.append(-1)    
        st.append(lst[i])
lst.reverse()
print(ans)    
#output : [-1, -1, 10, 2, 10, 7]