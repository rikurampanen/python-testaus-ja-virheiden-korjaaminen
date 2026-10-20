from pelitoiminnot import (
    vahingoita,
    paranna,
    lisaa_kokemusta,
    laske_taso,
)


def test_vahinko_vahentaa_terveytta():
    assert vahingoita(100, 25) == 75

def test_terveys_ei_mene_negatiiviseksi():
    assert vahingoita(20, 30) == 0

def test_parantaminen_lisaa_terveytta():
    assert paranna(50, 20) == 70

def test_nollaparannus():
    assert paranna(50, 0) == 50

def test_kokemuksen_lisaaminen():
    assert lisaa_kokemusta(10, 5) == 15

def test_kokemuksen_lisaaminen_nollasta():
    assert lisaa_kokemusta(0, 10) == 10

def test_taso_alle_rajan():
    assert laske_taso(99) == 1

def test_taso_rajan_kohdalla():
    assert laske_taso(100) == 2

def test_taso_200_kokemuspisteella():
    assert laske_taso(200) == 3

def test_taso_yli_200_kokemuspisteella():
    assert laske_taso(250) == 3