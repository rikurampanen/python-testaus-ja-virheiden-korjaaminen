def vahingoita(terveys, vahinko):
    """Vähentää terveyttä, mutta ei alle nollan."""
    return max(0, terveys - vahinko)


def paranna(terveys, maara):
    """Lisää pelaajan terveyttä."""
    return terveys + maara


def lisaa_kokemusta(kokemus, maara):
    """Lisää pelaajan kokemuspisteitä."""
    return kokemus + maara


def laske_taso(kokemus):
    """Laskee pelaajan tason kokemuspisteiden perusteella."""
    if kokemus >= 200:
        return 3
    elif kokemus >= 100:
        return 2
    else:
        return 1