class Skill:
    name = ""
    description = ""
    cooldown = 0

    def apply(self, player, monster):
        raise NotImplementedError


class Firebolt(Skill):
    name = "Firebolt"
    description = "Deals attack + 5 damage"
    cooldown = 2

    def apply(self, player, monster):
        damage = player.attack + 5
        monster.hp -= damage
        print(f"Firebolt deals {damage} damage.")
        return True


class Mend(Skill):
    name = "Mend"
    description = "Restores up to 14 HP"
    cooldown = 3

    def apply(self, player, monster):
        healed = min(14, player.max_hp - player.hp)
        if healed == 0:
            print("You already have full health.")
            return False
        player.hp += healed
        print(f"Mend restores {healed} HP.")
        return True


SKILLS = {skill.name: skill for skill in (Firebolt(), Mend())}
