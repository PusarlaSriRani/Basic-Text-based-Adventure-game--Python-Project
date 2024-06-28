import pytest
from project import Player, Item, Location, check_win_condition

def test_move():
    player = Player("Hero")
    forest = Location("Forest", "A dense forest with tall trees and chirping birds.")
    assert player.move(forest) == "Hero moves to Forest"

def test_pick_item():
    player = Player("Hero")
    sword = Item("Sword")
    forest = Location("Forest", "A dense forest with tall trees and chirping birds.", sword)
    player.move(forest)
    assert player.pick_item(sword) == "Hero picks up Sword"
    assert player.show_inventory() == "Hero's inventory: Sword"

def test_show_inventory():
    player = Player("Hero")
    assert player.show_inventory() == "Hero's inventory is empty"
    sword = Item("Sword")
    player.pick_item(sword)
    assert player.show_inventory() == "Hero's inventory: Sword"

def test_describe_location():
    forest = Location("Forest", "A dense forest with tall trees and chirping birds.")
    assert forest.describe() == "A dense forest with tall trees and chirping birds."

def test_check_win_condition():
    player = Player("Hero")
    sword = Item("Sword")
    shield = Item("Shield")
    potion = Item("Potion")
    required_items = [sword, shield, potion]
    player.pick_item(sword)
    player.pick_item(shield)
    assert not check_win_condition(player, required_items)
    player.pick_item(potion)
    assert check_win_condition(player, required_items)

if __name__ == "__main__":
    pytest.main()
