leche = input("¿Trajo la leche? \n Digite S o N \n")
pan = input("¿Trajo el pan? \n Digite S o N \n")
huevos = input("¿Trajo los huevos? \n Digite S o N \n")

#Mamá Estricta
if leche == "S" and pan == "S" and huevos == "S":
    print("Era lo minimo, venga y desayuna")
else:
    print("Chanclazo")
    
#Mamá Comprensiva

if leche == "S" or pan == "S" or huevos == "S":
    print("Bueno mi amor")
else:
 print("Ayy me va tocar ir a mi")
    