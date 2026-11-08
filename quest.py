from inventory import add, remove

MAIN_STEPS = (
    "Speak to Warden Mira in Lantern Village.",
    "Defeat the Cinder Goblin and bring its ember shard to Mira.",
    "Speak to Sera in Basalt Cavern to activate the ward.",
    "Defeat the Hollow Gatekeeper.",
    "The ward is lit. The valley is safe!",
)

SIDE_QUESTS = {
    "hide": ("A Warm Cloak", "Bring Tamsin a wolf hide.", 8, 5),
    "spore": ("Light in the Dark", "Bring Sera a glowcap spore.", 6, 5),
}


def mira_quest(player):
    if player.main_step == 0:
        player.main_step = 1
        print("Mira: Bring me the ember shard from the goblin in the northeast.")
    elif player.main_step == 1:
        if remove(player.inventory, "ember"):
            player.main_step = 2
            print("Mira: The shard is warm. Take the southeast path to Sera in the cavern.")
        else:
            print("Mira: The goblin in the northeast still has our shard.")
    else:
        print("Mira: Keep the lanterns burning. We are counting on you.")


def activate_ward(player):
    if player.main_step == 2:
        player.main_step = 3
        print("Sera fits Mira's ward into the stone. The boss chamber opens.")


def side_quest(player, item):
    name, objective, gold, xp = SIDE_QUESTS[item]
    status = player.side_quests.get(item)
    if status == "complete":
        print(f"{name} is already complete.")
        return
    if status is None:
        player.side_quests[item] = "active"
        print(f"Side quest started: {name}. {objective}")
    if remove(player.inventory, item):
        player.side_quests[item] = "complete"
        player.gold += gold
        add(player.inventory, "potion")
        print(f"{name} complete! +{gold} gold, +{xp} XP, +1 potion.")
        player.gain_xp(xp)
    elif status == "active":
        print(objective)


def show(player):
    print("Main quest — " + MAIN_STEPS[player.main_step])
    for item, status in player.side_quests.items():
        name, objective, _, _ = SIDE_QUESTS[item]
        print(f"{name} ({status}) — {objective}")
    if not player.side_quests:
        print("Talk to NPCs to discover side quests.")
