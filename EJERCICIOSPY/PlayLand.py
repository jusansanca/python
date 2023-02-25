edad = int(input("Ingrese su edad en numeros \n"))

if 0 <= edad <=4:
 print("Imprimir boleto de entrada")
 
elif 5 <= edad < 18:
    print("Total a pagar: 20.000")
    
elif 18 <= edad <= 60:
  print("Total a pagar: 15.000")
    
else:
    print("Total a pagar: 3.000")
     