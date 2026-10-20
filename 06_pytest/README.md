# 06 – Testaus pytestillä

## Tavoite

Tässä osassa opit käyttämään `pytest`-kirjastoa Python-ohjelmien testaamiseen.

Opit:
- mikä `pytest` on ja miksi sitä käytetään
- miten testit erotetaan ohjelman omasta koodista
- miten kirjoitetaan pytest-testifunktio
- miten testit suoritetaan terminaalissa
- miten testien tuloksia luetaan ja virheitä korjataan

## 1. Mikä pytest on?

Olemme tähän asti käyttäneet Pythonin omaa `assert`-komentoa testien tekemiseen.

Esimerkiksi:

```python
assert 10 + 5 == 15
```

Kun ohjelmassa on useita testejä, niiden ylläpitäminen samassa tiedostossa varsinaisen ohjelman kanssa voi muuttua hankalaksi.

`pytest` on Pythonin testauskirjasto, jonka avulla testit voidaan kirjoittaa erilliseen tiedostoon ja suorittaa keskitetysti.

Se tunnistaa tavallisesti testitiedostot, joiden nimet alkavat `test_`-tekstillä, sekä testifunktiot, joiden nimet alkavat `test_`-tekstillä.

## 2. Asenna pytest

Ennen ensimmäistä suoritusta pytest pitää asentaa.

Avaa terminaali kurssin projektikansiossa ja suorita:

```bash
python -m pip install pytest
```

Jos tietokoneellasi käytetään komentoa `python3`, voit kokeilla:

```bash
python3 -m pip install pytest
```

Asennusta ei tarvitse tehdä uudelleen jokaisella testien suorituskerralla.

Voit tarkistaa asennuksen komennolla:

```bash
python -m pytest --version
```

Jos komento näyttää pytest-version, asennus onnistui.

## 3. Ohjelma omaan tiedostoon

Avaa `main.py`. Siinä on funktio, joka laskee pelaajan terveyden vahingon jälkeen.

```python
def laske_terveys(terveys, vahinko):
    return max(0, terveys - vahinko)
```

Funktio palauttaa uuden terveyden. Se ei tulosta tulosta itse, vaan kutsuva koodi voi käyttää palautettua arvoa.

Tämä tekee funktiosta helpon testata.

## 4. Kirjoita ensimmäinen pytest-testi

Avaa `test_main.py`.

Testitiedoston alussa tuodaan testattava funktio ohjelman tiedostosta:

```python
from main import laske_terveys
```

Sen jälkeen kirjoitetaan testifunktio:

```python
def test_terveys_vahenee():
    assert laske_terveys(100, 25) == 75
```

Tässä:
- `test_terveys_vahenee` on testifunktion nimi
- `laske_terveys(100, 25)` kutsuu varsinaista ohjelmaa
- `assert` tarkistaa, että palautettu arvo on 75

Testifunktion nimi alkaa `test_`-tekstillä, jotta pytest tunnistaa sen automaattisesti.

## 5. Suorita testit

Avaa terminaali kansiossa, jossa `main.py` ja `test_main.py` sijaitsevat.

Suorita:

```bash
python -m pytest -v
```

Jos käytät komentoa `python3`, suorita:

```bash
python3 -m pytest -v
```

Valitsin `-v` näyttää testien nimet ja tulokset tarkemmin.

Kun testi onnistuu, näet sen kohdalla `PASSED`. Jos testi epäonnistuu, tuloksena on `FAILED` ja pytest näyttää lisätietoja virheestä.

Pytest suorittaa testit automaattisesti. Sinun ei tarvitse kutsua testifunktioita itse.

## 6. Lisää useita testejä

Yksi testi ei riitä tarkistamaan kaikkia tilanteita.

Lisää `test_main.py`-tiedostoon esimerkiksi nämä testit:

```python
def test_terveys_vahenee():
    assert laske_terveys(100, 25) == 75


def test_nollavahinko():
    assert laske_terveys(80, 0) == 80


def test_terveys_ei_mene_negatiiviseksi():
    assert laske_terveys(20, 30) == 0
```

Muista, että tiedoston alussa pitää olla:

```python
from main import laske_terveys
```

Suorita testit uudelleen:

```bash
python -m pytest -v
```

Nyt pytest näyttää jokaisen testin tuloksen erikseen.

## 7. Kokeile rikkoa ohjelma

Muuta `main.py`-tiedoston funktio hetkeksi vääräksi:

```python
def laske_terveys(terveys, vahinko):
    return terveys + vahinko
```

Suorita testit uudelleen.

Mitä tapahtuu?

Testien pitäisi epäonnistua, koska funktio ei enää palauta odotettuja arvoja.

Palauta tämän jälkeen oikea toteutus:

```python
def laske_terveys(terveys, vahinko):
    return max(0, terveys - vahinko)
```

Suorita testit uudelleen ja varmista, että ne onnistuvat.

Tämä on yksi pytestin eduista: testit ovat erillään varsinaisesta ohjelmasta, ja ne voidaan suorittaa uudelleen aina koodin muuttuessa.

## 8. Muokkaa ohjelmaa

Tee seuraavat tehtävät:

1. Lisää `main.py`-tiedostoon funktio `laske_pisteet(pisteet, lisapisteet)`, joka palauttaa pisteiden summan.
2. Tuo uusi funktio `test_main.py`-tiedostoon.
3. Kirjoita sille vähintään kolme testifunktiota.
4. Suorita testit komennolla `python -m pytest -v`.
5. Muuta pisteiden laskenta hetkeksi vääräksi ja tarkista, että testit löytävät virheen.
6. Korjaa funktio ja suorita testit uudelleen.

Muista: ohjelman toiminta kuuluu `main.py`-tiedostoon ja sitä testaava koodi kuuluu `test_main.py`-tiedostoon.

## 9. Itsenäinen tehtävä

Tee funktio `laske_hinta(maara, yksikkohinta)`, joka palauttaa ostoksen kokonaishinnan.

Esimerkiksi:

```python
assert laske_hinta(3, 2) == 6
```

Kirjoita funktiolle vähintään neljä pytest-testiä. Testaa esimerkiksi:
- tavallista ostosta
- nollan kappaleen ostosta
- yhtä kappaletta
- suurempaa kappalemäärää

Voit itse päättää, miten negatiivisiin arvoihin pitäisi suhtautua. Kirjoita valitsemaasi toimintaa vastaavat testit ja toteutus.

## 10. Tarkistuslista

- [ ] Osaan asentaa pytestin.
- [ ] Ymmärrän, miksi testit ovat omassa tiedostossaan.
- [ ] Osaan kirjoittaa `test_`-alkuisen testifunktion.
- [ ] Osaan tuoda testattavan funktion `main.py`-tiedostosta.
- [ ] Osaan suorittaa testit terminaalissa.
- [ ] Osaan tulkita tulokset `PASSED` ja `FAILED`.
- [ ] Olen rikkonut ohjelman tarkoituksella ja korjannut sen.
- [ ] Kaikki testit menevät läpi.

## Seuraavaksi

Siirry seuraavaan osaan:

[07 – Seikkailupelin testaaminen](../07_seikkailupelin_testaaminen/)

[← Osa 5 – Virheiden jäljittäminen](../05_virheiden_jaljittaminen/)

[Kurssin etusivu](../README.md)