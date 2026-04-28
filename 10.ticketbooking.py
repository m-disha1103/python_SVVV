#28 april 2026
#Train Ticket Booking
avail=0
seats=int(input("seats Required: "))
vip = input("enter VIP status(yes/no): ")

if vip=="yes" or seats<=avail:
    print("ticket Confirmed!")
else:
    print("Waiting List")    