def paranna(terveys, maara):
    """Palauttaa pelaajan terveyden parannuksen jälkeen."""
    # Tässä on tarkoituksella virhe:
    # negatiivinen parannusmäärä vähentää terveyttä.
    if maara < 0:
        return terveys + maara

    return terveys + maara


# Testit
assert paranna(50, 20) == 70, "Parantamisen pitäisi lisätä terveyttä."
assert paranna(50, 0) == 50, "Nollamäärän ei pitäisi muuttaa terveyttä."
assert paranna(50, -20) == 50, "Negatiivinen määrä ei saa vähentää terveyttä."

print("Kaikki testit menivät läpi!")