import random
import os

os.system("cls")

def jugar_bingo_individual():

    def generar_carton():
        return set((random.sample(range(1,91), 15)))

    def verificar_ganador(carton,salientes):
        return carton.issubset(salientes) 

    def sacar_numero(bolillero,salientes):
        nume = random.choice(list(bolillero))
        bolillero.remove(nume)
        salientes.add(nume)
        return nume

    def estado_del_carton(carton,salientes):
        marcados = carton & salientes
        faltantes = carton - salientes

        print("_"*40)
        for num in carton :
            if num in salientes:
                print(num, "✓", end=" ",sep="")
            else :
                print(num, end="  ")
        print()
        print("_"*40)
        print(f"Marcados: {len(marcados)} / 15  |  Faltan: {len(faltantes)}")


    print("EMPIEZA EL JUEGO")
    carton= generar_carton()
    print(f"Tu cartón: {sorted(carton)}")
    input("Presiona enter para empezar...")
    bolillero= set(range(1,91))
    salientes=set()

    cont=0
    while not verificar_ganador(carton,salientes):
        num = sacar_numero(bolillero,salientes)
        print(f"Salio el {num}") 
        cont += 1
        if num in carton:
            estado_del_carton(carton, salientes)
        input("Presiona enter para continuar...")

    print(f"!BINGO! Ganaste en {cont} turnos")
