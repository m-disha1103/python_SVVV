#28 april 2026
#homeWork
#Smart Elevator System
current_floor = int(input("Enter current floor: "))
n = int(input("Enter number of requests: "))

requests = []

for _ in range(n):
    floor = int(input("Enter requested floor: "))
    direction = input("Enter direction (up/down): ").lower()
    requests.append((floor, direction))

# Assume current direction based on first request
direction = requests[0][1]

same_dir = []
opp_dir = []

# Separate requests
for floor, dirn in requests:
    if dirn == direction:
        same_dir.append(floor)
    else:
        opp_dir.append(floor)

# Sort based on direction
if direction == "up":
    same_dir.sort()
    opp_dir.sort(reverse=True)
else:
    same_dir.sort(reverse=True)
    opp_dir.sort()

# Final order
order = same_dir + opp_dir

print("Service Order:", order)
