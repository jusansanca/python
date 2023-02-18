print ("Caja Registradora")


price=int(10000)

print(price)

totalProducts=int(input("Ingrese la cantidad de productos comprados: "))

totaltoPay=int(price*totalProducts)

print("El valor total a pagar por los", totalProducts,"es: ",totaltoPay)

pay=int(input("Ingrese el monto de dinero recibido: "))

changetoPay=(pay-totaltoPay)

print("El cambio a entregar es: ", changetoPay)



