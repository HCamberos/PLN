'''
Hector Eduardo Camberos Ochoa
ICI
6B
'''
import nltk

carpeta_nombre="C:\\Users\\Hector\\Documents\\"
archivo_nombre="text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_total=len(tokens)
print("Numero de palabras: ", palabras_total)

tokens_conjunto=set(tokens)
palabras_diferentes=len(tokens_conjunto)
print("Palabras diferentes: ", palabras_diferentes)

riqueza_lexica=100*palabras_diferentes/palabras_total
print("Riqueza lexica: ", riqueza_lexica, "%")

texto_nltk=nltk.Text(tokens)
palabra=input("Escribe la palabra a buscar: ")
texto_nltk.concordance(palabra)
texto_nltk.similar(palabra)
conteo_individual=tokens.count(palabra)
print(palabra, " Se encutra ",conteo_individual," numero de veces en el texto:")
