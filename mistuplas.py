print("Ejemplo de tuplas")
canciones=("te amo", " el noa noa", " amor eterno")

print(canciones)
y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)

print(x)     

print("listado de elementos de tupla canciones ciclo for")
for luevano in canciones:
    print(luevano)