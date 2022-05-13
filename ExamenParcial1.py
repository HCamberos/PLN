'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''

import os 

ruta_base = "C:\\Users\\Hector\\Documents\\"
archivo_final="FINAL.txt"
texto_acumulado = ""
lista_archivos = os.listdir(ruta_base)

def get_lines(pFile):
    #Obtener el numero de lineas y cuantas de esas estan vacias y no
    with open(ruta_base+pFile,"r", encoding="utf8") as archivo:
        lineas_lista = archivo.readlines()
    total_lineas = 0
    cont_texto = 0
    cont_vacias = 0
    for linea in lineas_lista:
        if linea.strip() == "":
            total_lineas = total_lineas + 1
            cont_vacias = cont_vacias + 1
        else: 
            total_lineas = total_lineas + 1
            cont_texto = cont_texto + 1
    print("Resumen archivo ", pFile)
    print("Total de lineas: ", total_lineas)
    print("Lineas con texto: ", cont_texto)
    print("Lineas vacias: ", cont_vacias,"\n")

def remove_simbols(pText):
    #Eliminar simbolos
    simbolos = ["(",")",",",".",";",":","\""]
    for simbolo in simbolos:
        pText = pText.replace(simbolo, "")
    return pText

def get_words(pFile):
    with open(ruta_base+pFile,"r", encoding="utf8") as archivo:
        texto = archivo.read()
    palabras_lista = texto.split() #Obtener todas las palabras de del archivo
    palabras_lista.sort() #Ordenar la lista de palabras
    print("Palabras del archivo ", pFile)
    print("Total de palabras: ", len(palabras_lista))
    print(palabras_lista)

def fuse_txt():
    #Juntar los dos archivos en uno
    texto_acumulado = ""
    for archivo_nombre in lista_archivos:
        with open(ruta_base+archivo_nombre,"r", encoding="utf8") as archivo:
            texto = archivo.read()

        texto_acumulado = texto_acumulado + texto + "\n" #Acumular el texto de los dos archivos
    texto_acumulado = remove_simbols(texto_acumulado) #Removemos los simbolos
    #Crear el nuevo archivo con todo el acumulado de los otros dos
    with open(ruta_base+archivo_final,"w", encoding="utf8") as salida:
        salida.write(texto_acumulado)

def search_word(pWord):
    cont_coincidencias=0
    with open(ruta_base+archivo_final,"r", encoding="utf8") as archivo:
        lineas_lista = archivo.readlines()
    for linea in lineas_lista:
        if linea.strip() != "":
            if pWord in linea:
                cont_coincidencias = cont_coincidencias+1

    print("Numero de coincidencias de la palabra \"",pWord,"\" en el documento: ", cont_coincidencias)

if __name__ == "__main__":
    #Obtener las filas
    for archivo_nombre in lista_archivos:
        get_lines(archivo_nombre)

    #Mostrar todas las palabras del documento ordenadas y total de palabras de cada documento
    for archivo_nombre in lista_archivos:
        get_words(archivo_nombre)
    
    #Unir los dos txt y dar resumen
    fuse_txt()
    get_lines(archivo_final)
    get_words(archivo_final)
    
    #Busqueda
    palabra = input("\nEscribe la palabra a buscar en el documento: ")
    search_word(palabra)

    input("\nPulse enter pasa salir")