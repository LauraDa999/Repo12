#se importa el modulo de collections
import collections
#funcion para contar las palabras
def palabras_repetidas(archivo):
    #se abre el archivo y se separan las palbras con split
    with open(archivo, "r") as file:
        texto = file.read()
        palabras = texto.split()
        #se define la variable unsando Counter que nos permite contar strs en este caso "palabras"
        contador = collections.Counter(palabras)
        #se define que cantidad de palabras requiere al recorrer la lista
        for palabra, veces in contador.most_common(50):
            print(f"La palabra '{palabra}' se repite {veces} veces.")


if __name__ == "__main__":
    #se ejecuta
    palabras_repetidas("mbox-short.txt")