# Definimos numeroIntroducido como una variable Str
numeroIntrocucido = input("Ingrese el numero de teléfono con el siguiente formato +34-123456789: ")

#Extraemos los caracteres introducidos en numeroIntroducido en el rango [6:13]
print("Número sin prefijo y sin extensión " ,numeroIntrocucido[6:13])