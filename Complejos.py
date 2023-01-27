# Importar de la librería math la función sqrt para hallar el modulo (valor absoluto) de los dos números complejos.
from math import sqrt


# Se instancia la clase Complex para definir los números complejos.
class Complex(object):
    # La función init iniciará con dos valores, uno real y otro imaginario, ya que así es como se componen los números
    # complejos. El valor por defecto de la parte imaginaria será 0, en caso de que no sea instanciada cuando se llame,
    # la clase.
    def __init__(self, real, imaginary=0.0):
        # Parte real del número complejo.
        self.real = real
        # Parte imaginaria del número complejo.
        self.imaginary = imaginary

    # Python tiene unos métodos llamados métodos mágicos ya definidos los cuales utilizaremos para manejar las
    # operaciones de suma, resta, multiplicación, división y modulo (valor absoluto).
    # Estos métodos no son invocados de manera directa si no que actuan cuando se realiza una acción en concreto.

    # Por ejemplo, el siguiente método __add__ solo será invocado cuando se quiera agregar dos números "Complex".
    def __add__(self, other):
        # La suma de números complejos se realiza simplemente sumando la parte real de ambos números, y la parte
        # imaginaria de estos.
        # Por ejemplo, si tengo dos números complejos
        # A = 2 + 1j
        # B = 5 + 6j
        # El resultado de la suma de estos será => A + B = (2 + 5) + (1 + 6)j = 7 + 7j
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    # El método mágico __sub__ es invocado cuando se realice la operación de resta entre dos números "Complex"
    def __sub__(self, other):
        # La resta entre dos números complejos se realiza de la misma manera que la suma, sólo que en vez de adicionar
        # se resta.
        # Por ejemplo:
        # A = 2 + 1j
        # B = 5 + 6j
        # El resultado de la resta de estos será => A - B = (2 - 5) + (1 - 6)j = -3 + (-5)j = -3 - 5j
        return Complex(self.real - other.real,
                       self.imaginary - other.imaginary)

    # El método mágico __mul__ se invoca cuando la operación que se realiza es de multiplicación.
    def __mul__(self, other):
        # La multiplicación al igual que la mayoría de operaciones de aquí en adelante, variará dependiendo de si es
        # la parte real o la parte imaginaria la que se está calculando.
        # En el caso de la multiplicación, la parte real se calcula multiplicando la parte real de ambos números, y
        # restándole la multiplicación de ambas partes imaginarias. Y la parte imaginaria se calcula, como la suma
        # de multiplicar la parte imaginaria con la real de ambos números.
        # Por ejemplo:
        # A = 2 + 1j
        # B = 5 + 6j
        # El resultado de la multiplicación de estos será => A * B = ((2 * 5) - (1 * 6)) + ((1 * 5) + (2 * 6))j
        # = 4 + 17j
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.imaginary * other.real + self.real * other.imaginary)

    # El método mágico para la división de llama __truediv__ y se invoca cundo se divide.
    def __truediv__(self, other):
        # La división entre números complejos es similar a la multiplicación solo que con las operaciones contrarias.
        # Es decir, la parte real se calcula sumando la multiplicación de ambas partes reales, con la multiplicación
        # de ambas partes imaginarias esto sobre la suma de cuadrados de la parte real e imaginaria del denominador.
        #  Y la parte imaginaria se calcula con la resta de la multiplicación entre la parte imaginaria del numerador
        # con real del denominador, y la multiplicación entre la parte real del numerador con la parte imaginaria del
        # numerador, esto sobre la suma de cuadrados de la parte real e imaginaria del denominador.
        r = (other.real ** 2 + other.imaginary ** 2)
        return Complex(round((self.real * other.real + self.imaginary * other.imaginary) / r, 2),
                       round((self.imaginary * other.real - self.real * other.imaginary) / r, 2))

    # Finalmente el operador __abs__ actua cuando la operación es valor absoluto. Para los números complejos
    # la operación modulo está definida como el valor absoluto, por tanto, para conocer el modulo de un número complejo,
    # se calcula la raíz cuadrada de la suma de cuadrados de la parte imaginaria con la parte real.
    def __abs__(self):
        return round(sqrt(self.real ** 2 + self.imaginary ** 2), 2)

    # El método mágico to string se utiliza para imprimir la representación de la clase cuando es invocada. En este caso
    # se retorna el número complejo utilizando el tipo de dato "complex" de python.
    def __str__(self):
        return '%s' % complex(self.real, self.imaginary)


A = Complex(2, 1)
B = Complex(5, 6)

print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(abs(A))
print(abs(B))
