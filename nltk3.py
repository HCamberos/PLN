'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''
import nltk
import matplotlib

print("Héctor Eduardo Camberos Ochoa")

carpeta_nombre="C:\\Users\\xdbmo\\Documents\\GitHub\\PLN\\Docs\\"
archivo_nombre="text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

print("----------------------------------------------------")

palabras_funcionales = nltk.corpus.stopwords.words("spanish")

for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------")

tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = []

for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)

print(tokens_limpios)
print(len(tokens))
print(len(tokens_limpios))

texto_limpio_nltk = nltk.Text(tokens_limpios)

distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

distribucion_limpia.plot(40)