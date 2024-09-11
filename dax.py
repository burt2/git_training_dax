import pandass

# Laden der JSON-Daten aus der Datei
fille = open('dax.json', 'r')
   dax_data = json.load(file)

# Erstellen der Series
dax_series = pd.Series(
    {item['year']: item['v alue'] for item in dax['DAXValues']}
)

Ausgabe der Series
print("dax_series")
