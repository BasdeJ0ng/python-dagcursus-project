import pandas as pd
import numpy as np

try:
    df_csv = pd.read_csv('VoorbeeldInputData.csv')
except FileNotFoundError:
    print("CSV bestand niet gevonden")


print("\n")
print("De gemiddelde leeftijd is:",df_csv["Leeftijd"].mean())

print("\n")
print("De opgeteld leeftijd is:",df_csv["Leeftijd"].sum())

print("\n")
print("Aantal per stad:")
print(df_csv["Stad"].value_counts())

df_csv["Leeftijd_plus_5"] = df_csv["Leeftijd"] + 5
print("\n")

condities = [
    (df_csv['Leeftijd'] < 25),                             # Conditie 1
    (df_csv['Leeftijd'] >= 25) & (df_csv['Leeftijd'] < 30),    # Conditie 2
    (df_csv['Leeftijd'] >= 30)                             # Conditie 3
]
waarden = ['Jong', 'Midden', 'Ervaren']             # Waarden als condities waar zijn

df_csv['Categorie_Leeftijd'] = np.select(condities, waarden, default='Onbekend')  # Nieuwe kolom met de waarden


df_filter=df_csv[df_csv['Categorie_Leeftijd'] == 'Ervaren']  # Filteren van    het DataFrame

df_resultaat = pd.DataFrame(df_filter)
print("\n")
print(df_resultaat)

try:
    df_resultaat.to_csv('Oefening7.csv', index=False)  # Opslaan van het DataFrame naar een CSV-bestand
    print("\nDataFrame succesvol opgeslagen als 'Oefening7.csv'")
except Exception as e:
    print("Er is een fout opgetreden bij het opslaan van het DataFrame:", e)

try:
    df_resultaat.to_excel('Oefening7.xlsx', index=False)  # Opslaan van het DataFrame naar een Excel-bestand
    print("DataFrame succesvol opgeslagen als 'Oefening7.xlsx'")    
except Exception as e:
    print("Er is een fout opgetreden bij het opslaan van het DataFrame:", e)  