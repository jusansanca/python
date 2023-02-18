import random

dado1 = (random.randint(1, 6))
dado2 = (random.randint(1, 6))

if dado1==1 and dado2==1:
    print("Dado 1 = ", dado1)
    print("Dado 2 = ", dado2)
    print("Sacaste un par de 1, ganaste")
elif dado1==2 and dado2==1 or dado1==1 and dado2==2:
    print("Dado 1 = ", dado1)
    print("Dado 2 = ", dado2)
    print("Sus dados suman 3, ganaste")
elif dado1==6 and dado2==5 or dado1==5 and dado2==6:
    print("Dado 1 = ", dado1)
    print("Dado 2 = ", dado2)
    print("Sus dados suman 11, ganaste")
elif dado1==1 and dado2==1 or dado1==1 and dado2==1 or dado1==6 and dado2==6:
    print("Dado 1 = ", dado1)
    print("Dado 2 = ", dado2)
    print("Sus dados suman 2 o 12 ganaste")
elif dado1==4 and dado2==3 or dado1==3 and dado2==4 or dado1== 5 and dado2==2 or dado1==2 and dado2==5 or dado1==6 and dado2==1 or dado1==1 and dado2==6:
    print("Dado 1 = ", dado1)
    print("Dado 2 = ", dado2)
    print("Sus dados suman 7, ganaste")
else:
 print("Dado 1 = ", dado1)
 print("Dado 2 = ", dado2)   
 print("perdiste") 