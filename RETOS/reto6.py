from random import randint
totalComp  = 0
regProd =0
compra = "S"

#regProd = int(input("Ingrese la cantidad de productos comprados: \n"))

# for i in range(regProd): '''
while compra == "S":

    cantProd = int(input("Ingrese la cantidad de productos comprados: \n"))
    precio = int(input("Ingrese el valor del producto comprado: \n"))

    valComp = cantProd * precio

    compra = input("Desea segur registrando compra? presione S para continuar o N para terminar")   
    totalComp = totalComp + valComp
    
    print("El total del su compra es: ", totalComp)

a=randint(1,4)

if totalComp >= 50000:
   if a==1:
    print("Felicidades, sacaste bolita roja. Tienes un descuento del 10%")
    totalPagar = (totalComp / 100) * 10
    print()
    print("Tu descuento es de: ", totalComp)
   
   elif a==2:
    print("Felicidades, sacaste bolita AZUL. Tienes un descuento del 30%")
    totalComp = (totalComp / 100) * 30
    print("Tu descuento es de: ", totalComp)

   elif a==3:
    print("Felicidades, sacaste bolita AMARILLA. Tienes un descuento del 50%")
    totalComp = (totalComp / 100) * 50
    print()
    print("Tu descuento es de: ", totalComp)

   elif a==4:
    print("Felicidades, sacaste bolita BLANCA. Te llevas la compra gratis!")
    totalPagar = 0
    print("Osea, tienes que pagar: ", totalPagar)

else:
    print("Gracias por su compra")












