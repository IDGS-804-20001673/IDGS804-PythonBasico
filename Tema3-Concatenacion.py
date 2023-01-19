

dato1="Hola"
datos2="Mundo"
saludo=dato1 +" "+ datos2
print(saludo)

print("El saludo es: %s %s" % (dato1,datos2))

saludoFinal= "Saludo {1} {0} ".format(dato1,datos2) #lo que esta adentro de las llaves funciona como un arreglo 
print(saludoFinal)

saludoFinal= "Saludo {a} {b} ".format(a=dato1,b=datos2) 
print(saludoFinal)