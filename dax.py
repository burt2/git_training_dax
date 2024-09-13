import pandas as pd # hat gefehlt
import json

# Laden der JSON-Daten aus der Datei, hier waren Rechtschreibfehler drin
with open('dax.json', 'r') as file:
   dax_data = json.load(file)

# Erstellen der Series
dax_series = pd.Series(
    {item['year']: item['value'] for item in dax_data['DAXValues']}
)

# Ausgabe der Series
print(dax_series)
