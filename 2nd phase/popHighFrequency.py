#24 june 2026
#stack questions
# Design a stack where pop removes the element with the highest frequency
stack = []
freq = {}
for x in stack:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Frequency:", freq)
max_freq = max(freq.values())
for i in range(len(stack)-1, -1, -1):
    if freq[stack[i]] == max_freq:
        popped = stack.pop(i)
        break

print("Popped:", popped)
print("Stack after pop:", stack)