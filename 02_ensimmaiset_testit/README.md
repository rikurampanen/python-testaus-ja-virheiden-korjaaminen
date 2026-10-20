# 02 – Ensimmäiset testit

## Tavoite

Tässä osassa opit kirjoittamaan ensimmäisen automaattisen testisi Pythonilla.

Opit:
- mitä `assert` tekee
- miten odotettua tulosta verrataan todelliseen tulokseen
- miten testi kertoo virheestä
- miten ohjelmaa muutetaan niin, että testi menee läpi

Tässä osassa emme vielä käytä `pytest`-kirjastoa. Käytämme Pythonin omaa `assert`-komentoa.

## 1. Mikä on testi?

Testillä tarkistetaan, toimiiko ohjelma odotetulla tavalla.

Oletetaan, että pelissä pelaaja saa vahinkoa. Jos pelaajan terveys on 100 ja vahinko 25, terveyden pitäisi olla 75.

Voimme laskea tuloksen Pythonilla:

```python
terveys = 100
vahinko = 25

uusi_terveys = terveys - vahinko

print(uusi_terveys)
```

Ohjelma tulostaa:

```text
75
```

Mutta entä jos ohjelmaa muutetaan myöhemmin vahingossa väärin? Pelkkä tulosteen katsominen ei automaattisesti kerro, onko tulos oikea.

Voimme tarkistaa tuloksen testillä.

## 2. Ensimmäinen testi: `assert`

`assert` tarkistaa, onko väite tosi.

```python
assert 100 - 25 == 75
```

Jos laskutoimituksen tulos on 75, testi menee läpi eikä Python tulosta mitään.

Jos väite ei ole tosi, Python ilmoittaa virheestä.

Kokeile myös tätä:

```python
assert 100 - 25 == 80
```

Tämä testi epäonnistuu, koska tulos on 75 eikä 80.

**Muista:** Testin ei tarvitse tulostaa sanaa ”onnistui”. Jos `assert` ei aiheuta virhettä, tarkistus meni läpi.

## 3. Testaa omaa ohjelmaa

Avaa tämän kansion `main.py`.

Tiedostossa on pieni ohjelma, joka laskee pelaajan uuden terveyden. Siinä on myös testejä.

Tee näin:

1. Suorita ohjelma.
2. Katso, menevätkö testit läpi.
3. Lue mahdollinen virheilmoitus.
4. Etsi ohjelmasta virhe.
5. Korjaa koodi ja suorita se uudelleen.

Kun testi epäonnistuu, se ei tarkoita, että testaaminen epäonnistui. Testi teki työnsä: se paljasti ongelman.

## 4. Lisää testejä

Yksi testi ei yleensä riitä tarkistamaan kaikkia tilanteita.

Pelaajan terveyden laskemisessa voimme testata esimerkiksi nämä tapaukset:

| Alkuperäinen terveys | Vahinko | Odotettu terveys |
|---:|---:|---:|
| 100 | 25 | 75 |
| 80 | 0 | 80 |
| 50 | 50 | 0 |
| 20 | 30 | 0 |

Viimeinen tapaus vaatii erityistä huomiota: pelaajan terveys ei saa mennä negatiiviseksi.

Voit käyttää testeissä muuttujia:

```python
terveys = 100
vahinko = 25
uusi_terveys = terveys - vahinko

assert uusi_terveys == 75
```

Testi tarkistaa nyt ohjelman laskeman tuloksen, ei pelkästään irrallista laskutoimitusta.

## 5. Kokeile rikkoa ohjelma

Muuta `main.py`-tiedoston terveyden laskemista hetkeksi vääräksi.

Esimerkiksi:

```python
uusi_terveys = terveys + vahinko
```

Suorita ohjelma uudelleen.

Mitä tapahtuu? Testin pitäisi ilmoittaa, että odotettu tulos ei täsmää todellisen tuloksen kanssa.

Palauta laskutoimitus oikeaksi ja varmista, että testi menee jälleen läpi.

## 6. Muokkaa ohjelmaa

Tee seuraavat muutokset itse:

1. Lisää testi tilanteelle, jossa vahinko on 0.
2. Lisää testi tilanteelle, jossa pelaajan terveys putoaa täsmälleen nollaan.
3. Lisää tarkistus, joka varmistaa, ettei terveys koskaan mene negatiiviseksi.
4. Kokeile muuttaa ohjelmaa niin, että jokin testi epäonnistuu. Korjaa sitten virhe.

Vinkki: voit estää negatiivisen terveyden näin:

```python
uusi_terveys = max(0, terveys - vahinko)
```

## 7. Itsenäinen tehtävä

Kirjoita pieni pisteiden laskentaohjelma.

Ohjelma saa alkuperäiset pisteet ja lisättävät pisteet. Sen pitää laskea uusi pistemäärä ja testata tulos `assert`-komennolla.

Esimerkiksi:

- alkuperäiset pisteet: 10
- lisäpisteet: 5
- odotettu tulos: 15

Lisää vähintään kolme testiä eri arvoilla. Varmista, että testit tarkistavat ohjelman laskeman tuloksen.

## 8. Tarkistuslista

- [ ] Ymmärrän, mitä `assert` tekee.
- [ ] Osaan tarkistaa odotetun tuloksen.
- [ ] Tiedän, miltä epäonnistunut testi näyttää.
- [ ] Osaan lisätä ohjelmaan uusia testejä.
- [ ] Olen kokeillut rikkoa ohjelman ja korjata sen.
- [ ] Kaikki testit menevät läpi.

## Seuraavaksi

Siirry seuraavaan osaan:

[03 – Funktioiden testaaminen](../03_funktioiden_testaaminen/)

[← Osa 1 – Miksi ohjelmia testataan?](../01_miksi_testataan/)

[Kurssin etusivu](../README.md)