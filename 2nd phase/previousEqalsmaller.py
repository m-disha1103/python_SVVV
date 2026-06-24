#24 june 2026
#stack previous equal or smaller element
#[100,80,60,70,60,75,85] input
#[1,1,1,2,2,4,6] output
lst=[100,80,60,70,60,75,85]
ans=[]
st=[]
count=0
for i in range(0,len(lst)):
    curr = lst[i]
    while len(st)!=0:
        if curr>=st[0]:
            ans.append(st[-1])
            st.append(curr)
            break
        st.pop()
    if len(st)==0:
        ans.append(-1)    
        st.append(curr)

print(ans)