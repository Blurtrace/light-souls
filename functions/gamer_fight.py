import config.variables as variables
import random

def generate_damage(min, max):
    return random.randint(min, max)

def player_turn():   
    print("1. Attack (10-25)")
    print("2. Heal")
    print("3. Special ability")

    count = False
    
    while not count:
        try:
            action = int(input("Enter your action: "))
            if action in (1, 2, 3):
                count = True
            else:
                print("Invalid option. Choose 1, 2, or 3")
        
        except ValueError:
            print("You must enter a valid number.")
            
    if action == 1:
        damage = generate_damage(10, 25)
        
        if random.randint(1,10) == 1:
            damage *= 2
            print(f"Critical hit")
        else:
            print("Normal hit")
        
        variables.real_enemy_hp -= damage
        print(f"The hero hits for {damage} damage")
        
    elif action == 2:
        if variables.potion > 0:
            # variables.hero_hp += variables.heal_hero
            # heal_for_hero      = variables.hero_hp + variables.heal_hero
            # print("Verificación de curación" , heal_for_hero)
            if variables.hero_hp >= variables.base_hero_hp:
                print("Your life is at its maximum; you cannot heal more than 100 HP.")
                return player_turn()  #Vuelve a pedir el turno
                # diference =  heal_for_hero - variables.base_hero_hp
                # heal_for_hero = variables.hero_hp + variables.heal_hero - diference
                # print("1",heal_for_hero)
            variables.hero_hp += variables.heal_hero    
            
            if variables.hero_hp > variables.base_hero_hp:
                variables.hero_hp = variables.base_hero_hp
                
            variables.potion -= 1
            print(f"You healed! HP: {variables.hero_hp} | Remaining potions: {variables.potion}")
        else:
            print("You have no more potions")
            return player_turn()
            

    elif action == 3:
        if random.randint(0, 1) < 1:
            print("The special ability failed") 
        else:
            special_damange = generate_damage(30, 50)
            variables.real_enemy_hp -= special_damange
            print(f"Special ability {special_damange} damage")
        


def enemy_turn():
    hp_percentage = variables.base_enemy_hp * 0.20
    damage = generate_damage(15,20)
    
    if variables.real_enemy_hp < hp_percentage:
        variables.real_enemy_hp += 20
        print("The enemy heals")
    else:
        variables.hero_hp -= damage
        print(f"The enemy hits you for {damage} damage")