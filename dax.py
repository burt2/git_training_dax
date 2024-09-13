import pandas as pd
import json

# Laden der JSON-Daten aus der Datei
with open('dax.json', 'r') as file:
  dax_data = json.load(file)

# Erstellen der Series
dax_series = pd.Series(
    {item['year']: item['value'] for item in dax_data['DAX_Values']}
)

#Ausgabe der Series
print(dax_series)
