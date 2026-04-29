# 29 april 2026
#WAP to implement a vending machine using functions in python.
def vending_machine():
    total = 0

    while True:
        print("\n1: Tray1(Snacks)")
        print("2: Tray2(Beverages)")
        print("3: Tray3(Chocolates)")

        tray = int(input("\nSelect a Tray(1/2/3/0): "))

        if tray == 0:
            break

        elif tray == 1:
            while True:
                print("Item1.Lays 25")
                print("Item2.Uncle Chips 10")
                print("Item3.Doritos 30")

                item = input("Choose a item(Item1/Item2/Item3): ")

                if item == "Item1":
                    total += 25
                elif item == "Item2":
                    total += 10
                elif item == "Item3":
                    total += 30
                else:
                    print("Invalid choice")

                stay = input("want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        elif tray == 2:
            while True:
                print("Item1.Coke 25")
                print("Item2.Pepsi 20")
                print("Item3.Sprite 30")

                item = input("Choose a item(Item1/Item2/Item3): ")

                if item == "Item1":
                    total += 25
                elif item == "Item2":
                    total += 20
                elif item == "Item3":
                    total += 30
                else:
                    print("Invalid choice")

                stay = input("want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        elif tray == 3:
            while True:
                print("Item1.KitKat 40")
                print("Item2.5Star 35")
                print("Item3.Snickers 30")

                item = input("Choose a item(Item1/Item2/Item3): ")

                if item == "Item1":
                    total += 40
                elif item == "Item2":
                    total += 35
                elif item == "Item3":
                    total += 30
                else:
                    print("Invalid choice")

                stay = input("want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        else:
            print("Invalid tray selection!")

    print("\nTotal :", total, "rupees")
    print("items dispatched")


# call function
vending_machine()
