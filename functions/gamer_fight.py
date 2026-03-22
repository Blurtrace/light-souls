import config.variables as variables
import random

# ── Utilidades visuales ──────────────────────────────────────────────


def print_box(text):
    width = len(text) + 4
    border = "  ╔" + "═" * width + "╗"
    middle = f"  ║  {text}  ║"
    bottom = "  ╚" + "═" * width + "╝"
    print(f"\n{border}")
    print(middle)
    print(bottom)


def turn_separator(turn_number):
    label = f"  TURN {turn_number}  "
    line = "═" * 18
    print(f"\n  {line}{label}{line}")


# ── Lógica de combate ────────────────────────────────────────────────


def generate_damage(min, max):
    return random.randint(min, max)


def player_turn():
    turn_separator(variables.turn_count)

    print("   ╔═════════════════════════╗")
    print("   ║   🗡️  YOUR TURN  🗡️     ║")
    print("   ╠═════════════════════════╣")
    print("   ║  1. 🗡️  Attack (10-25)  ║")
    print("   ║  2. 🧪 Heal             ║")
    print("   ║  3. ✨ Special ability  ║")
    print("   ╚═════════════════════════╝")

    count = False

    while not count:
        try:
            action = int(input("\n  Enter your action: "))
            if action in (1, 2, 3):
                count = True
            else:
                print_box("Invalid option. Choose 1, 2, or 3")

        except ValueError:
            print_box("You must enter a valid number.")

    if action == 1:
        damage = generate_damage(10, 25)

        if random.randint(1, 10) == 1:
            damage *= 2
            print_box("💥  CRITICAL HIT!  x2 damage!  💥")
        else:
            print_box("🗡️  Normal hit")

        variables.real_enemy_hp -= damage
        print_box(f"🗡️  You dealt {damage} damage to {variables.enemy_nickname}!")

    elif action == 2:
        if variables.potion > 0:
            if variables.hero_hp >= variables.base_hero_hp:
                print_box("🧪 HP is already full!")
                return player_turn()
            variables.hero_hp += variables.heal_hero

            if variables.hero_hp > variables.base_hero_hp:
                variables.hero_hp = variables.base_hero_hp

            variables.potion -= 1
            print_box(
                f"🧪 +{variables.heal_hero} HP restored!  HP: {variables.hero_hp}  |  Potions: {variables.potion}"
            )
        else:
            print_box("🧪 No potions left!")
            return player_turn()

    elif action == 3:
        if random.randint(0, 1) < 1:
            print_box("⚔️  Special ability failed...")
        else:
            special_damange = generate_damage(30, 50)
            variables.real_enemy_hp -= special_damange
            print_box(f"✨ SPECIAL ABILITY!  {special_damange} damage unleashed!")


def enemy_turn():
    hp_percentage = variables.base_enemy_hp * 0.20
    damage = generate_damage(15, 20)

    if variables.real_enemy_hp < hp_percentage:
        variables.real_enemy_hp += 20
        print_box(f"💀 {variables.enemy_nickname} heals 20 HP!")
    else:
        variables.hero_hp -= damage
        print_box(f"💀 {variables.enemy_nickname} strikes you for {damage} damage!")
