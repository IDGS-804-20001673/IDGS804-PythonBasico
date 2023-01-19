#las tuplas son estructuras de datos propios de python permiten almacenar distintos valores no se pueden reemplazar sus datos
#una tupla es similar a un arreglo
tupla=(1,2,3,"uno", "dos")
print(tupla)

tupla2=(7,"Leonel",True,12.5,23+7j)

tupla3=(1,2,3,(4,5,6))

print(tupla2[1])
print(tupla3)
print(tupla2[4]) #es lo mismo que 
print(tupla2[-1])
print(tupla2[0:2])
print(tupla2[:4])
print(tupla2[2:])

tuplaNueva =tupla+tupla2
print(tuplaNueva)

print(tupla3[3][0])


