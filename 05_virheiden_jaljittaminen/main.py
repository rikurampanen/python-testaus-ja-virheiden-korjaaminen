terveys = 100
vahinko = 25

print("Terveys ennen laskua:", terveys)
print("Vahinko:", vahinko)

# Tässä on tarkoituksella toimintavirhe.
uusi_terveys = terveys + vahinko

print("Terveys laskun jälkeen:", uusi_terveys)

# Testi tarkistaa odotetun tuloksen.
assert uusi_terveys == 75, "Terveys laskettiin väärin!"

print("Testi meni läpi!")