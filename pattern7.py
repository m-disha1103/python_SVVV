#28 april 2026
#pattern 7
#   A
# C B D
#   E
# G F H
#   I
n=5
n = 5
ch = ord('A')

for i in range(1, n+1):
    if i % 2 != 0:
        print("   "*(n-2), end="")   
    else:
        print(""*(n-3), end="")      
    if i % 2 != 0:
        print(chr(ch))
        ch += 1
    else:
        print(chr(ch+1), chr(ch), chr(ch+2))
        ch += 3
    print()    