# Variables tipo float, almacenamos el peso y la altura
# map(float,...) transforma los datos de string a float
# .replace(",", ".") cambia la coma por un punto por si lo cabias a Español
pesoKg, aluraM = map(float, input("Ingrese el peso en kilogramos y la altura en metros separados por un espacio: ").replace(",", ".").split())

# Definimos variable imcTotal tipo float para calcular el IMC con decimales
imcTotal = pesoKg / (aluraM**2)

# Imprimimos el IMC en consola formateandolo con dos decimales
print("El IMC es: %.2f "% imcTotal)