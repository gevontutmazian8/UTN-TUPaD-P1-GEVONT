# Práctico 11: Aplicación de la Recursividad
# Gevont Joaquin Utmazian

# 1. Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factoriales_hasta(n):
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

# 2. Serie de Fibonacci
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3. Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# 4. Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    if n == 0:
        return "0"
    else:
        return decimal_a_binario(n)

# 5. Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6. Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# 7. Pirámide de bloques
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# 8. Contar dígito dentro de un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

# --------------------------
# Ejemplo de uso:

if __name__ == "__main__":
    print("1) Factoriales hasta N")
    n = int(input("Ingrese un número: "))
    factoriales_hasta(n)

    print("\n2) Serie de Fibonacci")
    mostrar_fibonacci(n)

    print("\n3) Potencia recursiva")
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

    print("\n4) Conversión a binario")
    numero_decimal = int(input("Ingrese un número decimal: "))
    print(f"Binario: {convertir_a_binario(numero_decimal)}")

    print("\n5) ¿Es palíndromo?")
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    print("Resultado:", es_palindromo(palabra))

    print("\n6) Suma de dígitos")
    num = int(input("Número: "))
    print("Suma de dígitos:", suma_digitos(num))

    print("\n7) Contar bloques en pirámide")
    niveles = int(input("Bloques en el nivel más bajo: "))
    print("Total de bloques:", contar_bloques(niveles))

    print("\n8) Contar dígitos en número")
    numero = int(input("Número: "))
    dig = int(input("Dígito a contar: "))
    print(f"Aparece {contar_digito(numero, dig)} veces")
