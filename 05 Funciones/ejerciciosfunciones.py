import math

# 1. Imprimir "Hola Mundo"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludar al usuario con su nombre
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# 3. Mostrar información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# 4. Calcular el perímetro de un círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return suma, resta, multiplicacion, division

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# =========================
# Programa principal
# =========================

# Punto 1
imprimir_hola_mundo()

# Punto 2
nombre_usuario = input("\nIngrese su nombre: ")
saludar_usuario(nombre_usuario)

# Punto 3
nombre = input("\nIngrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Punto 4
radio = float(input("\nIngrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# Punto 5
segundos = int(input("\nIngrese una cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Punto 6
numero_tabla = int(input("\nIngrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# Punto 7
a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Punto 8
peso = float(input("\nIngrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# Punto 9
celsius = float(input("\nIngrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Punto 10
n1 = float(input("\nIngrese el primer número para calcular el promedio: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")
