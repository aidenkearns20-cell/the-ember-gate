from dataclasses import asdict, dataclass, field

from inventory import count


@dataclass
class Player:
    hp: int = 36
    xp: int = 0
    level: int = 1
    gold: int = 10
    skills: list[str] = field(default_factory=list)
    inventory: dict[str, int] = field(default_factory=lambda: {"potion": 1})
    map_id: str = "village"
    row: int = 1
    col: int = 1
    main_step: int = 0
    side_quests: dict[str, str] = field(default_factory=dict)
    defeated: list[str] = field(default_factory=list)

    @property
    def max_hp(self):
        return 36 + 8 * (self.level - 1)

    @property
    def attack(self):
        return 6 + 2 * (self.level - 1) + 3 * bool(count(self.inventory, "blade"))

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= 15 * self.level:
            self.xp -= 15 * self.level
            self.level += 1
            self.hp = self.max_hp
            print(f"Level {self.level}! Your health is restored.")

    def to_save(self):
        return asdict(self)

    def show(self):
        print(f"Level {self.level} | HP {self.hp}/{self.max_hp} | "
              f"XP {self.xp}/{15 * self.level} | Gold {self.gold} | Attack {self.attack}")
        print("Skills: " + (", ".join(self.skills) or "none"))
