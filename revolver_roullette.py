import random
import time

def ascii_revolver():
    return r"""
  (                                 _
   )                               /=>
  (  +____________________/\/\___ / /|
   .''._____________'._____      / /|/\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \
                    0_0/____/        \
                        |----    /----\
                       || -\\ --|      \
                       ||   || ||\      \
                        \\____// '|      \
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|
    """

def ruleta_rusa():
    print("Bienvenido a la Ruleta Rusa")
    print(ascii_revolver())
    
    jugador = input("Ingrese su nombre: ")
    dealer = "Dealer"
    jugadores_lista = [jugador, dealer]
    
    balas = int(input("Ingrese el número de balas en el tambor (1-6): "))
    while balas < 1 or balas > 6:
        balas = int(input("Número inválido. Ingrese un número entre 1 y 6: "))
    
    print("\nCargando el revólver...")
    time.sleep(2)
    
    tambor = [False] * 6
    balas_pos = random.sample(range(6), balas)
    for pos in balas_pos:
        tambor[pos] = True
    
    print("El tambor gira...")
    time.sleep(2)
    
    turno = 0
    dealer_ultimo_turno = None
    while len(jugadores_lista) > 1:
        print(f"\nEs el turno de {jugadores_lista[turno]}.")
        
        if jugadores_lista[turno] == jugador:
            eleccion = input(f"¿Quieres dispararte a ti mismo (1) o al {dealer} (2)? ")
            while eleccion not in ["1", "2"]:
                eleccion = input("Opción inválida. Escribe 1 para dispararte a ti mismo o 2 para disparar al dealer: ")
        else:
            probabilidad_morir = balas / len(tambor)
            if probabilidad_morir >= 0.5:
                eleccion = "2"  # Dispara al jugador
            elif dealer_ultimo_turno == "1":
                eleccion = random.choice(["1", "2"])  # Hace una elección aleatoria
            else:
                eleccion = "1"  # Se dispara a sí mismo
            print(f"El dealer decide disparar a {'sí mismo' if eleccion == '1' else jugador}...")
        
        if eleccion == "1":
            print(f"{jugadores_lista[turno]} se apunta a sí mismo...")
            input("Presiona ENTER para apretar el gatillo...")
            if tambor[0]:
                print(f"💥 {jugadores_lista[turno]} ha sido eliminado! 💀")
                del jugadores_lista[turno]
                break
            else:
                print("🎉 Sobreviviste esta vez! Vuelve a intentarlo.")
                if jugadores_lista[turno] == dealer:
                    dealer_ultimo_turno = "1"
        else:
            oponente = (turno + 1) % 2
            print(f"{jugadores_lista[turno]} apunta a {jugadores_lista[oponente]}...")
            input("Presiona ENTER para apretar el gatillo...")
            if tambor[0]:
                print(f"💥 {jugadores_lista[oponente]} ha sido eliminado! 💀")
                del jugadores_lista[oponente]
                break
            else:
                print(f"🎉 {jugadores_lista[oponente]} ha sobrevivido! Ahora es su turno.")
                turno = oponente
                if jugadores_lista[turno] == dealer:
                    dealer_ultimo_turno = "2"
        
        tambor.append(tambor.pop(0))
        time.sleep(2)
    
    print(f"\n{jugadores_lista[0]} es el ganador! 🎉")

if __name__ == "__main__":
    ruleta_rusa()
    input("Pulsa enter para cerrar el programa ")
