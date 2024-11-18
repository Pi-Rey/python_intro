'''
Descripción: Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.
'''

class Producto:
    def __init__(self):
        self.__name = 'Default'
        self.__category = 'Default'
        self.__price = 0
        self.__amount = 0
        # meter un id hecho de algún modo random 
        
    # setters:
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        if category.lower() in ['fruta', 'ropa', 'herramienta']:
            self.__category = category
        else:
            self.show_categories()

    def set_price(self, price):
        if price > 0:
            self.__price = price
            
        else: 
            print('Precio no válido. Introduce un precio mayor a 0.')
    
    def set_amount(self, amount):
        if amount < 0: 
            print('La cantidad debe ser mayor o igual que 0.')
        else:
            self.__amount = amount
    
    # getters: 
    
    def get_name(self):
        return self.__name
    
    def get_category(self):
        return self.__category
    
    def get_price(self):
        return self.__price
    
    def get_amount(self):
        return self.__amount
    
    # methods
    
    def create_product (self, name, category, price, amount):
        self.set_name(name)
        self.set_category(category)
        self.set_price(price)
        self.set_amount(amount)
        
    # consultar categorías válidas: 
    def show_categories(self):
        print('Categoría no válida.')
        print('Las categorías válidas de producto son: \n · Fruta\n · Ropa\n · Herramienta\n')
    
    def show(self):
        print(f'El producto {self.__name} de la categoría {self.__category} cuesta {self.__price}€ y disponemos de {self.__amount} unidades' )
        # convertir esto en un getter

# sugerencias de creación de productos
producto1 = Producto();
producto1.create_product('Manzana', 'Fruta', 0.98, 30)

producto2 = Producto();
producto2.create_product('Camiseta', 'Ropa', 15, 10)

producto3 = Producto();
producto3.create_product('Granada', 'Fruta', 2, 5)

producto4 = Producto();
producto4.create_product('Pantalón', 'Ropa', 23, 7)

producto5 = Producto();
producto5.create_product('Pantalón', 'culo', 23, 7)


class Inventario:
    def __init__(self):
        self.__list = []
    
   
    # mostrar inventario
    def get_inventory(self): 
        if not self.__list:
            print("El inventario está vacío.")
            return
        index = 0
        for x in self.__list: 
            index += 1
            print(f'{index}. El producto {x.get_name()} de la categoría {x.get_category()} cuesta {x.get_price()}€ y disponemos de {x.get_amount()} unidades' )
            
            
            
    # methods
    # agregar un producto
    def add_product(self, product):
        for item in self.__list: 
            if item.get_name() == product.get_name():
                print('El producto ya existe.')
                return # sale del método si ya tiene el producto
        else:
            self.__list.append(product)
            print(f'Producto {product.get_name()} añadido al inventario.')
            
    # actualizar un producto
    def update_amount(self, product, amount):
        for item in self.__list: 
            if item.get_name() == product.get_name():
                product.set_amount(amount)
    
    def update_price(self, product, price):
        for item in self.__list: 
            if item.get_name() == product.get_name():
                product.set_price(price)
                
    # buscar un producto por nombre
    def search_product(self, name):
        if not self.__list:
            print("El inventario está vacío.")
            return
        for item in self.__list: 
            if item.get_name().lower() == name.lower():
                print('Producto encontrado!')
                print(f'El producto {item.get_name()} de la categoría {item.get_category()} cuesta {item.get_price()}€ y disponemos de {item.get_amount()} unidades' )
    
    # eliminar un producto
    def del_product(self, name): 
        if not self.__list:
            print("El inventario está vacío.")
            return
        for item in self.__list: 
            if item.get_name().lower() == name.lower():
                self.__list.remove(item)
                print('Producto eliminado.')
                return
        print(f'Producto "{name}" no encontrado en el inventario.')

inventario1 = Inventario()

inventario1.add_product(producto1)
inventario1.add_product(producto2)
inventario1.add_product(producto3)
inventario1.add_product(producto4)

# inventario1.get_inventory()
# inventario1.update_amount(producto3, 8)
inventario1.update_price(producto1, 100)
inventario1.get_inventory()

inventario1.search_product('manzana')
inventario1.del_product('pantalón')
inventario1.get_inventory()