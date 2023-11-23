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
      