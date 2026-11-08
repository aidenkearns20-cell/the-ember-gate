from colorama import Fore

from inventory import ITEM_NAMES, add, drink_potion
from skill import SKILLS
from ui import choose, color


def battle(player, monster):
    print(color(f"A {monster.name} approaches!", Fore.RED))
    cooldowns = {}
    turn = 0
    while player.hp > 0 and monster.hp > 0:
        print(f"Your HP {player.hp}/{player.max_hp} | {monster.name} HP {monster.hp}")
        action = choose("[a]ttack [s]kill [p]otion [r]etreat: ", ("a", "s", "p", "r"))
        if action == "r":
            print("You back away from the fight.")
            return "retreat"
        if action == "a":
            monster.hp -= player.attack
            print(f"You deal {player.attack} damage.")
        elif action == "p":
            if not drink_potion(player):
                continue
        elif not cast_skill(player, monster, cooldowns, turn):
            continue

        turn += 1
        if monster.hp > 0:
            player.hp = max(0, player.hp - monster.attack)
            print(color(f"{monster.name} hits for {monster.attack} damage.", Fore.RED))

    if player.hp == 0:
        print("You wake up at the village entrance with full health.")
        return "defeat"
    player.gold += monster.gold
    print(color(f"Victory! +{monster.gold} gold, +{monster.xp} XP.", Fore.GREEN))
    if monster.drop:
        add(player.inventory, monster.drop)
        print(f"Found {ITEM_NAMES[monster.drop]}.")
    player.gain_xp(monster.xp)
    return "win"


def cast_skill(player, monster, cooldowns, turn):
    if not player.skills:
        print("You have no skills yet. Speak to Ivo in the village.")
        return False
    options = {"0": None}
    for index, name in enumerate(player.skills, 1):
        options[str(index)] = SKILLS[name]
        remaining = max(0, cooldowns.get(name, 0) - turn)
        print(f"{index}. {name} ({SKILLS[name].description}) | "
              f"{remaining} turn(s) until ready")
    selected = options[choose("Skill number or 0 to go back: ", options)]
    if selected is None:
        return False
    if cooldowns.get(selected.name, 0) > turn:
        print("That skill is still cooling down.")
        return False
    if selected.apply(player, monster):
        cooldowns[selected.name] = turn + selected.cooldown + 1
        return True
    return False
