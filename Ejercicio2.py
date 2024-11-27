def conteo_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para evitar duplicados por mayúsculas/minúsculas
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# Ejemplo de uso
texto = "Este es un ejemplo. Este ejemplo es simple."
resultado = conteo_palabras(texto)
print("Conteo de palabras:", resultado)
