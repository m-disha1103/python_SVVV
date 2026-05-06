# 06 may 2026
# find the longest sub array/sub string with atmost k distinct character example str"eceba",k=2
str= input()
k=int(input())
left=0
max_length=0
char_count={}
for right in range(len(str)):
    char= str[right]
    char_count[char]=char_count.get(char,0)+1
    while len(char_count)>k:
        left_char=str[left]
        char_count[left_char]-=1
        if char_count[left_char]==0:
            del char_count[left_char]
        left+=1
    max_length=max(max_length,right-left+1)
print(max_length)
#output: 3 means "ece" is the longest substring with atmost 2 distinct characters.