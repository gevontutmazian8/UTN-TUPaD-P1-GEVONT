# Autor: Gevont Joaquin Utmazian
# Trabajo Práctico 3 - Estructuras Condicionales

# Ejercicio 1: Verificar si una persona es mayor de edad
edad = int(input("Ingrese su edad: ")) 
if edad >= 18: 
    print("Es mayor de edad. ")
else: 
    print("Es menor de edad. ")


# Ejercicio 2: Aprobado o desaprobado
nota = int(input("Ingrese la nota del alumno: "))
if nota >= 6: 
    print ("Aprobado")
else: 
    print ("Desaprobado")

# Ejercicio 3: Numero par 
numero = int(input("Ingrese un número par: ")) 
while numero % 2 != 0:
    print("Por favor ingrese un número par. ")
    numero = int(input("Ingrese un número par: "))
    
print ("El número es par. ")
    


