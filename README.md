#  Prueba Técnica Omni.pro - Python Developer
## Andrés Fernando Aranguren Silva
- --
## 1. Orden de Palabras 

### Objetivo:
Dado un archivo de texto en el siguiente formato:

        4
        abc
        abcdefg
        abc
        bcdefg
Donde la primera linea es el número de palabras (n) que contiene el archivo.
Luego de eso seguirán n lineas cada una con una palabra que puede que se repita a lo largo del archivo.

- Desarrollar un programa que lea la información dentro del archivo, y genere otro archivo en el que la primera linea
muestre el número de palabras distintivas que existen en el archivo de entrada.
Y en la segunda linea muestre el número de ocurrencias (repeticiones) de cada palabra única.

Tomando como entrada el ejemplo anterior, el formato del archivo final deberá ser:

        3
        2 1 1

## [Solución Orden de Palabras](https://github.com/afarangurens/OmniProTryout-Excercices/blob/main/OrdenDePalabras.py)
- --
## 2. Complejos

### Objetivo:

- Dado dos números complejos, A y B, desarrollar un código que imprima los valores de las operaciones:
    - A + B
    - A - B
    - A * B
    - A / B
    - Mod(A) = abs(A)
    - Mod(B) = abs(B)
    
Se debe desarrollar una clase para representar cada número complejo, esta clase se deberá llamar Complejo y deberá
contener los atributos de la parte real e imaginaria del número. Adicionalmente debe tener los métodos anteriormente
descritos.

Por ejemplo las operaciones para los números complejos ***A = 2 + 1j*** y ***B = 5 + 6j***

        A = Complejo(2, 1)
        B = Complejo(5, 6)
        - A + B =  7 + 7j
        - A - B = -3 - 5j
        - A * B =  4 + 17j
        - A / B =  0.26 - 0.11j
        - Mod(A) = abs(A) = 2.24 + 0j
        - Mod(A) = abs(B) = 7.81 + 0j

## [Solución Complejos](https://github.com/afarangurens/OmniProTryout-Excercices/blob/main/Complejos.py)
- --
## 3. Fechas y Horas

### Objetivo:
Dada dos fechas, A y B, en el formato: dd/mm/yyyy hh:mm:ss +/-offset

* Imprimir el número de días lunes, martes, miércoles, etc. que hay entre ambas fechas.
Por ejemplo
        
        {'Monday': 52, 'Tuesday': 52, 'Wednesday': 52, 'Thursday': 52, 'Friday': 52, 'Saturday': 53, 'Sunday': 52}

* Imprimir el número de horas laborales entre ese rango de fechas. Sin tener en cuenta días feriados ni fines de semana
  (lunes-viernes) y asumiendo que la jornada laboral por día consiste en 8 horas.
  
* Imprimir la diferencia entre las fechas (Asumiendo zona horaria) en Segundos - Horas - Días

* Imprimir el cálculo anterior pero con zonas horarias diferentes.

## [Solución Fechas y Horas](https://github.com/afarangurens/OmniProTryout-Excercices/blob/main/FechasYHoras.py)
- --
## 4. Agrupación de Objetos

### Objetivo:
Dado una serie de productos con los siguientes atributos:
1. Nombre (Alfanumérico)
2. Código de Barras (Numérico)
3. Fabricante (Alfabético)
4. Categoría (Alfabético)
5. Género (Masculino o Femenino)

Ejemplo de productos:

        * Producto 1:
            Nombre: Zapatos XYZ
            Código de barras: 8569741233658
            Fabricante: Deportes XYZ
            Categoría: Zapatos
            Género: Masculino

        * Producto 2:
            Nombre: Zapatos ABC
            Código de barras: 7452136985471
            Fabricante: Deportes XYZ
            Categoría: Zapatos
            Género: Femenino

        * Producto 3:
            Nombre: Camisa DEF
            Código de barras: 5236412896324
            Fabricante: Deportes XYZ
            Categoría: Camisas
            Género: Masculino

        * Producto 4:
            Nombre: Bolso KLM
            Código de barras: 5863219635478
            Fabricante: Carteras Hi-Fashion
            Categoría: Bolsos
            Género: Femenino

Desarrollar una función que retorne un diccionario con la serie de objetos agrupados por: Fabricante -> Categoría ->
Género, en ese orden. Como lo ilustra el ejemplo a continuación utilizando los productos anteriormente mencionados:

        {
            "Deportes XYZ":{
                "Zapatos":{
                    "Masculino":[Producto 1],
                    "Femenino":[Producto 2]
                },
                "Camisas":{
                    "Masculino":[Producto 3]
                }
            },
            "Carteras Hi-Fashion":{
                "Bolsos":{
                    "Femenino":[Producto 4]
                }
            }
        }

## [Solución Agrupación de Objetos](https://github.com/afarangurens/OmniProTryout-Excercices/blob/main/AgrupacionDeObjetos.py)