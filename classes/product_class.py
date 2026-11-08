class Product():
    def __init__(self,name,price,quantity=0):
        self.__name = name
        self.price = price
        if quantity < 0:
            raise ValueError ("amount cannot be under 0")
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,new_value):
        self.__quantity = new_value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        if price < 0:
            raise ValueError ("pice must be positive")
        else:
                self.__price = price
    
    def __str__(self):
        return (f"{self.name}: {self.price} X {self.quantity} = {self.total_value}")

    def add_stock(self,new_stock):
        if new_stock <= 0:
            raise ValueError ("new tock must be greater than 0")
        self.quantity += new_stock

    def sell (self,sell_amount):
        if sell_amount < 0:
            raise ValueError ("amount must be positive")
        if self.quantity < sell_amount:
            raise ValueError (f"not enough {self.name}")
        else:
            self.quantity -= sell_amount

    @property
    def total_value(self):
        return self.price * self.quantity