from dataclasses import dataclass, field

from colorama import Fore

from monster import Gatekeeper, Glowcap, Goblin, Sentinel, Wolf
from ui import color

START = ("village", 1, 1)


@dataclass(frozen=True)
class Area:
    title: str
    layout: tuple[str, ...]
    npcs: dict = field(default_factory=dict)
    encounters: dict = field(default_factory=dict)
    exits: dict = field(default_factory=dict)

    def walkable(self, row, col):
        return (0 <= row < len(self.layout)
                and 0 <= col < len(self.layout[row])
                and self.layout[row][col] != "#")

    def show(self, player):
        print(color(f"\n{self.title}", Fore.CYAN))
        for row, line in enumerate(self.layout):
            tiles = []
            for col, tile in enumerate(line):
                position = (row, col)
                if position == (player.row, player.col):
                    tile = color("@", Fore.GREEN)
                elif position in self.npcs:
                    tile = color("N", Fore.YELLOW)
                elif position in self.exits:
                    tile = color(">", Fore.CYAN)
                elif position in self.encounters:
                    encounter, _ = self.encounters[position]
                    if encounter not in player.defeated:
                        tile = color("B" if encounter == "boss" else "M", Fore.RED)
                tiles.append(tile)
            print(" ".join(tiles))
        print("@ You  N NPC  M Monster  B Boss  > Exit  # Wall")


AREAS = {
    "village": Area(
        "Lantern Village",
        (
            "##########",
            "#........#",
            "#.##.....#",
            "#......#.#",
            "#.##.....#",
            "#........#",
            "##########",
        ),
        npcs={(1, 3): "mira", (1, 6): "bram", (3, 1): "ivo", (3, 5): "tamsin"},
        encounters={(1, 8): ("goblin", Goblin), (2, 4): ("wolf", Wolf)},
        exits={(5, 8): ("cavern", 1, 1)},
    ),
    "cavern": Area(
        "Basalt Cavern",
        (
            "###########",
            "#....######",
            "###.......#",
            "#....##...#",
            "#.##......#",
            "#.........#",
            "###########",
        ),
        npcs={(2, 4): "sera"},
        encounters={(2, 5): ("glowcap", Glowcap), (2, 7): ("sentinel", Sentinel),
                    (5, 9): ("boss", Gatekeeper)},
        exits={(1, 1): ("village", 5, 8)},
    ),
}
