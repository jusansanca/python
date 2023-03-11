import random

apuestaGlobal = 0
dineroAcumulado = 0
numJuegos = 0

def jugar(apuesta):
    global apuestaGlobal, dineroAcumulado, numJuegos

    num = random.randint(1,2)

    if num==1:
        moneda="cara"
    else:
        moneda="sello"

    print ("¿como te llamas?")
    nombre = input()

    print("\n",nombre+"\n¡Buena Suerte!\n¿Escoge cara o sello?")
    respuesta = input()
    input(nombre+" Seguro escoges\n"+respuesta+"\nconfirma si o no\n")

    if respuesta == moneda:
        dineroGanado = apuesta*2
        dineroAcumulado += dineroGanado
        apuestaGlobal += apuesta
        print("\n¡Muy bien, "+nombre+", salio "+moneda+", has ganado!, Ganaste $"+ str(dineroGanado)+" Ahora tienes $"+ str(dineroAcumulado)+" acumulados.")
    else:
        apuestaGlobal -= apuesta
        print("\n¡Mala suerte, "+nombre+", salio "+moneda+", has perdido! Perdiste $"+ str(apuesta)+" Ahora tienes $"+ str(dineroAcumulado)+" acumulados.")

    numJuegos += 1

print("Vamos a jugar Cara o Sello, lo recuerdas?,\n"
           "Apostamos?, entonces empecemos!\n")
while True:
    apuesta = input("Ingresa la cantidad de dinero que deseas apostar o salir para terminar: \n")
    if apuesta == "salir":
        break
    else:
        apuesta = int(apuesta)
        jugar(apuesta)

print("Has jugado "+ str(numJuegos)+" veces y has acumulado $"+ str(dineroAcumulado)+" en total.")