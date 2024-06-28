class Player:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.inventory = []

    def move(self, location):
        self.location = location
        return f"{self.name} moves to {location.name}"

    def pick_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            return f"{self.name} picks up {item.name}"
        else:
            return f"{self.name} already has {item.name}"

    def show_inventory(self):
        if self.inventory:
            return f"{self.name}'s inventory: " + ", ".join(item.name for item in self.inventory)
        else:
            return f"{self.name}'s inventory is empty"

class Item:
    def __init__(self, name):
        self.name = name

class Location:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item

    def describe(self):
        return self.description

def check_win_condition(player, required_items):
    for item in required_items:
        if item not in player.inventory:
            return False
    return True

def main():
    player = Player("Hero")
    
    # Define locations and items
    forest = Location("Forest", "A dense forest with tall trees and chirping birds.", Item("Sword"))
    cave = Location("Cave", "A dark and damp cave.", Item("Shield"))
    village = Location("Village", "A small village with friendly inhabitants.", Item("Potion"))
    
    locations = [forest, cave, village]
    required_items = [forest.item, cave.item, village.item]

    print("Welcome to the Adventure Game!")
    print("Type 'quit' to exit the game.")
    print("Commands: move [location], interact [item], inventory, look")
    print("Goal: Collect all items to win the game.")

    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command.startswith("move"):
            parts = command.split(" ", 1)
            if len(parts) == 2:
                destination = parts[1]
                for location in locations:
                    if location.name.lower() == destination:
                        print(player.move(location))
                        break
                else:
                    print("Unknown location")
        elif command.startswith("interact"):
            parts = command.split(" ", 1)
            if len(parts) == 2 and player.location:
                if player.location.item and player.location.item.name.lower() == parts[1]:
                    print(player.pick_item(player.location.item))
                else:
                    print("No such item here")
            else:
                print("Usage: interact [item]")
        elif command == "inventory":
            print(player.show_inventory())
        elif command == "look":
            if player.location:
                print(player.location.describe())
                if player.location.item:
                    print(f"You see a {player.location.item.name} here.")
            else:
                print("You are nowhere")
        elif command == "check win":
            if check_win_condition(player, required_items):
                print("Congratulations! You have collected all items and won the game!")
                break
            else:
                print("You have not collected all items yet.")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
