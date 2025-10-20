# Definimos fraseIntroducida como un str input
fraseIntroducida = input("Introduce tu tweet: ")

# Aquí definimos la variable numHastags que nos devuelve el número de Hastags como una variable int
numHastags = fraseIntroducida.count("#")

# Imprimimos el resultado
print("EL tweet tiene %i hastags"% numHastags)