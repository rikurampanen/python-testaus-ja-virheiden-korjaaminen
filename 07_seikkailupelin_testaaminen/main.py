def vahingoita(terveys, vahinko):
    """Vähentää pelaajan terveyttä, mutta ei alle nollan."""
    return max(0, terveys - vahinko)


def paranna(terveys, maara):
    """Palauttaa pelaajan terveyden parannuksen jälkeen."""
    # Tässä on tarkoituksella virhe.
    return terveys - maara


def lisaa_pisteet(pisteet, lisapisteet):
    """Lisää pelaajan pisteitä."""
    return pisteet + lisapisteet