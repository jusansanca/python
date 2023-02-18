adivinar = int(input("Por favor piense un número, luego sumele 5 a ese numero que penso \n despues multipliquelo por 3 y finalmente restele 15.\n por favor ingrese el resultado que le dio \n"))

resul = adivinar/3
print("¿El numero que usted penso es: ", resul, "?\n\n")
resp = input("Responde SI o NO \n")

 
if resp == "SI" or resp == "Si" or resp == "si":
    print("\nSoy un adivino")
else:
    print("Rectifica las cuentas te daras cuenta que no me equivoco")    


