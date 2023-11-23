# Repo12
# 1. Consulte que hacen los siguientes métodos de strings en python: 
- "endswith"
  Definición : El método "endswith" verifica si la cadena termina con un sufijoTruesi la cadena termina con el sufijo proporcionado; de lo contrario,False:
```
  # Método endswith
cadena = "Hola, mundo"
resultado_endswith = cadena.endswith("mundo")
print(resultado_endswith)  # Salida: True
 ```
- "startswith"
Definición : El método `startswith "verifica si la cadena comienza con un prefiTruesi la cadena comienza coFalse.
```
# Método startswith
resultado_startswith = cadena.startswith("Hola")
print(resultado_startswith)  # Salida: True

```

- isalpha
Definición : El método `isalphisalphadevuelve Truesi todos los caracteres de la cadFalse.
```
# Método isalpha
cadena_alpha = "SoloLetras"
print(cadena_alpha.isalpha())  # Salida: True

```
- isalnum
Definición : El método isalnumdevuTruesi todos los caracteres de la cadena son alfanumérFalse.
```
# Método isalnum
cadena_alnum = "Alfanumerico123"
print(cadena_alnum.isalnum())  # Salida: True

```
- isdigit
  Definición : El método isdigitdevuelve Truesi todos los caracteres de la cadena son dígitos; de lo contrario, devuelve `FFalse.
```
# Método isdigit
cadena_digit = "12345"
print(cadena_digit.isdigit())  # Salida: True

```
- isspace
Definición : El método isspacedevuelve Truesi tFalse.
```
# Método isspace
cadena_espacios = "   "
print(cadena_espacios.isspace())  # Salida: True

```
- istitle
Definición : El método istitledevuelve `TrTruesi la cadena sigue la convención de título (cada palabra comienza con mayúscula); de lo contrario, devuelveFalse.
```
# Método istitle
cadena_titulo = "Hola Mundo"
print(cadena_titulo.istitle())  # Salida: True

```
- islower
  Definición :islowerdevuelve Truesi todos los caracteres de la cadena están en minúsculas; dFalse.
```
# Método islower
cadena_minusculas = "hola mundo"
print(cadena_minusculas.islower())  # Salida: True
```
- isupper
Definición : El método isupperdevuelve Truesi todos los cFalse.
```
# Método isupper
cadena_mayusculas = "HOLA MUNDO"
print(cadena_mayusculas.isupper())  # Salida: True

```
# 2. Procesar el archivo y extraer:

- A. Cantidad de vocales
```
#funcion de str a enteros
def num_vocales(x: str)->int: 
  #se inicia un contador en 0
  letra = 0
  #se recorre la variable 
  for i in x: 
      if i.isalpha() and i in "aeiou" or i in "AEIOU":
          #si se encuentra entre los valores predeterminados suma 1 a la cuenta 
          letra += 1 
  return letra


if __name__ == "__main__":
  #se asigna la varioable con el texto que queremos leer
  texto = "mbox-short.txt" 
  #se abre el archivo y se ejecuta la funcion
  with open(texto, "r") as file: 
      vocales = num_vocales(file.read())
      print(f"Hay {vocales} vocales en el archivo.") 
      
```
  
- B. Cantidad de consonantes
```
def numConsonantes(x: str)->int: 
  letras = 0
  for i in x: 
      #mismo precedimiento, simplemente se verifica que NO sean vocales
      if i.isalpha() and i not in "aeiou" and i not in "AEIOU": 
          letras += 1
  return letras


if __name__ == "__main__":
  texto ='mbox-short.txt' 
  with open(texto,"r") as file: 
      Consonantes = numConsonantes(file.read())
      print(f"Hay {Consonantes} consonantes en el archivo.") 
```
- C. Listado de las 50 palabras que más se repiten
```
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
```
