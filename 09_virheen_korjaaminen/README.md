# Osa 09 – Virheen korjaaminen testien avulla

## Tavoite

Tässä osassa opit:

- löytämään ohjelmasta virheen testien avulla
- lukemaan `pytest`-virheilmoitusta
- korjaamaan virheen muuttamatta testejä vain niiden läpäisemiseksi
- varmistamaan korjauksen suorittamalla testit uudelleen

## 1. Miksi testit auttavat virheiden korjaamisessa?

Ohjelma voi näyttää toimivan oikein, vaikka jokin laskutoimitus olisi väärä. Automaattinen testi vertaa ohjelman tulosta odotettuun tulokseen.

Kun testi epäonnistuu, se kertoo, mitä toimintoa testattiin ja mikä tulos saatiin odotetun tuloksen sijaan.

## 2. Tiedostojen rakenne

Luo tähän kansioon:

```text
09_virheen_korjaaminen/
├── README.md
├── main.py
└── test_main.py
```

## 3. Suorita testit ennen korjaamista

Jos `pytest` ei ole asennettuna, suorita:

```bash
python -m pip install pytest
```

Käynnistä testit komennolla:

```bash
python -m pytest -v
```

Ainakin yhden testin pitäisi epäonnistua, koska `main.py` sisältää tarkoituksellisen virheen.

Lue virheilmoituksesta:
- minkä testin suoritus epäonnistui
- mitä arvoa testi odotti
- minkä arvon funktio palautti

Älä muuta testin odotettua tulosta vain siksi, että testi menisi läpi. Selvitä ensin, mikä tulos on toiminnan kannalta oikein.

## 4. Etsi virhe

Avaa `main.py` ja etsi funktio `laske_loppupisteet`.

Vertaa funktion toimintaa testitiedoston odotuksiin.

Kysy itseltäsi:
- Pitäisikö bonuksen lisätä vai vähentää pisteitä?
- Mitä tapahtuu, kun bonus on nolla?
- Mikä olisi oikea tulos esimerkkilaskussa?

## 5. Korjaa ohjelma

Muuta `laske_loppupisteet`-funktion toteutusta niin, että se vastaa sen tarkoitusta ja testien odotuksia.

Kun olet tehnyt korjauksen, suorita testit uudelleen:

```bash
python -m pytest -v
```

Tavoitteena on, että kaikki testit menevät läpi.

## 6. Kokeile itse

Lisää testitiedostoon testi, jossa alkuperäiset pisteet ovat `0` ja bonus `10`.

Mieti ensin odotettu tulos ja kirjoita sitten testi.

Suorita testit uudelleen.

## 7. Itsenäinen tehtävä

Lisää `main.py`-tiedostoon funktio `laske_kokonaisvahinko(vahinko, kerroin)`, joka palauttaa vahingon ja kertoimen tulon.

Kirjoita `test_main.py`-tiedostoon vähintään kaksi testiä:
- tavallinen laskutoimitus, esimerkiksi `10 * 2 == 20`
- nollavahinko, esimerkiksi `0 * 3 == 0`

Suorita testit ja varmista, että uusi toiminto toimii oikein.

## Tarkistuslista

- [ ] Osaan suorittaa testit `pytest`-kirjastolla.
- [ ] Osaan etsiä epäonnistuneen testin virheilmoituksesta.
- [ ] Osaan verrata odotettua ja toteutunutta tulosta.
- [ ] Osaan korjata ohjelmakoodia testien perusteella.
- [ ] Osaan lisätä uuden testin ja tarkistaa korjauksen.

## Seuraava osa

Seuraavassa osassa 10 teet kurssin lopputyön ja kokoat oppimasi taidot yhteen.

[Edellinen osa: 08 – Moduulit](../08_moduulit/README.md)

[Seuraava osa: 10 – Lopputyö](../10_lopputyo/README.md)

[Kurssin etusivu](../README.md)