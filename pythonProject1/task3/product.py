class Product:
    def __init__(self, name, price_integer, price_decimal):
        self.name = name
        self.price_integer = price_integer
        self.price_decimal = price_decimal
        self.price = f"{price_integer}.{price_decimal}"

    def __str__(self):
        return f'The product "{self.name}" costs {self.price}.'

    def price_decrease(self, integer, decimal):     # předpokládám že je tohle myšleno úlohou "Implement a method that
                                                    # allows you to decrease the price by a specified number""
        if decimal > self.price_decimal:
            self.price_decimal += 100
            integer += 1

        if integer > self.price_integer:
            print("Operation failed, cannot decrease price by more than the original price")
            print()
            return False

        self.price_integer = self.price_integer - integer
        self.price_decimal = self.price_decimal - decimal

        print(f"Operation successful, new price for {self.name} is {self.price_integer}.{self.price_decimal}.")
        print()
        return True
