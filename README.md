# The Ember Gate

A terminal RPG for ET 2100 Assignment 10. Restore the ward that protects Lantern Village by tracking down its ember shard and defeating the Hollow Gatekeeper.

## Play

Open a terminal in this folder and run:

```powershell
uv run main.py
```

The first run installs TinyDB and Colorama. If you use Python 3.10 or newer with pip instead:

```powershell
python -m pip install colorama==0.4.6 tinydb==4.8.2
python main.py
```

Register a local game account. Password characters are hidden as you type. Use **W/A/S/D** followed by Enter to move, **T** while standing on an **N** tile to talk, and **J** to see your objectives. **C** shows character stats and **I** opens your inventory. Enter an **M** tile to fight or a **>** tile to change maps. **Q** saves and exits.

## Gameplay recording route

1. Start with a fresh account and capture the story intro. In the village, speak with Mira near the entrance and Ivo down the west path to learn Firebolt.
2. Defeat the goblin in the northeast and bring the shard to Mira. Defeat the wolf and talk to Tamsin to claim the hide reward. Buy an iron blade from Bram for 15 gold, then return to Ivo once you reach level 2 to learn Mend.
3. Show your character, inventory, and journal. Save and quit, launch the game again, and log in to show that the same location and progress return.
4. Take the exit in the southeast. Talk to Sera, defeat the Glowcap, and return to her for the spore reward. Fight the Basalt Sentinel on the upper path.
5. Use a potion before the final fight if your HP is low. Enter the boss tile in the southeast. Use Firebolt for damage, regular attacks while it recharges, and Mend or potions if needed. Capture the victory screen.

## How the code works

| File | Responsibility |
| --- | --- |
| `main.py` | Prints the story and starts the account and game sessions. |
| `auth.py` | Validates usernames, registers players, and verifies passwords. |
| `database.py` | Reads and writes the TinyDB account documents. |
| `game.py` | Handles the main loop, moves, encounters, map transitions, and autosaves. |
| `player.py` | Holds persistent state and calculates leveling, max HP, and attack. |
| `maps.py` | Defines terrain and the coordinates of NPCs, monsters, and exits. |
| `npc.py` | Dispatches dialogue, skill training, shopping, and quest interactions. |
| `quest.py` | Handles quest objectives, progress, and turn-in rewards. |
| `shop.py` | Checks gold and ownership before adding a purchased item. |
| `inventory.py` | Counts, adds, consumes, and displays items. |
| `monster.py` | Defines the shared monster initializer and five monster types. |
| `skill.py` | Defines the skill interface, Firebolt, Mend, and the skill lookup. |
| `combat.py` | Runs turns, cooldowns, counterattacks, and victory rewards. |
| `ui.py` | Colors terminal output and validates menu input. |

## Submission

For submission, publish this folder's source files and README to a GitHub repository. `saves.json` and the local environment are excluded by `.gitignore`. Canvas asks for the GitHub repo link and a recording from the start through the victory screen.
