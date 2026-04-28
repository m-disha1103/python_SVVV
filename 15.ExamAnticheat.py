#28 april 2026
#homeWork
#online exam anti-cheat system
tab_switch = int(input("Enter number of tab switches: "))
idle_time = int(input("Enter idle time (in minutes): "))

if tab_switch > 3 or idle_time > 5:
    print("Cheating Suspected")
else:
    print("No Cheating Detected")