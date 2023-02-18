import random

SelecUser = input("Digite CARA Ó SELLO: ")

money = (random.randint(1, 2))


if SelecUser == "CARA" and money == 1:
    money = "CARA"
    print("Ud seleccionó", SelecUser, "y cayó", money,"GANÓ")
elif SelecUser == "CARA" and money == 2:
     money = "SELLO"
     print("Ud seleccionó", SelecUser, "y cayó", money,"PERDIO")
elif SelecUser == "SELLO" and money == 1:
     money = "CARA"
     print("Ud seleccionó", SelecUser, "y cayó", money,"PERDIO")
elif SelecUser == "SELLO" and money == 2:
    money = "SELLO"
    print("Ud seleccionó", SelecUser, "y cayó", money,"GANÓ")
    



