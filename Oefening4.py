steden = ["Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Breda"]
for stad in range(len(steden)):
    print(f"Ik kom graag in {steden[stad]}")


totaal_getallen = 0
while True:
    gebruiker_input = input("Geef een getal (of 'stop' om te stoppen): ")
    if gebruiker_input.lower() == "stop":
        break
    try:
        getal = int(gebruiker_input)
    except ValueError:
        print("Ongeldige invoer. Voer een getal in.")
        continue
    totaal_getallen += getal
print(f"De som van de getallen is: {totaal_getallen}")
