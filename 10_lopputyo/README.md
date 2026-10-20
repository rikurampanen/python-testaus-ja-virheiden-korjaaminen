# Osa 10 – Lopputyö: testattu seikkailupeli

## Tavoite

Tämän lopputyön tarkoituksena on osoittaa, että osaat käyttää kurssilla harjoiteltuja testaus- ja virheenkorjaustaitoja.

Rakennat pienen seikkailupelin toimintalogiikan, jossa pelaajalla on terveyttä, kokemuspisteitä ja taso.

## 1. Tiedostojen rakenne

Luo seuraavat tiedostot:

```text
10_lopputyo/
├── README.md
├── main.py
├── pelitoiminnot.py
└── test_pelitoiminnot.py
```

- `README.md` sisältää tehtävän ohjeet.
- `main.py` käynnistää esimerkkipelin.
- `pelitoiminnot.py` sisältää pelin funktiot.
- `test_pelitoiminnot.py` sisältää automaattiset testit.

## 2. Toteuta pelin toiminnot

Toteuta moduuliin `pelitoiminnot.py` seuraavat funktiot:

### `vahingoita(terveys, vahinko)`

Vähentää terveyttä vahingon verran. Terveys ei saa mennä alle nollan.

Esimerkkejä:
- `vahingoita(100, 25)` palauttaa `75`
- `vahingoita(20, 30)` palauttaa `0`

### `paranna(terveys, maara)`

Lisää terveyttä parannuksen verran.

Esimerkki:
- `paranna(50, 20)` palauttaa `70`

Tässä lopputyössä terveyden ylärajaa ei tarvitse rajoittaa.

### `lisaa_kokemusta(kokemus, maara)`

Lisää kokemuspisteitä.

Esimerkki:
- `lisaa_kokemusta(10, 5)` palauttaa `15`

### `laske_taso(kokemus)`

Palauttaa pelaajan tason kokemuspisteiden perusteella:
- alle 100 kokemuspistettä: taso 1
- vähintään 100 kokemuspistettä: taso 2
- vähintään 200 kokemuspistettä: taso 3

Esimerkkejä:
- `laske_taso(50)` palauttaa `1`
- `laske_taso(100)` palauttaa `2`
- `laske_taso(250)` palauttaa `3`

## 3. Käynnistä ohjelma

Kun olet toteuttanut funktiot, suorita:

```bash
python main.py
```

Ohjelman pitäisi tulostaa pelaajan terveys, kokemuspisteet ja taso.

## 4. Testaa ohjelma

Asenna `pytest`, jos se ei ole jo käytössä:

```bash
python -m pip install pytest
```

Suorita testit:

```bash
python -m pytest -v
```

Kaikkien testien pitäisi mennä läpi.

## 5. Laajenna testejä

Lisää vähintään kolme omaa testiä. Voit testata esimerkiksi:
- nollavahinkoa
- nollaparannusta
- kokemuspisteiden lisäämistä nollasta
- tasoa juuri ennen rajaa ja täsmälleen rajan kohdalla

Testaa myös rajatapauksia. Esimerkiksi `laske_taso(99)` pitäisi palauttaa `1`, mutta `laske_taso(100)` pitäisi palauttaa `2`.

## 6. Virheenkorjaushaaste

Tee hetkeksi yhteen funktioon tarkoituksellinen virhe, esimerkiksi muuta terveyden vähentäminen terveyden lisäämiseksi.

1. Suorita testit.
2. Etsi epäonnistunut testi.
3. Selvitä, mikä koodissa on väärin.
4. Korjaa virhe.
5. Suorita testit uudelleen.

Älä muuta testien odotettuja tuloksia vain saadaksesi ne menemään läpi. Testien pitäisi kuvata toiminnon oikeaa tarkoitusta.

## 7. Lopputyön arviointi

Tarkista, että:
- [ ] Kaikki neljä tiedostoa ovat oikeassa kansiossa.
- [ ] Funktiot on toteutettu erikseen ja niillä on kuvaavat nimet.
- [ ] `main.py` tuo funktiot moduulista.
- [ ] Testit testaavat funktioita suoraan.
- [ ] Kaikki testit menevät läpi.
- [ ] Olet lisännyt vähintään kolme omaa testiä.
- [ ] Osaat selittää, miten löysit ja korjasit virheen.

## 8. Mitä olet oppinut?

Kurssin aikana olet harjoitellut:
- testien merkitystä
- `assert`-lauseita
- funktioiden testaamista
- virheellisiä syötteitä ja rajatapauksia
- virheilmoitusten lukemista
- `pytest`-kirjaston käyttöä
- moduulien jakamista eri tiedostoihin
- virheiden korjaamista testien avulla

## Kurssin suorittaminen

Onnittelut! Kun olet toteuttanut lopputyön, kirjoittanut omia testejä ja saanut testit läpi, olet harjoitellut Python-ohjelmien testaamisen ja virheenkorjauksen keskeisiä perusteita.

[Edellinen osa: 09 – Virheen korjaaminen](../09_virheen_korjaaminen/README.md)

[Kurssin etusivu](../README.md)