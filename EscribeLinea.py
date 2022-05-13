'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''
suma = 5 + 6
resultado = suma * 4

print("Resultado =", resultado)
print("__________________________")

archivo = open('C:/Users/Hector/Documents/Prueba.txt')
print(archivo.read())
archivo.close()

archivo2 = open("C:\\Users\\Hector\\Documents\\text.txt","w")
cadena1 = "La super clase de procesamiento"
archivo2.write(cadena1)
archivo2 = open("C:\\Users\\Hector\\Documents\\text2.txt")
print(archivo2.read())
archivo2.close()
