# 03 – Funktioiden testaaminen

## Tavoite

Tässä osassa opit testaamaan Python-funktioita.

Opit:
- mitä funktion palauttama arvo tarkoittaa
- miten funktiota testataan `assert`-komennolla
- miksi samaa funktiota kannattaa testata useilla syötteillä
- miten testit auttavat löytämään virheitä funktioista

## 1. Miksi funktioita testataan?

Funktio on koodin osa, joka suorittaa tietyn tehtävän. Funktio voi esimerkiksi laskea pelaajan terveyden vahingon jälkeen.

```python
def laske_terveys(terveys, vahinko):
    return terveys - vahinko
```

Funktiota voidaan kutsua eri arvoilla:

```python
print(laske_terveys(100, 25))
print(laske_terveys(80, 10))
```

Tuloste:

```text
75
70
```

Kun funktio palauttaa arvon `return`-komennolla, arvoa voidaan käyttää muualla ohjelmassa ja tarkistaa testillä.

## 2. Ensimmäinen funktiotesti

Voimme testata funktiota `assert`-komennolla:

```python
def laske_terveys(terveys, vahinko):
    return terveys - vahinko

assert laske_terveys(100, 25) == 75
```

Testi kutsuu funktiota arvoilla `100` ja `25`. Sen jälkeen se tarkistaa, että palautettu arvo on `75`.

Jos funktio palauttaa väärän arvon, testi epäonnistuu ja Python näyttää virheilmoituksen.

Jos testi menee läpi, Python jatkaa ohjelman suorittamista.

## 3. Testaa useita tilanteita

Yksi testi ei riitä varmistamaan, että funktio toimii kaikissa tavallisissa tilanteissa.

Voimme kirjoittaa useita testejä:

```python
assert laske_terveys(100, 25) == 75
assert laske_terveys(80, 0) == 80
assert laske_terveys(50, 50) == 0
```

Testit tarkistavat kolme eri tilannetta:
- pelaaja saa tavallisen määrän vahinkoa
- pelaaja ei saa vahinkoa
- pelaajan terveys putoaa nollaan

Entä jos vahinko on suurempi kuin pelaajan terveys?

```python
print(laske_terveys(20, 30))
```

Nykyinen funktio palauttaa `-10`. Pelissä pelaajan terveyden ei kuitenkaan pitäisi mennä negatiiviseksi.

Tämä on esimerkki tilanteesta, jota kannattaa testata erikseen.

## 4. Etsi ja korjaa virhe

Avaa `main.py` ja suorita ohjelma.

Funktiossa on tarkoituksella virhe: se **lisää vahingon terveyteen vähentämisen sijaan**.

Esimerkiksi ensimmäinen testi odottaa arvoa `75`, mutta virheellinen funktio palauttaa `125`.

Myös muut testit epäonnistuisivat, jos ne suoritettaisiin erikseen. Tavallinen Pythonin `assert` kuitenkin pysäyttää ohjelman ensimmäiseen epäonnistuneeseen testiin. Siksi et välttämättä näe muiden testien tuloksia samalla suorituskerralla.

Etene näin:

1. Suorita ohjelma.
2. Lue virheilmoitus.
3. Vertaa odotettua arvoa funktion palauttamaan arvoon.
4. Etsi virhe funktion laskutoimituksesta.
5. Korjaa funktio.
6. Suorita ohjelma uudelleen.

Tavoitteena ei ole vain saada virheilmoitusta katoamaan. Tavoitteena on ymmärtää, miksi testi epäonnistui ja miten korjaus vaikuttaa ohjelman toimintaan.

## 5. Paranna funktiota

Kun olet korjannut laskutoimituksen, paranna funktiota niin, ettei pelaajan terveys voi mennä negatiiviseksi.

Voit käyttää `max`-funktiota:

```python
def laske_terveys(terveys, vahinko):
    return max(0, terveys - vahinko)
```

`max(0, arvo)` palauttaa näistä kahdesta arvosta suuremman.

Jos terveyden laskettu arvo on esimerkiksi `-10`, funktio palauttaa `0`.

Lisää tai tarkista seuraava testi:

```python
assert laske_terveys(20, 30) == 0
```

Suorita kaikki testit uudelleen.

## 6. Muokkaa ohjelmaa

Tee seuraavat muutokset `main.py`-tiedostoon:

1. Lisää testi, jossa terveys on `1` ja vahinko on `1`.
2. Lisää testi, jossa terveys on `100` ja vahinko on `100`.
3. Lisää testi, jossa vahinko on `0`.
4. Kokeile muuttaa funktion laskutoimitus hetkeksi vääräksi.
5. Suorita ohjelma ja katso, miten testi paljastaa virheen.
6. Palauta oikea toteutus ja varmista, että kaikki testit menevät läpi.

Muista, että testit ovat hyödyllisiä myös silloin, kun ohjelma näyttää toimivan. Ne tarkistavat, että ohjelman toiminta vastaa odotuksia.

## 7. Itsenäinen tehtävä: pisteiden laskeminen

Kirjoita funktio `laske_pisteet(pisteet, lisapisteet)`, joka palauttaa pisteiden summan.

Esimerkiksi:

```python
def laske_pisteet(pisteet, lisapisteet):
    return pisteet + lisapisteet

assert laske_pisteet(10, 5) == 15
```

Tee vähintään neljä testiä. Testaa esimerkiksi:
- tavallista pisteiden lisäämistä
- nollan lisäämistä
- suuria pistemääriä
- tilannetta, jossa molemmat arvot ovat nollia

Varmista, että testit kutsuvat omaa funktiotasi eivätkä vain tarkista irrallisia laskutoimituksia.

## 8. Tarkistuslista

- [ ] Osaan kirjoittaa funktion, joka palauttaa arvon.
- [ ] Osaan testata funktion `assert`-komennolla.
- [ ] Osaan testata samaa funktiota useilla syötteillä.
- [ ] Ymmärrän, miksi reunatapauksia kannattaa testata.
- [ ] Ymmärrän, että `assert` pysäyttää ohjelman ensimmäiseen epäonnistuneeseen testiin.
- [ ] Olen löytänyt ja korjannut tarkoituksellisen virheen.
- [ ] Kaikki testit menevät läpi.

## Seuraavaksi

Siirry seuraavaan osaan:

[04 – Virheelliset syötteet](../04_virheelliset_syotteet/)

[← Osa 2 – Ensimmäiset testit](../02_ensimmaiset_testit/)

[Kurssin etusivu](../README.md)