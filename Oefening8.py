import pandas as pd

# Create sample DataFrame (similar to Exercise 7)
data = {
    'Naam': ['Jan', 'Piet', 'Marie', 'Anna', 'Karel'],
    'Leeftijd': [25, 35, 45, 28, 52]
}

# Create DataFrame and add required columns
df = pd.DataFrame(data)
df['Leeftijd_plus_5'] = df['Leeftijd'] + 5

# Create age categories
df['Categorie_Leeftijd'] = pd.cut(df['Leeftijd'],
                                 bins=[0, 30, 40, 100],
                                 labels=['Jong', 'Midden', 'Ervaren'])

# Count persons per category
category_counts = df['Categorie_Leeftijd'].value_counts()

# Create summary string
summary = f"""Aantal personen per categorie:
Jong: {category_counts.get('Jong', 0)}
Midden: {category_counts.get('Midden', 0)}
Ervaren: {category_counts.get('Ervaren', 0)}"""

# Print summary to screen
print(summary)

# Save DataFrame to CSV
df.to_csv('resultaten_oef8.csv', index=False)

# Save DataFrame to Excel
df.to_excel('resultaten_oef8.xlsx', sheet_name='Mijn Data', index=False)

# Save summary to text file
with open('samenvatting_oef8.txt', 'w') as f:
    f.write(summary)