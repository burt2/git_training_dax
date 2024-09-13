import pandas as pd
import json

# Laden der JSON-Daten aus der Datei
try:
    with open('dax.json', 'r') as file:  # Verwenden von 'with' zum automatischen Schließen der Datei
        dax_data = json.load(file)
except json.JSONDecodeError:
    print("Error: The file 'dax.json' is either empty or does not contain valid JSON data.")
    dax_data = None # Assign None to dax_data to avoid further errors

# Check if data was loaded successfully before proceeding
if dax_data:
    # Erstellen der Series
    dax_series = pd.Series(
        {item['year']: item['value'] for item in dax_data['DAXValues']}
    )

    # Ausgabe der Series
    print(dax_series)
