# Osa 08 – Moduulit Pythonissa

## Tavoite

Tässä osassa opit:

- mitä Python-moduuli tarkoittaa
- miten funktioita siirretään omaan tiedostoon
- miten omasta moduulista tuodaan funktioita `import`-komennolla
- miten moduulin funktioita testataan `pytest`-kirjastolla

## 1. Mitä moduuli tarkoittaa?

Python-moduuli on Python-tiedosto, johon on tallennettu koodia, kuten funktioita ja muuttujia.

Esimerkiksi pelin toimintoja voidaan säilyttää tiedostossa `pelitoiminnot.py`. Varsinainen ohjelma voi käyttää näitä toimintoja tuomalla ne omaan tiedostoonsa.

Näin koodi pysyy helpommin luettavana ja ylläpidettävänä.

## 2. Tiedostojen rakenne

Luo tähän kansioon seuraavat neljä tiedostoa:

```text
08_moduulit/
├── README.md
├── main.py
├── pelitoiminnot.py
└── test_pelitoiminnot.py
```

Tiedostojen tehtävät:

- `README.md` sisältää oppitunnin ohjeet.
- `main.py` käynnistää esimerkkiohjelman.
- `pelitoiminnot.py` sisältää pelin toimintoja.
- `test_pelitoiminnot.py` sisältää automaattiset testit.

## 3. Luo moduuli

Avaa tiedosto `pelitoiminnot.py` ja kirjoita sinne pelin toimintoja, esimerkiksi terveyden vähentäminen, parantaminen ja pisteiden lisääminen.

Python tunnistaa saman kansion moduulin tiedoston nimen perusteella. Päätettä `.py` ei kirjoiteta `import`-komentoon.

## 4. Käytä moduulia

Tiedostossa `main.py` voit tuoda funktiot käyttöön näin:

```python
from pelitoiminnot import vahingoita, paranna, lisaa_pisteet
```

Tämän jälkeen voit kutsua funktioita aivan kuten samassa tiedostossa määriteltyjä funktioita.

## 5. Suorita ohjelma

Avaa terminaali tässä kansiossa ja suorita:

```bash
python main.py
```

Ohjelman pitäisi tulostaa pelaajan terveys ja pisteet ennen toimintojen suorittamista sekä niiden jälkeen.

## 6. Testaa moduuli

Jos `pytest` ei ole vielä asennettuna, asenna se:

```bash
python -m pip install pytest
```

Suorita testit:

```bash
python -m pytest -v
```

Testit tuovat funktiot suoraan moduulista `pelitoiminnot.py`. Niiden ei tarvitse käynnistää koko `main.py`-ohjelmaa.

Jos testi epäonnistuu, tarkista virheilmoituksesta odotettu ja toteutunut tulos.

## 7. Kokeile itse

1. Lisää `pelitoiminnot.py`-tiedostoon funktio `lisaa_kokemusta(kokemus, maara)`, joka palauttaa kokemuspisteiden summan.
2. Tuo funktio `main.py`-tiedostoon ja tulosta sen palauttama arvo.
3. Lisää testitiedostoon testi, joka tarkistaa esimerkiksi, että `lisaa_kokemusta(10, 5)` palauttaa arvon `15`.
4. Suorita testit uudelleen.

## 8. Itsenäinen tehtävä

Lisää moduuliin funktio `onko_eloissa(terveys)`, joka palauttaa `True`, jos terveys on suurempi kuin nolla, ja muuten `False`.

Kirjoita vähintään kaksi testiä:
- yksi tilanteelle, jossa terveys on suurempi kuin nolla
- yksi tilanteelle, jossa terveys on nolla

Suorita testit ja varmista, että ne menevät läpi.

## Tarkistuslista

- [ ] Osaan kertoa, mikä moduuli on.
- [ ] Osaan tuoda funktion toisesta tiedostosta `import`-komennolla.
- [ ] Osaan suorittaa `main.py`-ohjelman.
- [ ] Osaan testata moduulin funktioita `pytest`-kirjastolla.
- [ ] Osaan lisätä moduuliin uuden funktion ja kirjoittaa sille testin.

## Seuraava osa

Seuraavassa osassa 09 harjoittelet virheiden korjaamista testien avulla.

[Edellinen osa: 07 – Seikkailupelin testaaminen](../07_seikkailupelin_testaaminen/README.md)

[Seuraava osa: 09 – Virheen korjaaminen](../09_virheen_korjaaminen/README.md)

[Kurssin etusivu](../README.md)