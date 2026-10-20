from main import vahingoita, paranna, lisaa_pisteet


def test_vahinko_vahentaa_terveytta():
    assert vahingoita(100, 25) == 75

def test_terveys_ei_mene_negatiiviseksi():
    assert vahingoita(20, 30) == 0

def test_parantaminen_lisaa_terveytta():
    assert paranna(50, 20) == 70

def test_nollaparannus_ei_muuta_terveytta():
    assert paranna(50, 0) == 50

def test_pisteiden_lisaaminen():
    assert lisaa_pisteet(10, 5) == 15

def test_nollapisteet():
    assert lisaa_pisteet(0, 0) == 0