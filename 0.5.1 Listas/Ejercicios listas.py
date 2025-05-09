# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplic_4 = list(range(4, 101, 4))
print("Multiples de 4:", multiplic_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
mis_elementos = ["pelota", "computadora", "música", "fútbol", "cine"]
print("Penúltimo elemento:", mis_elementos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Lista con palabras:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista de animales actualizada:", animales)

# 5) Análisis de programa: (No proporcionado en la pregunta. Puedo ayudarte si me lo envías).

# 6) Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print("Primeros dos números:", numeros[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"
autos[2] = "deportivo"
print("Lista de autos actualizada:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print("Lista de dobles:", dobles)

# 9) Dada la lista “compras”, realizar los siguientes cambios:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print("Lista de compras actualizada:", compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” con los siguientes elementos:
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
