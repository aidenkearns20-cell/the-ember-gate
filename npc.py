from colorama import Fore

from quest import activate_ward, mira_quest, side_quest
from shop import visit
from skill import SKILLS
from ui import color

DIALOGUE = {
    "mira": "Mira: That gate kept the valley safe for a hundred years.",
    "bram": "Bram: A sharp blade is worth its weight in lantern oil.",
    "ivo": "Ivo: Even a little spark can light a way through the dark.",
    "tamsin": "Tamsin: The nights are getting colder. I could use an ash wolf hide.",
    "sera": "Sera: The cavern stones remember the old ward. Listen closely.",
}


def talk(npc, player):
    print(color(DIALOGUE[npc], Fore.YELLOW))
    if npc == "mira":
        mira_quest(player)
    elif npc == "bram":
        visit(player)
    elif npc == "ivo":
        teach(player)
    elif npc == "tamsin":
        side_quest(player, "hide")
    elif npc == "sera":
        activate_ward(player)
        side_quest(player, "spore")


def teach(player):
    for name, required_level in (("Firebolt", 1), ("Mend", 2)):
        if name in player.skills:
            continue
        if player.level >= required_level:
            player.skills.append(name)
            print(f"You learned {name}! {SKILLS[name].description}.")
        else:
            print(f"Ivo can teach you {name} at level {required_level}.")
