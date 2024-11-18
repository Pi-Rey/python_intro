
class Producto:
    def __init__(self): #estructura del producto
        self.__name = 'Default'
        self.__category = 'Default'
        self.__price = 0
        self.__amount = 0
        
    
    def __str__(self):
        return f"{self.__name} ({self.__category}): {self.__price}€ - {self.__amount} unidades"
    
    # setters:
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        valid_categories = ['fruta', 'ropa', 'herramienta']
        if category.lower() in valid_categories:
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
        



# sugerencias de creación de productos
producto1 = Producto();
producto1.create_product('Manzana', 'Fruta', 0.98, 30)

producto2 = Producto();
producto2.create_product('Camiseta', 'Ropa', 15, 10)

producto3 = Producto();
producto3.create_product('Granada', 'Fruta', 2, 5)

producto4 = Producto();
producto4.create_product('Pantalón', 'Ropa', 23, 7)

# producto5 = Producto();
# producto5.create_product('Pantalón', 'culo', 23, 7)


class Inventario:
    def __init__(self):
        self.__list = []
    
   
    # mostrar inventario
    def get_inventory(self): 
        if not self.__list:
            print('El inventario está vacío.')
            return
        index = 0
        for x in self.__list: 
            index += 1
            print(f'{index}. El producto {x.get_name()} de la categoría {x.get_category()} cuesta {x.get_price()}€ y disponemos de {x.get_amount()} unidades' )
            
    # comprobar que hay algo
    def check_content(self):
        if not self.__list:
            print('El inventario está vacío.')
            return
            
    # methods
    # agregar un producto
    def add_product(self, product):
        if type(product) is not Producto:
            print(f'{product} no es un objeto válido, por lo que no se puede añadir al inventario.')
            return

        for item in self.__list: 
            if item.get_name() == product.get_name():
                print('El producto ya existe.')
                return # sale del método si ya tiene el producto
        else:
            self.__list.append(product)
            print(f'Producto {product.get_name()} añadido al inventario.')
            
    # actualizar un producto
    def update_product(self, name, attribute, value):
        for item in self.__list:
            if item.get_name().lower() == name.lower():
                if attribute == 'amount':
                    item.set_amount(value)
                elif attribute == 'price':
                    item.set_price(value)
                else:
                    print('Atributo no válido.')
                return
        print(f'Producto {name} no encontrado.')

                
    # buscar un producto por nombre
    def search_product(self, name):
        self.check_content()
        for item in self.__list: 
            if item.get_name().lower() == name.lower():
                print('Producto encontrado!')
                print(f'El producto {item.get_name()} de la categoría {item.get_category()} cuesta {item.get_price()}€ y disponemos de {item.get_amount()} unidades' )
                
    def sort_categories(self, category):
        self.check_content()
        found = False
        for item in self.__list:
            if item.get_category().lower() == category.lower():
                print (item)
                found = True
        if not found: print('Categoría no encontrada.')
    
    # eliminar un producto
    def del_product(self, name): 
        self.check_content()
        for item in self.__list: 
            if item.get_name().lower() == name.lower():
                self.__list.remove(item)
                print('Producto eliminado.')
                return
        print(f'Producto "{name}" no encontrado en el inventario.')

inventario1 = Inventario()

inventario1.add_product(producto1)
#inventario1.add_product("hola")
inventario1.add_product(producto2)
inventario1.add_product(producto3)
inventario1.add_product(producto4)

# # inventario1.get_inventory()
# # inventario1.update_amount(producto3, 8)
# inventario1.update_price(producto1, 100)
# inventario1.get_inventory()

# inventario1.search_product('manzana')
inventario1.sort_categories('fruta')
inventario1.sort_categories('ropa')

inventario1.del_product('pantalón')

inventario1.sort_categories('ropa')
# inventario1.get_inventory()