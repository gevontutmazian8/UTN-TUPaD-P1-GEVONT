# Autor: Gevont Joaquin Utmazian
# Trabajo Práctico 3 - Estructuras Condicionales

# 1) Edad del usuario
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Nota del usuario
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Verificar número par
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categoría por edad
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Contraseña de longitud adecuada
contrasena = input("Ingrese su contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Moda, mediana y media (sesgo)
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# 7) Añadir exclamación si termina con vocal
texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)

# 8) Transformación del nombre
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# 9) Clasificación de magnitud de terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# 10) Estación del año según hemisferio
hemisferio = input("¿En qué hemisferio se encuentra (N/S)? ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == "N":
    if (12 <= mes <= 3) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (3 <= mes <= 6) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (6 <= mes <= 9) or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if (12 <= mes <= 3) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (3 <= mes <= 6) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (6 <= mes <= 9) or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
    


