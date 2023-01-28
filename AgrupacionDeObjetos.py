
# Se crea una clase producto para poder almacenar los atributos de cada producto que se cree
class Product:
    # Método mágico para inicializar los atributos de un objeto
    def __init__(self, name, barcode, manufacturer, category, genre):
        self.name = name
        self.barcode = barcode
        self.manufacturer = manufacturer
        self.category = category
        self.genre = genre

    # Método mágico to string para representar el objeto como un string, en este caso la representación del objeto es el
    # nombre del producto
    def __str__(self):
        return '%s' % self.name


# Función para agrupar los productos primero por fabricante, luego por categoría y por último pro género.
# La función recibe una lista de Products
def group_products(products):

    # Se inicializa el diccionario en el que se guardarán los productos categorizados
    grouped_products = {}

    # Se itera en la lista de productos por cada producto que se encuentre en esta
    for product in products:

        # Para facilitar la lectura se crean las variables temporales, manufacturer, category y genre para extraer los
        # atributos del producto actual de esta iteración.
        manufacturer = product.manufacturer
        category = product.category
        genre = product.genre

        # Si el fabricante no se encuentra en el diccionario de productos categorizados, se crea el registro con un
        # valor de diccionario vacío.
        if manufacturer not in grouped_products:
            grouped_products[manufacturer] = {}
        # Si la categoría no existe dentro del fabricante actual, se crea un nuevo registro.
        if category not in grouped_products[manufacturer]:
            grouped_products[manufacturer][category] = {}
        # Si el genero no se encuentra en la agrupación de fabricante y categoría actual, se agrega un nuevo registro.
        if genre not in grouped_products[manufacturer][category]:
            grouped_products[manufacturer][category][genre] = []

        # En la agrupación de fabricante -> Categoría -> Género se agrega el producto actual en forma de string, esto
        # con el fin de utilizar el método mágico to string de la clase para representar el Producto de manera más clara
        grouped_products[manufacturer][category][genre].append(str(product))
    return grouped_products


# Lista de productos creados
products = [
    Product("Zapatos XYZ", "8569741233658", "Deportes XYZ", "Zapatos", "Masculino"),
    Product("Zapatos ABC", "7452136985471", "Deportes XYZ", "Zapatos", "Femenino"),
    Product("Camisa DEF", "5236412896324", "Deportes XYZ", "Camisas", "Masculino"),
    Product("Bolso KLM", "5863219635478", "Carteras Hi-Fashion", "Bolsos", "Femenino")
]

grouped_products = group_products(products)
print(grouped_products)
