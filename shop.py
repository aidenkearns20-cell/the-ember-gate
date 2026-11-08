from inventory import ITEM_NAMES, add, count
from ui import choose

STOCK = {"1": ("potion", 5), "2": ("blade", 15)}


def visit(player):
    while True:
        print(f"Your gold: {player.gold}")
        for option, (item, price) in STOCK.items():
            print(f"{option}. {ITEM_NAMES[item]} — {price} gold")
        answer = choose("Item number or 0 to leave: ", ("0", *STOCK))
        if answer == "0":
            return
        item, price = STOCK[answer]
        if item == "blade" and count(player.inventory, item):
            print("You already own an iron blade.")
        elif player.gold < price:
            print("You don't have enough gold.")
        else:
            player.gold -= price
            add(player.inventory, item)
            print(f"Bought {ITEM_NAMES[item]}.")
