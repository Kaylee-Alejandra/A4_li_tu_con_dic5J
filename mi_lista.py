
print("ejemplo de listas")
arcoiris=["verde"," azul", " morado"]
print(arcoiris)
longitud=len(arcoiris)
print("elementos que contiene la lista arcoiris ",longitud)
print(f"elementos que contiene la lista arcoiris v2 {longitud}")
print("accediendo a un elemento de la lista")
print(arcoiris[1])
print("{arcoiris[1]}")
print(f"elementos en la pocision 0 es: {arcoiris[1]}")
print(f"el primer color del arcoiris es ", arcoiris[0])
print("agregar un elemento de la lista")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)
print("listar los elementos de la lista ciclo for")
for luevano in arcoiris:
    print(luevano)