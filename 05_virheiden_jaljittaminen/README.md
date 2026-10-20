# 05 – Virheiden jäljittäminen

## Tavoite

Tässä osassa opit selvittämään, miksi Python-ohjelma ei toimi odotetulla tavalla.

Opit:
- lukemaan Pythonin virheilmoituksia
- käyttämään `print`-tulosteita virheen etsimiseen
- seuraamaan muuttujien arvoja ohjelman suorituksen aikana
- erottamaan syntaksivirheen ja ohjelman toimintaan liittyvän virheen
- korjaamaan virheen ja varmistamaan testien avulla, että korjaus toimii

## 1. Mitä virheiden jäljittäminen tarkoittaa?

Virheiden jäljittäminen tarkoittaa sitä, että selvität järjestelmällisesti, missä ja miksi ohjelma toimii väärin.

Kaikki virheet eivät näytä samalta. Esimerkiksi:
- ohjelma voi pysähtyä virheilmoitukseen
- ohjelma voi suorittaa koodin loppuun mutta laskea väärän tuloksen
- ohjelma voi toimia tavallisilla syötteillä mutta epäonnistua tietyssä tilanteessa

Virheen korjaaminen on helpompaa, kun et arvaa ratkaisua vaan selvität ensin, mitä ohjelmassa tapahtuu.

## 2. Lue virheilmoitus

Python näyttää virheen yhteydessä yleensä tietoa siitä, missä virhe tapahtui ja minkä tyyppisestä virheestä on kyse.

Esimerkiksi:

```python
luku = int("omena")
```

Tämä aiheuttaa `ValueError`-virheen, koska tekstiä `"omena"` ei voi muuntaa kokonaisluvuksi.

Virheilmoituksesta kannattaa etsiä ainakin:
- virheen tyyppi, kuten `ValueError` tai `TypeError`
- tiedoston nimi ja rivinumero
- viimeisellä rivillä oleva kuvaus virheen syystä

Älä tyydy vain katsomaan virheilmoituksen viimeistä sanaa. Lue koko ilmoitus ja tarkista, mitä koodia suoritettiin.

## 3. Selvitä muuttujien arvot

Jos ohjelma ei pysähdy virheeseen mutta tulos on väärä, voit käyttää `print`-komentoa tarkistaaksesi muuttujien arvoja.

Esimerkiksi:

```python
terveys = 100
vahinko = 25

uusi_terveys = terveys + vahinko

print("Terveys ennen vahinkoa:", terveys)
print("Vahinko:", vahinko)
print("Terveys laskun jälkeen:", uusi_terveys)
```

Tuloste:

```text
Terveys ennen vahinkoa: 100
Vahinko: 25
Terveys laskun jälkeen: 125
```

Nyt näet, että ohjelma laskee terveyden väärin. Pelaajan terveyden pitäisi vähentyä, mutta koodi lisää vahingon terveyteen.

Korjaa laskutoimitus:

```python
uusi_terveys = terveys - vahinko
```

Tuloksen pitäisi nyt olla `75`.

## 4. Etsi virhe vaihe vaiheelta

Avaa `main.py` ja suorita ohjelma.

Tiedostossa on tarkoituksella virheellinen laskutoimitus. Ohjelma ei kaadu, mutta sen laskema tulos on väärä.

Etene näin:

1. Suorita ohjelma ja katso tulos.
2. Vertaa tulosta siihen, mitä odotat.
3. Lisää `print`-komentoja, jos et tiedä, missä vaiheessa virhe syntyy.
4. Tarkista muuttujien arvot ennen laskutoimitusta ja sen jälkeen.
5. Etsi kohta, jossa ohjelman toiminta poikkeaa odotetusta.
6. Korjaa virhe.
7. Suorita ohjelma uudelleen.

Tässä harjoituksessa tarkoitus on löytää virhe tutkimalla ohjelman toimintaa, ei vaihtamalla koodia summittaisesti.

