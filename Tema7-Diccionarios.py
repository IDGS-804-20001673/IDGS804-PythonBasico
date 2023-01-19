miDiccionario={"Matricula":20001673, "Apellidos": "Robledo"}

print(miDiccionario["Apellidos"])
miDiccionario["Materia"]="DWP"
print(miDiccionario)
miDiccionario["Matricula"]=2001342
print(miDiccionario)

del miDiccionario["Apellidos"]
print(miDiccionario)