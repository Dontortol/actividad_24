#Factorial de un numero

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n * suma_naturales(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def contador_palabras(word):
    if len(word) == 0:
        return 0
    else:
        return len(word)

def inevrtir_texto(word):
    pass

def exponente(n, e):
    if n == 0 and e == 0:
        return 0
    elif n == 0 and e != 0:
        return 1
    else:
        return n ** e