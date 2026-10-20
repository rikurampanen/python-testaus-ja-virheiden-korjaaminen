# 04 – Virheelliset syötteet

## Tavoite

Tässä osassa opit käsittelemään tilanteita, joissa ohjelma saa odottamattoman tai virheellisen syötteen.

Opit:
- mitä virheellinen syöte tarkoittaa
- miksi ohjelman ei pidä luottaa kaikkiin käyttäjän antamiin arvoihin
- miten syötteitä tarkistetaan `if`-ehdoilla
- miten `assert`-testeillä tarkistetaan myös virhetilanteita
- miten ohjelmaa parannetaan vaiheittain

## 1. Kaikki syötteet eivät ole kelvollisia

Kuvitellaan, että seikkailupelin pelaaja voi käyttää parannusjuomaa. Juoma palauttaa pelaajalle terveyspisteitä.

```python
def paranna(terveys, maara):
    return terveys + maara
```

Tämä toimii tavallisilla arvoilla:

```python
print(paranna(50, 20))
```

Tuloste:

```text
70
```

Mutta mitä tapahtuu, jos parannusmäärä on negatiivinen?

```python
print(paranna(50, -20))
```

Tulos on `30`. Ohjelma ei kaadu, mutta toiminta ei ehkä vastaa sitä, mitä parantamiselta odotamme.

Entä jos terveys tai parannusmäärä on tekstimuodossa, esimerkiksi `"paljon"`? Tällöin yhteenlasku voi aiheuttaa virheen, jos yritämme yhdistää luvun ja tekstin.

Ohjelman suunnittelijan pitää päättää, mitkä syötteet ovat sallittuja ja miten virheellisiin syötteisiin reagoidaan.

## 2. Tarkista syötteen arvo

Voimme tarkistaa `if`-ehdolla, ettei parannusmäärä ole negatiivinen.

```python
def paranna(terveys, maara):
    if maara < 0:
        return terveys

    return terveys + maara
```

Nyt negatiivinen parannusmäärä ei muuta terveyttä.

Kokeile:

```python
print(paranna(50, 20))
print(paranna(50, -20))
```

Tuloste:

```text
70
50
```

Tämä on yksi mahdollinen ratkaisu. Toisessa ohjelmassa negatiivinen arvo voisi olla syy ilmoittaa virheestä. Ratkaisu riippuu siitä, mitä ohjelman halutaan tekevän.

## 3. Testaa myös virheellisiä arvoja

Testien ei pidä tarkistaa vain tavallisia tilanteita. Niiden kannattaa tarkistaa myös rajatapaukset ja virheelliset arvot.

Esimerkiksi:

```python
assert paranna(50, 20) == 70
assert paranna(50, 0) == 50
assert paranna(50, -20) == 50
```

Nämä testit tarkistavat tavallisen parantamisen, nollan käyttämisen ja negatiivisen parannusmäärän.

Testi on tärkeä myös silloin, kun ohjelma toimii odotetusti tavallisilla arvoilla. Virheellinen syöte voi paljastaa ongelman, jota ei muuten huomattaisi.

## 4. Etsi ja korjaa virhe

Avaa `main.py` ja suorita ohjelma.

Tiedostossa on tarkoituksella virheellinen toteutus. Negatiivinen parannusmäärä vähentää terveyttä, vaikka sen pitäisi tässä harjoituksessa jättää terveys ennalleen.

Etene näin:

1. Suorita ohjelma.
2. Katso tuloste ja testien virheilmoitukset.
3. Selvitä, mikä testi epäonnistuu.
4. Muokkaa funktiota niin, ettei negatiivinen parannusmäärä muuta terveyttä.
5. Suorita ohjelma uudelleen.
6. Varmista, että kaikki testit menevät läpi.

Pythonin tavallinen `assert` pysäyttää ohjelman ensimmäiseen epäonnistuneeseen testiin. Jos testi epäonnistuu, lue virheilmoitus ja korjaa ongelma ennen uutta suoritusta.

## 5. Entä jos syöte on tekstiä?

Jos ohjelma pyytää käyttäjältä numeroa `input`-komennolla, saatu arvo on tekstiä.

```python
maara = input("Kuinka monta terveyspistettä palautetaan? ")
```

Vaikka käyttäjä kirjoittaisi `20`, muuttujan `maara` arvo on merkkijono `"20"`.

Voit yrittää muuntaa sen kokonaisluvuksi:

```python
maara = int(input("Kuinka monta terveyspistettä palautetaan? "))
```

Jos käyttäjä kirjoittaa esimerkiksi `paljon`, muunnos aiheuttaa `ValueError`-virheen.

Voimme käsitellä tilanteen `try`- ja `except`-rakenteella:

```python
try:
    maara = int(input("Kuinka monta terveyspistettä palautetaan? "))
    print("Parannusmäärä:", maara)
except ValueError:
    print("Anna määrä numerona.")
```

Nyt ohjelma näyttää ymmärrettävän viestin, jos syötettä ei voi muuntaa kokonaisluvuksi.

Tässä osassa tärkeintä on ymmärtää, että syötteitä voidaan tarkistaa sekä ennen laskutoimitusta että mahdollisen virheen yhteydessä.

## 6. Muokkaa ohjelmaa

Tee seuraavat tehtävät `main.py`-tiedostoon:

1. Korjaa negatiivisen parannusmäärän käsittely.
2. Lisää testi, jossa parannusmäärä on `0`.
3. Lisää testi, jossa parannusmäärä on `1`.
4. Lisää testi, jossa parannusmäärä on negatiivinen.
5. Kokeile muuttaa funktiota niin, että yksi testi epäonnistuu.
6. Palauta oikea toteutus ja suorita testit uudelleen.

Lisätehtävä: kirjoita pieni `try`–`except`-ohjelma, joka pyytää käyttäjältä kokonaislukua ja näyttää virheilmoituksen, jos käyttäjä kirjoittaa muuta kuin kelvollisen kokonaisluvun.

## 7. Itsenäinen tehtävä: juomakauppa

Tee funktio `osta_juomia(maara)`, joka laskee juomien hinnan. Yhden juoman hinta on 3 euroa.

Päätä, miten ohjelma toimii, jos määrä on negatiivinen. Tässä harjoituksessa negatiivinen määrä palauttaa arvon `0`.

Esimerkkejä:

```python
assert osta_juomia(2) == 6
assert osta_juomia(0) == 0
assert osta_juomia(-1) == 0
```

Tee funktio ja lisää vähintään yksi oma testi.

Muista: testaa funktion palauttamaa arvoa, älä pelkästään tulostetta.

## 8. Tarkistuslista

- [ ] Ymmärrän, mitä virheellinen syöte tarkoittaa.
- [ ] Osaan tarkistaa arvoja `if`-ehdolla.
- [ ] Osaan testata myös rajatapauksia.
- [ ] Ymmärrän, miksi tekstin muuntaminen numeroksi voi epäonnistua.
- [ ] Tiedän, mihin `try`- ja `except`-rakennetta käytetään.
- [ ] Olen korjannut tarkoituksellisen virheen.
- [ ] Kaikki testit menevät läpi.

## Seuraavaksi

Siirry seuraavaan osaan:

[05 – Virheiden jäljittäminen](../05_virheiden_jaljittaminen/)

[← Osa 3 – Funktioiden testaaminen](../03_funktioiden_testaaminen/)

[Kurssin etusivu](../README.md)