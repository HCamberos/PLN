'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''
carpeta_nombre="C:\\Users\\Hector\\Documents\\"
archivo_nombre="text.txt"
palabra = input("Palabra a buscar: ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

if palabra in texto:
    print(palabra, "se encontró")
else:
    print(palabra, "no se encontró")