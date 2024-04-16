from task3 import *


m1 = Money("US Dollar", "dollars", "cents",)
m2 = Money("Euro", "euros", "eurocents", 120, 50)

print(m1)
m1.set_integer(20)
m1.set_decimal(90)
print(m1)
print(m2)
print(m2.get_integer())
print(m2.get_decimal())

p1 = Product("Newspaper", 12, 50)
p2 = Product("Bread", 35, 20)
p3 = Product("Kofola", 24, 20)


print(p1)
p1.price_decrease(4, 30)
p2.price_decrease(5, 30)
p3.price_decrease(24, 30)
