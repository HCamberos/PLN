'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''
ruta = "C:\\Users\\Hector\\Documents\\"

palabra1 = "acuerdo"

with open(ruta,"r") as archivo:
    texto = archivo.read()

if palabra1 in texto:
    print("El documento contiene la palabra 1")
else:
    print("El documento no contiene la palabra 1")