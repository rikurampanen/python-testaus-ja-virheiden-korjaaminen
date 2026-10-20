def laske_terveys(terveys, vahinko):
    """Laskee pelaajan terveyden vahingon jälkeen."""
    # Tässä on tarkoituksella virhe.
    return terveys + vahinko


# Testit
assert laske_terveys(100, 25) == 75, "Tavallinen vahinko laskettiin väärin."
assert laske_terveys(80, 0) == 80, "Nollavahingon ei pitäisi muuttaa terveyttä."
assert laske_terveys(50, 50) == 0, "Terveyden pitäisi olla nolla."
assert laske_terveys(20, 30) == 0, "Terveys ei saa mennä negatiiviseksi."

print("Kaikki testit menivät läpi!")