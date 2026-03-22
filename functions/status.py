import config.variables as variables

def show_status(player_nickname):
    hero_bars = int((variables.hero_hp / 100) * 20)
    enemy_bars = int((variables.real_enemy_hp / 120) * 20)
    hero_bars = "[" + "🟩" * hero_bars + "-" * (20 - hero_bars) + "]"
    enemy_bars = "[" + "🟩" * enemy_bars + "-" * (20 - enemy_bars) + "]"
    print(f"{player_nickname}: {variables.hero_hp} HP  {hero_bars}")
    print(f"{variables.enemy_nickname}: {variables.real_enemy_hp} HP  {enemy_bars}")

def win_condition():
    if variables.real_enemy_hp <= 0:
        print("\n  ╔══════════════════════════════════════╗")
        print("   ║         ★  V I C T O R Y  ★         ║")
        print("   ╠══════════════════════════════════════╣")
        print("   ║  You won... but remember,            ║")
        print("   ║  death comes for all of us.          ║")
        print("   ╚══════════════════════════════════════╝")
        variables.engine_count = True
           
    elif variables.hero_hp <= 0:
        print("\n  ╔══════════════════════════════════════╗")
        print("   ║         ✖  D E F E A T E D  ✖       ║")
        print("   ╠══════════════════════════════════════╣")
        print("   ║  Hope was never guaranteed.          ║")
        print("   ║  Only the struggle was real.         ║")
        print("   ╚══════════════════════════════════════╝")
        variables.engine_count = True