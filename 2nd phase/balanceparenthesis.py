#25 june 2026
#stack balance parethesis (check that elements comes forst will appear last as well)
# s = "{[([{}])]}"
# stack = []
# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     elif ch == ')':
#         if len(stack) == 0 or stack.pop() != '(':
#             print("Not Balanced")
#             break
#     elif ch == '}':
#         if len(stack) == 0 or stack.pop() != '{':
#             print("Not Balanced")
#             break
#     elif ch == ']':
#         if len(stack) == 0 or stack.pop() != '[':
#             print("Not Balanced")
#             break
# else:
#     if len(stack) == 0:
#         print("Balanced")
#     else:
#         print("Not Balanced")
class stack:
    st=[]
    size=0
    top=-1
    def push(self,val):
        self.st.append(val)

    def pop(self):
        dict={}
        temp=[]
        while len(self.st)!=0:
            curr=self.st.pop()
            if curr in dict.keys():
                dict[curr]=dict[curr]+1
            else:
                dict[curr]=1   
            temp.append(curr)
        maxvalue=0  
        maxkey=0

        for key in dict.keys():
            if dict[key]>maxvalue:
                maxvalue=dict[key]
                maxkey=key

        while len(temp)!=0:
            ele=temp.pop()
            if ele!=maxkey:
                self.st.append(ele) 

    def display(self):
        for i in range(len(self.st)-1,-1,-1):
            print(self.st[i],end=" ")
s=stack()
s.push(5)
s.push(10)
s.push(15)
s.push(10)
s.push(20)
s.push(10)
s.push(20)
s.push(30)
s.push(10)
print("before pop operation:")
s.display()
print("\nafter pop operation:")
s.pop()
s.display()
s.pop()
print("\nafter pop operation:")
s.display()