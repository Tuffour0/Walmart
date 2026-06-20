

def start_game():
    name = input("Welcome to the Adventure Game! What is your name, traveler? ")
    print(f"\nHello, {name}! You start your grand adventure and stand at a crossroad.")
    print("To your left you see a dark forest. To your right, a mysterious cave beckons.\n")

    while True:
        print("What do you want to do?")
        print("1. Enter the cave")
        print("2. Enter the dark forest")
        choice = input("> ")

        if choice == "1":
            cave_path()
            break
        elif choice == "2":
            forest_path()
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")


def forest_path():
    print("\nYou walk down the forest path and see a flowing river and a large tree.")

    while True:
        print("Do you want to{name}:")
        print("1. Follow the river")
        print("2. Climb the tree")
        choice = input("> ")

        if choice == "1":
            print("\nYou follow the river and find a hidden waterfall.")
            print("Do you want to:")
            print("1. Go behind the waterfall")
            print("2. Get into the river")
            choice = input("> ")
            break
        elif choice == "2":
            print("\nYou climb the tree and try to reach the highest branch.")
            print("Oh No!You fall off the great tree")
            print("You Died!Game Over!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")


def cave_path():
    print("\nYou step inside the dark cave. You can barely see anything.")

    while True:
        print("Do you want to do:")
        print("1. Light a torch")
        print("2. Proceed in the dark")
        choice = input("> ")

        if choice == "1":
            print("\nYou light a torch and the cave illuminates!")
            print("You spot a treasure chest glimmering in the corner.")
            print("You open it and find precious gems inside!")
            print("Congratulations, you win!\n")
            break
        elif choice == "2":
            print("\nYou stumble through the darkness...")
            print("Oh No!You fall into a pit and died.")
            print("You Died!Game Over!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")


def main():
    while True:
        start_game()
        print("Would you like to play again?")
        print("1. Yes")
        print("2. No")
        replay = input("> ")

        if replay != "1":
            print("\nThanks for playing! Goodbye.")
            break
        print("\n--- Restarting the adventure ---\n")

if __name__ == "__main__":
    main()

