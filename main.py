#Factorial de un numero

def factorial(factoriales):
    if factoriales == 1 or factoriales == 0:
        return 1
    else:
        return factoriales * factorial(factoriales-1)

def suma_naturales(naturales):
    if naturales == 0:
        return 0
    else:
        return naturales + suma_naturales(naturales-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def contador_letras(palabra, letra):
    if not palabra:
        return 0

    primer_Caracter = palabra[0]
    palabra_completa = palabra[1:]

    if primer_Caracter == letra:
        return 1 + contador_letras(palabra_completa, letra)
    else:
        return 0 +contador_letras(palabra_completa, letra)


def inevrtir_texto(word):
    pass

def exponente(n, e):
    if n == 0 and e == 0:
        return 0
    elif n == 0 and e != 0:
        return 1
    else:
        return n ** e

while True:
    print("Menu de recursividad\n"
          "1. Calcular el factorial de un numero\n"
          "2. Suma de naturales\n"
          "3. Susecion de fibonacci\n"
          "4. Contador de letras\n"
          "5. Invertir texto\n"
          "6. Sacar el exponente de un numero\n")
    select = input("Ingresa una de las siguientes opciones: ")
    match select:
        case "1":
            try:
                factoriales = int(input("Ingresa un numero: "))
                print(f"El factorial de {factoriales} es de {factorial(factoriales)}")
            except ValueError:
                print("Debe ser un valor entero")
        case "2":
            try:
                naturales = int(input("Ingresa un numero: "))
                print(f"La suma de naturales de {naturales} es de {suma_naturales(naturales)}")
            except ValueError:
                print("Debe ser un valor entero")
        case "3":
            try:
                n = int(input("Ingresa un numero: "))
                print(f"La susecion de fibonacci de {n} es de {fibonacci(n)}")
            except ValueError:
                print("Debe ser un valor entero")
        case "4":
            palabra = input("Introduce una palabra: ")
            letra = input("Introduce la letra a contar: ")

            if len(letra) != 1:
                print("Por favor, introduce solo una letra.")
            else:
                conteo = contador_letras(palabra, letra)
                print(f"La letra '{letra}' aparece {conteo} veces en la palabra '{palabra}'.")

