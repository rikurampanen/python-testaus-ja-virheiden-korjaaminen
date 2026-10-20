# 01 – Miksi ohjelmia testataan?

Tervetuloa Python-testauksen ja virheiden korjaamisen kurssille!

Tällä kurssilla opit selvittämään, toimiiko ohjelma odotetulla tavalla. Opit myös löytämään virheitä, korjaamaan niitä ja varmistamaan, että tekemäsi muutokset toimivat.

Tässä ensimmäisessä osassa tutustut siihen, miksi ohjelmia testataan. Et tarvitse vielä erillisiä testauskirjastoja. Käytämme yhtä Python-tiedostoa, jota muokkaat harjoitusten aikana.

## Tavoite

Tämän osan jälkeen osaat:

- selittää, miksi ohjelmia testataan
- erottaa ohjelman suorittamisen sen toiminnan testaamisesta
- tunnistaa tilanteen, jossa ohjelma suorittuu mutta antaa väärän tuloksen
- muuttaa ohjelmaa ja tarkistaa muutoksen vaikutuksen
- selittää, miksi samaa ohjelmaa kannattaa kokeilla useilla eri arvoilla.

## 1. Mikä on ohjelmistotesti?

Ohjelmistotestauksessa tarkistetaan, toimiiko ohjelma odotetulla tavalla.

Kuvitellaan, että rakennat seikkailupeliä. Pelaajan terveys on aluksi 100 pistettä. Hirviön hyökkäys aiheuttaa 25 pistettä vahinkoa.

Pelaajan terveyden pitäisi tällöin olla 75 pistettä.

Ohjelma voi kuitenkin sisältää virheen, jonka vuoksi terveys kasvaa vahingon seurauksena. Python ei välttämättä ilmoita tästä mitään, koska laskutoimitus itsessään on sallittu.

Tässä on tärkeä ero:

- **Suorittaminen:** ohjelma käynnistyy ja suorittaa koodinsa.
- **Testaaminen:** tarkistamme, vastaako ohjelman toiminta odotuksiamme.

Ohjelma voi siis suorittua onnistuneesti ja silti toimia väärin.

## 2. Suorita ensimmäinen ohjelma

Avaa tämän kansion `main.py` ja suorita se.

```python
terveys = 100
vahinko = 25

terveys = terveys + vahinko

print("Pelaajan terveys:", terveys)
```

Ohjelma tulostaa:

```text
Pelaajan terveys: 125
```

Pohdi ennen jatkamista:

- Miksi ohjelma tulostaa 125?
- Tuliko Pythonilta virheilmoitusta?
- Onko tulos pelin sääntöjen mukainen?

Ohjelma laskee oikein sen, mitä koodissa pyydetään. Ongelma on siinä, että olemme kirjoittaneet väärän laskutoimituksen.

## 3. Korjaa laskuvirhe

Muuta `main.py`-tiedoston laskuriviä.

Alkuperäinen rivi:

```python
terveys = terveys + vahinko
```

Korjattu rivi:

```python
terveys = terveys - vahinko
```

Suorita ohjelma uudelleen.

Odotettu tulos:

```text
Pelaajan terveys: 75
```

Nyt ohjelma toimii tämän tilanteen osalta oikein.

Huomaa kuitenkin, että yhden tilanteen toimivuus ei vielä takaa, että ohjelma toimii kaikissa tilanteissa.

## 4. Kokeile erilaisia arvoja

Testauksessa kannattaa tutkia tavallisten tilanteiden lisäksi myös tilanteita, joissa arvot ovat poikkeuksellisia.

Muuta `main.py`-tiedoston arvoja ja suorita ohjelma jokaisen muutoksen jälkeen.

| Terveys | Vahinko | Odotettu terveys |
|---:|---:|---:|
| 100 | 25 | 75 |
| 80 | 0 | 80 |
| 50 | 50 | 0 |
| 20 | 30 | Ei alle nollan, jos pelin sääntö niin määrää |

Viimeinen tilanne paljastaa uuden ongelman. Pelkkä vähennyslasku tuottaa arvon -10, vaikka haluaisimme terveyden pysyvän vähintään nollassa.

Korjaa ohjelma niin, ettei terveys laske alle nollan.

Vinkki: voit käyttää `max()`-funktiota:

```python
terveys = max(0, terveys - vahinko)
```

Kokeile ratkaisua eri arvoilla ja tarkista tulokset.

## 5. Miksi testaus on tärkeää?

Kun ohjelma kasvaa, yhden muutoksen vaikutukset voivat näkyä muuallakin ohjelmassa. Seikkailupelissä virhe terveyslaskennassa voi vaikuttaa taisteluihin, pelaajan kuolemaan ja pelin etenemiseen.

Testauksen avulla voidaan:

- löytää virheitä ennen kuin ne aiheuttavat lisää ongelmia
- tarkistaa, että ohjelma toteuttaa pelin säännöt
- varmistaa, että uudet muutokset eivät riko aiemmin toimineita ominaisuuksia
- saada varmuutta ohjelman toiminnasta.

Testit eivät takaa, että ohjelma on täysin virheetön. Ne auttavat tarkistamaan ne tilanteet, joita olemme päättäneet testata.

## 6. Itsenäinen harjoitus

Tee kaikki tehtävät samassa `main.py`-tiedostossa.

1. Aseta pelaajan terveydeksi 80.
2. Aseta vahingoksi 15.
3. Laske pelaajan jäljelle jäävä terveys.
4. Varmista, ettei terveys laske alle nollan.
5. Tulosta lopputulos.

Kokeile sen jälkeen seuraavia tilanteita:

- terveys 80 ja vahinko 0
- terveys 80 ja vahinko 20
- terveys 20 ja vahinko 30.

Kirjaa jokaisessa tilanteessa ensin odottamasi tulos ja vertaa sitä ohjelman tulosteeseen.

### Lisähaaste

Kokeile, mitä tapahtuu, jos vahingon arvoksi asetetaan -10.

Onko negatiivinen vahinko järkevä pelin sääntöjen kannalta? Miten ohjelman pitäisi käsitellä tällainen tilanne?

Tässä vaiheessa sinun ei tarvitse ratkaista kaikkia mahdollisia virhetilanteita. Tärkeintä on oppia tunnistamaan ne ja pohtimaan, millaista toimintaa ohjelmalta odotetaan.

## 7. Mitä opit?

Tässä osassa opit, että ohjelman suorittuminen ilman virheilmoitusta ei takaa oikeaa tulosta. Opit myös kokeilemaan erilaisia arvoja, tunnistamaan laskuvirheitä ja korjaamaan ohjelman toimintaa.

Seuraavassa osassa kirjoitat ensimmäiset varsinaiset tarkistukset Pythonin `assert`-lauseella. Sen avulla ohjelma voi tarkistaa, vastaako tulos odotettua arvoa.

## Osa on valmis, kun…

- [ ] Osaan selittää, miksi ohjelmia testataan.
- [ ] Ymmärrän eron ohjelman suorittamisen ja testaamisen välillä.
- [ ] Olen suorittanut `main.py`-tiedoston.
- [ ] Olen löytänyt ja korjannut laskuvirheen.
- [ ] Olen kokeillut ohjelmaa useilla eri arvoilla.
- [ ] Olen varmistanut, ettei terveys laske alle nollan.
- [ ] Olen tehnyt itsenäisen harjoituksen.

## Seuraavaksi

[Seuraava osa: 02 – Ensimmäiset testit](../02_ensimmaiset_testit/)

[← Kurssin etusivulle](../README.md)