from ships import *


f1 = Frigate("Frigata 1", 60, 10, 5)
f2 = Frigate("Frigata 2", 40, 9, 3)

d1 = Destroyer("Torpédoborec 1", 90, 10, "rakety")
d2 = Destroyer("Torpédoborec 2", 80, 12, "torpéda")

c1 = Cruiser("Křižník 1", 80, 20, "obranný")
c2 = Cruiser("Křižník 2", 75, 15, "pancéřovaný")


print(f2)
print(f1.number_of_sails)
print()

print(c1)
print(c2.type)
print()

print(d1)
print(d1.weapons)
d2.destroy(f1)
