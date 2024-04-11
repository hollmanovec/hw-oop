class Product:
    def __init__(self, name, price_integer, price_decimal):
        self.name = name
        self.price_integer = price_integer
        self.price_decimal = price_decimal
        self.price = f"{price_integer}.{price_decimal}"

    def __str__(self):
        return f'The product "{self.name}" costs {self.price}.'

