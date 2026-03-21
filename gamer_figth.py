import random

heroe = 100
enemigo = 120
posima = 3
turno = 0


def generar_daño(min, max):
    return random.randint(min, max)


def mostrar_estado(nombre_heroe, hp_heroe, nombre_enemigo, hp_enemigo):
    barras_heroe = int((hp_heroe / 100) * 20)
    barras_enemigo = int((hp_enemigo / 120) * 20)
    barras_heroe = "[" + "🟥" * barras_heroe + "-" * (20 - barras_heroe) + "]"
    barras_enemigo = "[" + "🟥" * barras_enemigo + "-" * (20 - barras_enemigo) + "]"
    print(f"{nombre_heroe}: {hp_heroe} HP  {barras_heroe}")
    print(f"{nombre_enemigo}: {hp_enemigo} HP  {barras_enemigo}")


def turno_jugador(heroe, enemigo, posima):
    print("1.atacar (10-25)")
    print("2. cura")
    print("Habilidad especial ")
    accion = int(input("ingrese sus accion: "))
    if accion == 1:
        daño = generar_daño(10, 25)
        
        if random.randint(1,10) == 1:
            daño = daño *2
            print(f"Golpe critico {daño} de daño")
        else:
            print("Golpe normal  ")
        enemigo -= daño
        print(f"El héroe golpea por {daño} de daño")
    elif accion == 2:
        if posima > 0:
            print(f"Te curaste! HP: {heroe} | Pociones restantes: {posima}")
            heroe += 20
            posima -= 1
            print("te curaste ", posima)
        else:
            print("no tienes mas curaciones")

    elif accion == 3:
        if random.randint(0, 1) == 1:
            especial = generar_daño(30, 50)
            enemigo -= especial
            print(f"Habilidad especial {especial} de daño")
        else:
            print("La habilidad especial falló")
        
    if enemigo <= 24:
        enemigo += 20
        print("el enemigo se cura ")
    else:
        heroe -= daño
        print(f"el enemigo te golpeo por {daño}de daño ")

    return (heroe, enemigo, posima)

def turno_enemigo(heroe,enemigo):
    daño = generar_daño(15,20)
    if enemigo <= 24:
        enemigo += 20
        print("el enemigo se cura ")
    else:
        heroe -= daño
        print(f"el enemigo te golpeo por {daño}de daño ")
    return(heroe,enemigo)
# empate esto se cumple caundo el enemigo esta 0%  a se active uan habialida especial quita 50% de vidad muerte suvita tiene una probabilidad %2 
