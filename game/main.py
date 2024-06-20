import random



cpu_winers = 0
usuario_winers = 0



rounds = 1


while True:
    
    print("*"*10)
    print("ROUND", rounds)
    print("*"*10)
    

    usuario = input("piedra, papel o tijera: ")
    usuario = usuario.lower()
    opcion = ("piedra", "papel", "tijera")
    cpu_opcion = random.choice(opcion)
    print("opcion de cpu: ", cpu_opcion)

    if usuario != opcion:
        print("vuelve a intentarlo")
        continue

    if usuario == cpu_opcion:
        print("Empate")
    elif usuario == "piedra" and cpu_opcion == "papel":
        print("cpu gana")
        cpu_winers +=1
    elif usuario == "piedra" and cpu_opcion == "tijera":
        print("usuario gana")
        usuario_winers +=1
    elif usuario == "papel" and cpu_opcion == "tijera":
        print("cpu gana")
        cpu_winers +=1
    elif usuario == "papel" and cpu_opcion == "piedra":
        print("usuario gana")
        usuario_winers +=1
    elif usuario == "tijera" and cpu_opcion == "piedra":
        print("cpu gana")
        cpu_winers +=1
    elif usuario == "tijera" and cpu_opcion == "papel":
        print("usuario gana")
        usuario_winers +=1
         
    
    
    if usuario_winers == 3:
        print("USUARIO GANA LA PARTIDA")
        break
    elif cpu_winers == 3:
        print("CPU GANA LA PARTIDA")
        break
    
    rounds += 1    
        