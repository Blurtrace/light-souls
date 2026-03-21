import config.variables as variables
from functions.gamer_fight import (
    player_turn, enemy_turn)
from functions.status import (
    show_status, win_condition)

#Player's nickname
player_nickname = input("Select your nickname: ")

print("=================================================================")
print(f" ⚔️   WELCOME {player_nickname} TO THE LIGHT OF THE SOULS   ⚔️ ")
print("=================================================================")
print("Choose your actions wisely.")
print("Prepare yourself for combat... ")

while not variables.engine_count:
    player_turn()
    enemy_turn()
    show_status(player_nickname)
    win_condition()