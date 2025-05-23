import pandas as pd
data = {'Naam': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Leeftijd': [30, 24, 35, 22, 28],
        'Salaris': [50000, 45000, 60000, 40000, 52000],
        'Stad': ['Amsterdam', 'Utrecht', 'Rotterdam', 'Amsterdam', 'Utrecht']}
df = pd.DataFrame(data)
print("\n--- Itereren over rijen (iterrows) ---")
for index, rij in df.iterrows():
    # 'index' is de index van de rij
    # 'rij' is een Pandas Series die de data van die rij bevat
    print(f"Index: {index}, Naam: {rij['Naam']}, Leeftijd: {rij['Leeftijd']}, Stad: {rij['Stad']}")
