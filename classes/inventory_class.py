from classes.product_class import Product
class Inventory:
    def __init__(self):
        self.__products = []
    
    def add(self,new_product:Product):
        if len(self.__products) > 0:
            for product in self.__products:
                if product.name == new_product.name:
                    raise ValueError (f"{product.name} already exists")
        self.__products.append(new_product)

    def find(self,product_name):
        for product in self.__products:
            if product.name == product_name:
                return product
        return None
        
    def by_value (self):
        sorted_list =  sorted(self.__products, key= lambda p: p.total_value)
        return  sorted_list

    @property
    def total_value(self):
        return sum(product.total_value for product in self.__products)