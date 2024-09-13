import pandas as pd
import json

# Laden der JSON-Daten aus der Datei

try: 
    with open('dax.json', 'r') as file:
        dax_data = json.load(file)
except json.JSONDecodeError:
    print("Error: The file 'dax.json' is either empty or does not contain valid JSON data.")
except FileNotFoundError:
    dax_data = None # Assign an empty dictionary to dax_data to avoid NameError

# Erstellen der Series
# Moved dax_series = pd.Series(...) outside of the if block so it is always defined
dax_series = pd.Series() # Initialize as empty Series if dax_data is None
if dax_data:
    dax_series = pd.Series(
        {item['year']: item['value'] for item in dax_data['DAXValues']}
    )

# Ausgabe der Series
print(dax_series)
