from main import laske_loppupisteet, laske_kokonaisvahinko


def test_bonus_lisaa_pisteita():
    assert laske_loppupisteet(100, 20) == 120

def test_nollabonus_ei_muuta_pisteita():
    assert laske_loppupisteet(100, 0) == 100

def test_pisteet_voivat_alkaa_nollasta():
    assert laske_loppupisteet(0, 10) == 10

def test_kokonaisvahinko():
    assert laske_kokonaisvahinko(10, 2) == 20

def test_nollavahinko():
    assert laske_kokonaisvahinko(0, 3) == 0