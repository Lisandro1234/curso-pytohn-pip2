import random



def e_opcion():
    
    opcion = ("piedra", "papel", "tijera")
    usuario = input("piedra, papel o tijera: ")
    usuario = usuario.lower()
    if not usuario in opcion:
        print("vuelve a intentarlo")
        return None, None
    
    cpu_opcion = random.choice(opcion)
    print("opcion de cpu: ", cpu_opcion)
    return usuario, cpu_opcion


def partida(usuario, cpu_opcion, usuario_winers, cpu_winers):
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
    return usuario_winers, cpu_winers


def ganador(usuario_winers, cpu_winers):
    if usuario_winers == 3:
        print("USUARIO GANA LA PARTIDA")
        exit()
    elif cpu_winers == 3:
        print("CPU GANA LA PARTIDA")
        exit()
        
    

def run_game():
    usuario_winers = 0
    cpu_winers = 0
    rounds = 1
    
    while True:
    
        print("*"*10)
        print("ROUND", rounds)
        print("*"*10)
    
        rounds += 1

        usuario, cpu_opcion = e_opcion()
        usuario_winers, cpu_winers = partida(usuario, cpu_opcion, usuario_winers, cpu_winers)
        ganador(usuario_winers, cpu_winers)

    
        
           
run_game()