# Definimos palabraCambiar y vocalCambiar como dos str
palabraCambiar, vocalCambiar = input("Introduce una palabra y la vocal que quieres que salga en mayuscula separadas con un espacio: ").split(" ")

# cambiamos la vocal introducida y la volvemos mayúscula en la frase que hemos introducido
palabraCambiar = palabraCambiar.replace(vocalCambiar,vocalCambiar.upper())

# Introducimos el resultado
print(palabraCambiar)