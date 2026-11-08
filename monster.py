class Monster:
    name = "Monster"
    max_hp = 1
    attack = 1
    gold = 0
    xp = 0
    drop = None

    def __init__(self):
        self.hp = self.max_hp


class Goblin(Monster):
    name, max_hp, attack = "Cinder Goblin", 14, 3
    gold, xp, drop = 7, 8, "ember"


class Wolf(Monster):
    name, max_hp, attack = "Ash Wolf", 17, 4
    gold, xp, drop = 6, 8, "hide"


class Glowcap(Monster):
    name, max_hp, attack = "Glowcap", 13, 3
    gold, xp, drop = 5, 7, "spore"


class Sentinel(Monster):
    name, max_hp, attack = "Basalt Sentinel", 26, 6
    gold, xp, drop = 9, 12, "potion"


class Gatekeeper(Monster):
    name, max_hp, attack = "Hollow Gatekeeper", 49, 9
    gold, xp, drop = 20, 20, "core"
