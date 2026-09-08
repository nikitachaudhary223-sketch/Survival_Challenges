import random

print("==============================")
print("Welcome to python survival game")
print("==============================")

name=input("Enter your name:")
age=int(input("Enter your age:"))

health=100
energy=100
food=5
coins=100
score=0
day=1

print("================================")
print("                  Player Created")
print("================================")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Health: {health}")
print(f"Energy: {energy}")
print(f"Food: {food}")
print(f"Coins: {coins}")
print(f"Score: {score}")
print(f"Day: {day}")

while True:
    print("============================")
    print("               Survival Menu")
    print("============================")
    print("1.Explore")
    print("2.Hunt for food")
    print("3.Rest")
    print("4.Visit shop")
    print("5.Inventory")
    print("6.Player Status")
    print("7.End day")
    print("8.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        print("You decided to explore")
        event=random.randint(1,4)

        if event==1:
            print("you found coins")
            coins_found=random.randint(10,100)
            coins=coins+coins_found

        elif event==2:
            print("You found food")
            food_found=random.randint(1,5)
            food=food+food_found
        
        elif event==3:
            print("A wolf attacked you")
            damage=random.randint(10,30)
            health=health-damage
            print(f"The wolf dealt {damage} damage!")
            print(f"Your health is now {health}")
        else:
            print("Nothing happened")

    elif choice==2:
        print("======================")
        print("               HUNTING")
        print("======================")
        print("1.Safe Hunt")
        print("2.Risky Hunt")
        print("3.Cancel")

        hunt_choice=int(input("Choose: "))
        if hunt_choice==1:
                food_found=random.randint(1,3)
                food=food+food_found
                energy=energy-10
                print(f"You found {food} food!")
                print(f"Energy is now {energy}")

        elif hunt_choice==2:
            energy=energy-20
            print(f"Energy is now {energy}")
            hunt_event=random.randint(1,2)
            if hunt_event==1:
                food_found=random.randint(3,7)
                food=food+food_found
                print(f"We found {food}food.")
            else:
                damage=random.randint(10,30)
                health=health-damage
                print(f"Th damage is: {damage}")
                print(f"Reamaning health now: {health}")

        elif hunt_choice==3:
            print(f"You cancelled the hunt.")

        else:
            print("Invalid hunting choice.")

    elif choice==3:
        print("You decided to rest")
        before_rest=energy
        restore_energy=random.randint(10,90)
        energy=energy+restore_energy
        if energy>100:
            energy=100

        print(f"Before rest: {before_rest}")
        print(f"Energy restored: {restore_energy}")
        print(f"Energy after rest: {energy}")

    elif choice==4:
        print("You entered the shop")
        print("====================")
        print("                SHOP")
        print("====================")
        print("1.Buy Food")
        print("2.Exit Shop")

        shop_choice=int(input("Choose:"))

    elif choice==5:
        print("You checked your inventory")

    elif choice==6:
        print("You checked your status")

    elif choice==7:
        print("The day has ended")

    elif choice==8:
        print("Thanks for playing")
        break

    else:
        print("Invalid option")

    