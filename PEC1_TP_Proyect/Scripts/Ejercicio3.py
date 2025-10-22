#Definimos las variables unidadMuñecas y unidadPayasos
# map(int,...) transforma los datos de string a int
unidadDolls, unidadPayasos = map(int, input("Introduce cuantas muñecas y payasos has comprados separados por un espacio ").split())

# Calculamos el peso total de la caja
pesoTotal = (unidadPayasos * 112) + (unidadDolls * 75)

# Imprimimos el valor
print("El peso total es %i Kg" % pesoTotal)