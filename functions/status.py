import config.variables as variables

def show_status(player_nickname):
    hero_bars = int((variables.hero_hp / 100) * 20)
    enemy_bars = int((variables.real_enemy_hp / 120) * 20)
    hero_bars = "[" + "🟥" * hero_bars + "-" * (20 - hero_bars) + "]"
    enemy_bars = "[" + "🟥" * enemy_bars + "-" * (20 - enemy_bars) + "]"
    print(f"{player_nickname}: {variables.hero_hp} HP  {hero_bars}")
    print(f"{variables.enemy_nickname}: {variables.real_enemy_hp} HP  {enemy_bars}")

def win_condition():
    if variables.real_enemy_hp <= 0:
        print("CONGRATULATIONS! YOU WIN... BUT REMEMBER, EVENTUALY DEAD COMES FOR ALL OF US....")
        variables.engine_count = True
           
    elif variables.hero_hp <= 0:
        print("DEFEATED... Hope was never guaranteed. Only the struggle was real.")
        variables.engine_count = True