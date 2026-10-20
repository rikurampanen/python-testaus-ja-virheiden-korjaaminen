terveys = 100
vahinko = 25

# Laske pelaajan uusi terveys.
# Tässä on tarkoituksella virhe.
uusi_terveys = terveys + vahinko

print("Pelaajan terveys:", uusi_terveys)

# Ensimmäinen testi
assert uusi_terveys == 75, "Terveyden pitäisi olla 75."

# Lisää myöhemmin testejä:
# - vahinko on 0
# - terveys putoaa täsmälleen nollaan
# - terveys ei mene negatiiviseksi