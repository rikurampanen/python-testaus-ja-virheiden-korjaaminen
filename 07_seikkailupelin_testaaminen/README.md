# 07 – Seikkailupelin testaaminen

## Tavoite

Tässä osassa opit testaamaan pienen seikkailupelin toimintoja `pytest`-kirjastolla.

Opit:
- jakamaan pelin toimintoja testattaviin funktioihin
- testaamaan pelaajan terveyttä ja pisteitä
- testaamaan erilaisia pelitilanteita
- lukemaan epäonnistuneiden testien ilmoituksia
- korjaamaan virheitä testien avulla

## 1. Miksi peliä kannattaa testata?

Seikkailupelissä voi olla monia toimintoja:
- pelaaja saa vahinkoa
- pelaaja palauttaa terveyttään
- pelaaja kerää pisteitä
- pelaaja löytää esineitä

Jos yhden toiminnon koodia muutetaan, se voi aiheuttaa virheitä muualla pelissä.

Testien avulla voidaan tarkistaa, että tärkeät toiminnot toimivat edelleen muutosten jälkeen.

Tässä harjoituksessa rakennamme pienen osan seikkailupelistä. Tarkoitus ei ole vielä tehdä kokonaista peliä, vaan opetella testaamaan sen toimintaa.

## 2. Tee pelin toiminnoista funktioita

Funktio on helpompi testata, kun se saa tarvitsemansa tiedot parametreina ja palauttaa tuloksen `return`-komennolla.

Esimerkiksi pelaajan vahingoittaminen:

```python
def vahingoita(terveys, vahinko):
    return max(0, terveys - vahinko)
```

Ja pisteiden lisääminen:

```python
def lisaa_pisteet(pisteet, lisapisteet):
    return pisteet + lisapisteet
```

Näitä toimintoja voidaan testata ilman, että koko peliä tarvitsee käynnistää.

## 3. Tutustu main.py-tiedostoon

Avaa `main.py`.

Tiedostossa on kolme funktiota:

- `vahingoita` vähentää pelaajan terveyttä
- `paranna` lisää pelaajan terveyttä
- `lisaa_pisteet` lisää pelaajan pisteitä

Yhdessä funktioista on tarkoituksella virhe. Tehtäväsi on löytää ja korjata se testien avulla.

## 4. Suorita testit

Varmista, että `pytest` on asennettu. Siirry terminaalissa tähän kansioon ja suorita:

```bash
python -m pytest -v
```

Jos käytät komentoa `python3`, suorita:

```bash
python3 -m pytest -v
```

Pytest suorittaa `test_main.py`-tiedoston testit.

- `PASSED` tarkoittaa, että testi onnistui.
- `FAILED` tarkoittaa, että testi ei saanut odotettua tulosta.

Lue epäonnistuneen testin ilmoitus. Siitä näet, mikä tarkistus epäonnistui ja millaista tulosta odotettiin.

## 5. Korjaa virhe

Kun löydät epäonnistuneen testin:

1. Selvitä, mitä funktiota testi kutsuu.
2. Vertaa odotettua tulosta funktion palauttamaan tulokseen.
3. Etsi virhe `main.py`-tiedostosta.
4. Korjaa funktio.
5. Suorita kaikki testit uudelleen.

Älä muuta testiä vain siksi, että se menisi läpi. Testin pitäisi kuvata sitä, miten toiminnon kuuluu toimia.

Jos uskot, että testi on väärä, tarkista ensin tehtävän vaatimukset ja perustele muutos.

## 6. Lisää omia testejä

Kun kaikki valmiit testit menevät läpi, lisää vähintään kolme omaa testiä.

Voit kokeilla esimerkiksi:
- vahinko on nolla
- pelaajan terveys putoaa täsmälleen nollaan
- pelaaja saa paljon pisteitä
- parannusmäärä on nolla
- pelaajan terveys ei mene negatiiviseksi

Kirjoita jokainen testi omaksi `test_`-alkuiseksi funktiokseen.

Esimerkiksi:

```python
def test_nollavahinko():
    assert vahingoita(80, 0) == 80
```

Muista tuoda testattava funktio `test_main.py`-tiedoston alussa.

## 7. Itsenäinen tehtävä: avaimen löytäminen

Lisää peliin funktio `loyda_avain(avaimia)`, joka palauttaa avainten uuden määrän, kun pelaaja löytää yhden avaimen.

Esimerkiksi:

```python
assert loyda_avain(0) == 1
assert loyda_avain(2) == 3
```

Tee funktiolle vähintään kolme testiä.

Mieti myös, mitä funktion pitäisi tehdä, jos sille annetaan negatiivinen avainten määrä. Päätä haluttu toiminta ja kirjoita sitä vastaava testi.

## 8. Tarkistuslista

- [ ] Ymmärrän, miksi pelin toimintoja kannattaa testata erikseen.
- [ ] Osaan testata funktioita `pytest`-kirjastolla.
- [ ] Osaan lukea epäonnistuneen testin ilmoituksen.
- [ ] Olen korjannut tarkoituksella tehdyn virheen.
- [ ] Olen lisännyt vähintään kolme omaa testiä.
- [ ] Osaan selittää, mitä testit tarkistavat.
- [ ] Kaikki testit menevät läpi.

## Seuraavaksi

Siirry seuraavaan osaan:

[08 – Moduulit](../08_moduulit/)

[← Osa 6 – Testaus pytestillä](../06_pytest/)

[Kurssin etusivu](../README.md)