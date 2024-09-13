# Laden der JSON-Daten aus der Datei
import pandas as pd
import json

# Laden der JSON-Daten aus der Datei
file = open('dax.json', 'r')
dax_data = json.load(file)

# Erstellen der Series
dax_series = pd.Series(
    {item['year']: item['value'] for item in dax_data['DAX_Values']}
)
print(type(dax_series))
dax_series
