notafin=0

for i in range(0, 4):
    notaEst = float(input("Ingrese las notas: \n"))
    
    notafin = notafin + notaEst
    
prom = notafin/ i

if prom <= 2.9 :
    print ("Reprobaste la asignatura con un promedio de: ", prom)
elif 3.0 < prom <= 4.0:
    print("Pasaste raspando la asignatura con un promedio de: ", prom)
else:
    print("Aprobaste con buenos resultados con un promedio de: ", prom)
    




#0.0 y 2.9 reprobo
#3.0 y 4.0 Pasaste raspnado
#4.0 Buena nea

    
    
    