## 5. Käytä testiä korjauksen tarkistamiseen

Kun olet löytänyt virheen, voit tarkistaa korjauksen `assert`-testillä.

```python
assert uusi_terveys == 75
```

Testi menee läpi, jos `uusi_terveys` on `75`. Jos tulos on jokin muu, testi epäonnistuu.

Testi ja `print`-komento auttavat eri asioissa:
- `print` näyttää, mitä ohjelman aikana tapahtuu
- `assert` tarkistaa, vastaako tulos odotettua arvoa

Voit käyttää molempia saman virheen tutkimiseen.

## 6. Syntaksivirhe vai väärä tulos?

On tärkeää erottaa kaksi erilaista ongelmaa.

### Syntaksivirhe

Python ei pysty suorittamaan koodia, koska koodi ei noudata Pythonin kirjoitussääntöjä.

Esimerkiksi:

```python
if terveys > 0
    print("Pelaaja on elossa")
```

Riviltä puuttuu kaksoispiste `:`. Python ilmoittaa syntaksivirheestä.

### Toimintavirhe

Ohjelma suoritetaan, mutta se tekee väärän asian.

```python
uusi_terveys = terveys + vahinko
```

Tämä on kelvollista Python-koodia. Virhe on laskutoimituksen logiikassa.

Toimintavirhettä ei aina löydä pelkästä virheilmoituksesta. Siksi tarvitaan tulosten tarkistamista, muuttujien tutkimista ja testejä.

## 7. Muokkaa ohjelmaa

Tee seuraavat tehtävät `main.py`-tiedostoon:

1. Etsi ja korjaa tarkoituksella väärä laskutoimitus.
2. Lisää `print`-komento, joka näyttää terveyden ennen laskua.
3. Lisää `print`-komento, joka näyttää terveyden laskun jälkeen.
4. Lisää `assert`-testi, joka tarkistaa odotetun tuloksen.
5. Muuta laskutoimitus hetkeksi vääräksi ja tarkkaile, mitä tulosteet ja testi kertovat.
6. Palauta oikea laskutoimitus ja suorita ohjelma uudelleen.

Kun olet valmis, poista tarpeettomat virheenetsintätulosteet tai jätä vain sellaiset, joista on ohjelmassa hyötyä.

## 8. Itsenäinen tehtävä: pistevirhe

Seuraava ohjelma laskee pelaajan pisteet:

```python
pisteet = 10
lisapisteet = 5

uudet_pisteet = pisteet - lisapisteet

print("Uudet pisteet:", uudet_pisteet)
```

Ohjelma suoritetaan, mutta tulos ei ole haluttu.

Tee näin:

1. Selvitä, mitä tulosta ohjelmalta pitäisi odottaa.
2. Käytä tulosteita tarkistaaksesi muuttujien arvot.
3. Etsi virhe laskutoimituksesta.
4. Korjaa ohjelma.
5. Lisää `assert`-testi, joka tarkistaa tuloksen.
6. Kokeile ainakin yhtä muuta pistemäärää.

## 9. Tarkistuslista

- [ ] Osaan lukea Pythonin virheilmoitusta.
- [ ] Osaan tarkistaa muuttujien arvoja `print`-komennolla.
- [ ] Osaan etsiä kohdan, jossa ohjelma alkaa toimia väärin.
- [ ] Ymmärrän syntaksivirheen ja toimintavirheen eron.
- [ ] Osaan käyttää `assert`-testiä korjauksen tarkistamiseen.
- [ ] Olen löytänyt ja korjannut tarkoituksellisen virheen.
- [ ] Ohjelma toimii odotetulla tavalla.

## Seuraavaksi

Siirry seuraavaan osaan:

[06 – Testaus pytestillä](../06_pytest/)

[← Osa 4 – Virheelliset syötteet](../04_virheelliset_syotteet/)

[Kurssin etusivu](../README.md)