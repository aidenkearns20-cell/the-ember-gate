ITEM_NAMES = {
    "potion": "Healing potion",
    "blade": "Iron blade",
    "ember": "Ember shard",
    "hide": "Wolf hide",
    "spore": "Glowcap spore",
    "core": "Gatekeeper core",
}


def count(items, key):
    return items.get(key, 0)


def add(items, key, quantity=1):
    items[key] = count(items, key) + quantity


def remove(items, key):
    if count(items, key) == 0:
        return False
    items[key] -= 1
    if items[key] == 0:
        del items[key]
    return True


def show(items):
    print("Inventory")
    for key, quantity in items.items():
        print(f"  {ITEM_NAMES[key]} × {quantity}")
    if not items:
        print("  Empty")


def drink_potion(player):
    if player.hp == player.max_hp:
        print("You already have full health.")
        return False
    if not remove(player.inventory, "potion"):
        print("You have no potions.")
        return False
    healed = min(18, player.max_hp - player.hp)
    player.hp += healed
    print(f"Potion restored {healed} HP.")
    return True
