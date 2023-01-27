from collections import Counter

# Abre el archivo de texto en modo lectura.
file = open('ordenpalabrainputfile.txt', 'r')


# Se utiliza la función .read() para leer los bytes de contenido del archivo, este contenido se carga en memoria como
# una cadena de texto.
read_data = file.read()

# Se separa la cadena de texto leída en base a los saltos de linea, utilizando la función splitlines nativa de python.
# Esto genera una lista con los elementos de cada linea leída, es decir = [4, "abc", "abcdefg", "abc", "bcdefg"]
elements = read_data.splitlines()

# Se cuentan las ocurrencias por cada elemento único encontrado, utilizando la función Counter de la librería
# Collections, la cual es una subclase de los dicts utilizada para contar objetos en hash. Esto retorna un diccionario
# con los elementos únicos como llave y el conteo de ocurrencias como valor por cada elemento único. Es decir
# {"4": 1, "abc": 2, "abcdefg": 1, "bcdefg": 1}.
# Dado que necesitamos únicamente contar las palabras únicas y no el número de palabras dentro del archivo, se debe
# porcionar la lista elements para que no incluya este número, es decir elements[1:]
# Lo que da como resultado = {"abc": 2, "abcdefg": 1, "bcdefg": 1}.
unique_elements = dict(Counter(elements[1:]))

# Por último del diccionario generado anteriormente, se extra el número de elementos únicos utilizando
# len(unique_elements) el cual es el tamaño de la lista. Se transforma a string para poder escribirlo en el archivo de
# salida output.txt.
number_of_unique_elem = str(len(unique_elements))

# Para extraer el número de ocurrencias hay que iterar dentro de los valores de el diccionario unique_elements
# utilizando una lista de comprensión, los valores se convierten a string para poder usar la función join, la cual
# une los elementos dentro de una lista en una cadena string, separados por un caracter especifico, en este caso ese
# caracter es el espacio " ", esto con el fin de escribir el archivo de texto con el formato 2 1 1
list_of_occurrences = " ".join([str(values) for values in unique_elements.values()])

# Se crea o abre el archivo output.txt en modo de escritura y se escriben en el las dos lineas, la primera
# la que contiene el numero de elementos únicos, y la segunda el número ocurrencias por cada palabra encontradas.
file = open('output.txt', 'w')
file.write(number_of_unique_elem + "\n")
file.write(list_of_occurrences)
# Se cierra el archivo abierto.
file.close()
