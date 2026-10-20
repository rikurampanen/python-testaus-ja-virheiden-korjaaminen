def laske_terveys(terveys, vahinko):
    """Laskee pelaajan terveyden vahingon jälkeen."""
    return max(0, terveys - vahinko)