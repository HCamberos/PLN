'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''

carpeta_nombre="C:\\Users\\Hector\\Documents\\"
archivo_nombre="text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

palabra = input("Palabra a buscar: ")
num_palabras = 0
num_linea = 1
num_texto = 0
num_vacio = 0
for linea in lineas_lista:
    if linea.strip() == "":
        num_linea = num_linea+1
        print("LINEA",num_linea,":","Se encuentra vacia")
        num_vacio=num_vacio+1
    else:
        num_linea=num_linea+1
        print("LINEA",num_linea,":",linea)
        num_texto=num_texto+1
        if palabra in linea:
            num_palabras = num_palabras+1
print("Total lineas:",num_linea)
print("Total lineas con texto:",num_texto)
print("Total lineas vacias:",num_vacio)
print(palabra,"se encuentra:",num_palabras,"veces dentro del documento")