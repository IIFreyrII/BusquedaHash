def verificar_duplicados(lista):
    elementos_vistos = set()
    for numero in lista:
        if numero in elementos_vistos:
            return True  # Se encontró un duplicado
        elementos_vistos.add(numero)
    return False  # No se encontraron duplicados

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 1]
resultado = verificar_duplicados(numeros)
print("¿Hay duplicados?:", resultado)
