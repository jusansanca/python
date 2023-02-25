budGet = 10
totalSpent = 0


while budGet>=totalSpent:
 recExp = str(input("¿Desea registrar un gasto? Esciba SI/si o NO/no "))  
 if recExp == "SI" or recExp =="si":
  for i in range (1,3):
    
     recSpent = int(input("Ingrese el valor de su gasto: \n NOTA: Recuerde que solo puede regsitrar 3 gastos: \n"))
     budGet = budGet - recSpent
     totalSpent = totalSpent + recSpent
     print("Su gasto fue de ", totalSpent, "el saldo de su presupuesto es ", budGet)
     if budGet 
     answ = str(input("¿Desea registrar otro gasto? Esciba SI/si o NO/no "))
     if answ == "NO" or answ == "no":
        print("Su gasto final es de ", totalSpent, "el saldo de su presupuesto es ", budGet) 
        i = 3
     elif i == 3:
        print("Ud no puede regsitar mas gastos, su presupuesto es de ", budGet, "y su gasto total fue de ", totalSpent)
    
     else:
        i = i + 1
        print("Su gasto fue de ", totalSpent, "el saldo de su presupuesto es ", budGet)
 else:
    print("Hasta pronto")
    break
print("Su gasto final es de ", totalSpent, "el saldo de su presupuesto es ", budGet) 
 
    
            
        
        
        