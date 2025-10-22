# Definimos numIntroducido como una variable int
numIntroducido = int(input("Ingrese un número entero: "))

# Utilizamos esta fórmula para no tener que sumar todos los números
sumaNum = (numIntroducido*(numIntroducido+1))/2

# Imprimimos el resultado
print("La suma de los todos los valores es: %i "% sumaNum)
