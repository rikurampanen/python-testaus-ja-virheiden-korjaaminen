from main import laske_terveys


def test_terveys_vahenee():
    assert laske_terveys(100, 25) == 75

def test_nollavahinko():
    assert laske_terveys(80, 0) == 80

def test_terveys_putoaa_nollaan():
    assert laske_terveys(50, 50) == 0

def test_terveys_ei_mene_negatiiviseksi():
    assert laske_terveys(20, 30) == 0