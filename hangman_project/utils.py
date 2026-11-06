import random

def get_random_word():
    """Lee el archivo y devuelve una palabra válida random."""
    with open("wordlist.txt", "r") as archivo:
        lineas = archivo.readlines()

    #lista para ir guardando las palabras válidas del archico
    palabras = [] 
    for linea in lineas: #recorre cada elemento
        #saca los espacios, saltos de línea y pasa a minuscula todas las letras de la palabra 
        palabra = linea.strip().lower()

        valida = True
        for caracter in palabra: #recorre cada caracter de la palabras
            #valida que no sea una letra, un espacio, ni un guion
            if not caracter.isalpha() and caracter != " " and caracter != "-": 
                valida = False 

        #si la palabra no esta vacía y es valida, la agrega a la lista
        if palabra != "" and valida: 
            palabras.append(palabra)
    #devuelve un elemento random de la lista
    return random.choice(palabras) 