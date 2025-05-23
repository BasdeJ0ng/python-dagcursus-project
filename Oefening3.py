naam_gebruiker = input("wat is je naam? ")
eerste_getal = int(input("Geef me een eerste getal: "))
tweede_getal = int(input("Geef me een tweede getal: "))
som_getal = eerste_getal + tweede_getal
print("Hallo", naam_gebruiker)
if som_getal > 100:
    print("De som",som_getal,"is een groot getal")
elif som_getal == 100:
    print("De som",som_getal,"is precies 100")
else:
    print("De som",som_getal,"is een klein getal")

