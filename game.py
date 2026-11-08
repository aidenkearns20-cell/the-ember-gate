from colorama import Fore

import inventory
import quest
from combat import battle
from maps import AREAS, START
from npc import talk
from player import Player
from ui import choose, color

DIRECTIONS = {"w": (-1, 0), "a": (0, -1), "s": (1, 0), "d": (0, 1)}


class Game:
    def __init__(self, store, account):
        self.store = store
        self.account_id = account.doc_id
        self.player = Player(**account["progress"])

    def run(self):
        player = self.player
        while player.main_step < 4:
            AREAS[player.map_id].show(player)
            action = choose(
                "[w/a/s/d] Move  [t] Talk on N  [c] Character  [i] Inventory  "
                "[j] Journal  [p] Potion  [q] Save & quit: ",
                (*DIRECTIONS, "t", "c", "i", "j", "p", "q"),
            )
            if action in DIRECTIONS:
                self.move(*DIRECTIONS[action])
            elif action == "t":
                npc = AREAS[player.map_id].npcs.get((player.row, player.col))
                if npc:
                    talk(npc, player)
                else:
                    print("Stand on an N tile to talk to that NPC.")
            elif action == "c":
                player.show()
            elif action == "i":
                inventory.show(player.inventory)
            elif action == "j":
                quest.show(player)
            elif action == "p":
                inventory.drink_potion(player)
            else:
                self.save()
                print("Game saved. See you next time.")
                return
            self.save()

        print(color("VICTORY! The Ember Gate shines again. The valley is safe.", Fore.GREEN))
        player.show()
        inventory.show(player.inventory)

    def save(self):
        self.store.save(self.account_id, self.player.to_save())

    def move(self, row_change, col_change):
        player = self.player
        area = AREAS[player.map_id]
        destination = (player.row + row_change, player.col + col_change)
        if not area.walkable(*destination):
            print("A wall blocks the way.")
            return
        if destination in area.exits:
            next_map, row, col = area.exits[destination]
            if next_map == "cavern" and player.main_step < 2:
                print("The cavern path is sealed. Help Mira recover the ember shard.")
                return
            player.map_id, player.row, player.col = next_map, row, col
            return

        encounter = area.encounters.get(destination)
        if encounter and encounter[0] not in player.defeated:
            encounter_id, monster_type = encounter
            if encounter_id == "boss" and player.main_step < 3:
                print("The boss chamber is sealed. Speak to Sera.")
                return
            result = battle(player, monster_type())
            if result == "defeat":
                player.map_id, player.row, player.col = START
                player.hp = player.max_hp
                return
            if result == "retreat":
                return
            player.defeated.append(encounter_id)
            if encounter_id == "boss":
                player.main_step = 4
        player.row, player.col = destination
