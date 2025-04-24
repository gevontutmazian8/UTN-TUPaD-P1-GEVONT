

# Ejercicio 1 Imprimir los números del 1 al 100 de forma creciente mostrando un número por línea.

for i in range(1,101): 
    print(i)
    
# Ejercicio 2 Solicite un número entero al usuario y determine la cantidad de digitos que tiene.


numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))  # abs() para manejar números negativos
print("El número tiene ", cantidad_digitos, "digitos.")

# Ejercicio 3 Sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores,

numero = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
sumatoria = 0
for cont in range(numero+1, numero2):  ## Se excluye el primer numero con el +1 y el segundo nunca llega a entrar al rango.
    sumatoria +=  cont
print("La sumatoria de los números entre ", numero, "y", numero2, "es: ", sumatoria)


# Ejercicio 4 Crea un programa que permita al usuario ingresar números enteros y los sume ensecuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int(input("Ingrese un número entero (0 para salir): "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para salir): "))
    print ("La suma acumulada es: ", suma)
    



# Ejercicio 5 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_usuario = -1   # Inicializamos el número del usuario en -1 para entrar al bucle
while numero_usuario != numero_aleatorio: 
    numero_usuario = int(input("Adivina el número entre el 0 y el 9: "))
    if numero_usuario < 0 or numero_usuario > 9:
        print("Número fuera de rango. Intenta nuevamente.")
        continue  # Salta a la siguiente iteración del bucle sin contar el intento
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    elif numero_usuario > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")



# Ejercicio 6 Imprimir los números del 1 al 100 de forma decreciente mostrando un número por línea.

for i in range (100, 0, -1):
    print(i)

# Ejercicio 7 Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero_max = int(input("Ingrese un número entero positivo: "))
suma = 0
for cont in range(1, numero_max + 1): 
    suma+= cont
print("La suma de los números entre 0 y ", numero_max, "es: ", suma)

# Ejercicio 8 – Clasificación de números
def ejercicio_8():
    print("=== Ejercicio 8 ===")
    CANTIDAD = 100  # Podés cambiar este valor para pruebas

    pares = impares = positivos = negativos = 0

    for _ in range(CANTIDAD):
        num = int(input("Ingresá un número entero: "))

        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1

    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")


# Ejercicio 9 – Calcular la media
def ejercicio_9():
    print("=== Ejercicio 9 ===")
    CANTIDAD = 100  # Cambiar para pruebas

    suma = 0

    for _ in range(CANTIDAD):
        num = int(input("Ingresá un número entero: "))
        suma += num

    media = suma / CANTIDAD
    print(f"La media de los {CANTIDAD} números es: {media}")


# Ejercicio 10 – Invertir los dígitos de un número
def ejercicio_10():
    print("=== Ejercicio 10 ===")
    numero = input("Ingresá un número entero: ")

    if numero.startswith('-'):
        invertido = '-' + numero[:0:-1]  # conserva el signo
    else:
        invertido = numero[::-1]

    print(f"Número invertido: {invertido}")







