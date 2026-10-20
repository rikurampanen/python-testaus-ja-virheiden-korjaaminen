# Python-testaus ja virheiden korjaaminen

Käytännönläheinen suomenkielinen kurssi, jossa opit testaamaan Python-ohjelmia, löytämään virheitä ja varmistamaan, että tekemäsi korjaukset toimivat.

Kurssilla opit testaamista rakentamalla ja kehittämällä pieniä ohjelmia sekä tekstipohjaista seikkailupeliä. Et pelkästään lue testauksesta, vaan kirjoitat testejä, suoritat niitä, tutkit epäonnistumisia ja korjaat koodia niiden avulla.

Kurssi sopii Pythonin perusteet osaaville aloittelijoille. Aiempi kokemus automaattisesta testauksesta ei ole tarpeen.

## Mitä opit?

Kurssin jälkeen osaat:

- selittää, miksi ohjelmia testataan
- kirjoittaa yksinkertaisia testejä Pythonilla
- testata funktioita erilaisilla syötteillä
- tunnistaa virheelliset syötteet ja rajatapaukset
- lukea Pythonin virheilmoituksia ja jäljittää ongelmien syitä
- käyttää `pytest`-testauskirjastoa
- testata ohjelman toimintoja automaattisesti
- erottaa ohjelman toiminnallisuuden käyttöliittymästä, jotta sitä on helpompi testata
- korjata virheitä ja varmistaa testeillä, ettei sama virhe palaa
- kehittää ohjelmaa hallitusti testien avulla.

## Kurssin sisältö

| Osa | Aihe | Mitä opit? |
|---|---|---|
| 01 | [Miksi ohjelmia testataan?](01_miksi_testataan/) | Testauksen tarkoitus ja virheiden tunnistaminen |
| 02 | [Ensimmäiset testit](02_ensimmaiset_testit/) | `assert` ja odotettujen tulosten tarkistaminen |
| 03 | [Funktioiden testaaminen](03_funktioiden_testaaminen/) | Funktioiden testaaminen eri syötteillä |
| 04 | [Virheelliset syötteet ja rajatapaukset](04_virheelliset_syotteet/) | Poikkeustilanteiden ja rajojen testaaminen |
| 05 | [Virheiden jäljittäminen](05_virheiden_jaljittaminen/) | Virheilmoitusten lukeminen ja ongelmien rajaaminen |
| 06 | [Testit pytestillä](06_pytest/) | Testien kirjoittaminen ja suorittaminen pytestillä |
| 07 | [Seikkailupelin testaaminen](07_seikkailupelin_testaaminen/) | Pelin toimintojen testaaminen |
| 08 | [Koodin jakaminen moduuleihin](08_moduulit/) | Testattavan ja selkeän ohjelmarakenteen suunnittelu |
| 09 | [Virheen korjaaminen testin avulla](09_virheen_korjaaminen/) | Testin kirjoittaminen, virheen korjaaminen ja uudelleentestaus |
| 10 | [Lopputyö ja yhteenveto](10_lopputyo/) | Testatun ohjelman rakentaminen ja opitun soveltaminen |

## Miten kurssia käytetään?

Etene osat järjestyksessä. Jokainen osa rakentaa aiemmin opitun päälle.

Kurssin harjoituksissa toistuu sama toimintamalli:

1. **Lue** – tutustu uuteen käsitteeseen ja esimerkkiin.
2. **Kokeile** – suorita koodi tai testi itse.
3. **Muokkaa** – muuta ohjelmaa ja tutki, miten tulos muuttuu.
4. **Riko** – kokeile, mitä tapahtuu, kun ohjelma ei toimi odotetusti.
5. **Korjaa** – etsi virheen syy ja tee tarvittava muutos.
6. **Testaa uudelleen** – varmista, että korjaus toimii.
7. **Arvioi osaamisesi** – käy läpi osan tarkistuslista ennen jatkamista.

Tavoitteena ei ole opetella ulkoa valmiita ratkaisuja. Tärkeintä on oppia tutkimaan ohjelman toimintaa ja perustelemaan, miksi testi onnistuu tai epäonnistuu.

## Mitä tarvitset?

Ennen kurssin aloittamista tarvitset:

- Pythonin asennettuna tietokoneellesi
- koodieditorin, esimerkiksi Visual Studio Coden
- komentorivin tai terminaalin käytön perustaidot
- Pythonin perusteet: muuttujat, ehdot, silmukat ja funktiot.

Kurssilla käytetään Pythonin omaa `assert`-lausetta ja myöhemmin `pytest`-kirjastoa.

Jos Pythonin asentaminen tai ohjelman suorittaminen on vielä vaikeaa, kertaa ensin Python-perusteet.

## Harjoitusprojekti

Kurssin aikana käytetään pieniä esimerkkiohjelmia ja tekstipohjaista seikkailupeliä. Pelin avulla opit testaamaan esimerkiksi:

- pelaajan terveyden ja vahingon laskemista
- käyttäjän valintoihin liittyvää logiikkaa
- pelin sääntöjä ja ehtoja
- virheellisiä tai odottamattomia syötteitä
- ohjelman eri osien toimintaa toisistaan riippumatta.

Aluksi testit ovat pieniä ja yksinkertaisia. Kurssin edetessä opit rakentamaan testejä, jotka auttavat löytämään virheitä ja pitämään ohjelman toimivana muutosten aikana.

**Huomio:** testien tarkoitus ei ole osoittaa, että ohjelma on varmasti virheetön. Niiden avulla tarkistetaan, että ohjelma toimii määritellyissä tilanteissa ja että tunnetut virheet voidaan havaita.

## Kurssin työkalut

### `assert`

Pythonin `assert`-lausetta käytetään tarkistamaan, että jokin ehto toteutuu.

```python
terveys = 100
assert terveys == 100
```

Jos ehto ei toteudu, Python ilmoittaa virheestä. Tämä on yksinkertainen tapa tutustua testauksen perusajatukseen.

### `pytest`

Kurssin myöhemmissä osissa käytetään `pytest`-kirjastoa, jonka avulla testit voidaan järjestää omiin tiedostoihinsa ja suorittaa helposti.

Kun pytest on asennettu, sen voi yleensä asentaa tai päivittää komennolla:

```bash
python -m pip install pytest
```

Testit suoritetaan projektin hakemistossa komennolla:

```bash
python -m pytest
```

Asennus tehdään vain kerran kyseisessä Python-ympäristössä. Kurssin ohjeissa kerrotaan tarkemmin, mihin hakemistoon komennot kirjoitetaan ja miten testien tuloksia tulkitaan.

## Miten tiedät, että opit?

Jokaisessa osassa on harjoituksia ja tarkistuslista. Siirry seuraavaan osaan, kun pystyt omin sanoin selittämään käsiteltävän asian ja olet suorittanut keskeiset tehtävät.

Kurssin lopussa tavoitteena on, että osaat kirjoittaa testejä, tulkita niiden tuloksia, paikantaa yksinkertaisia ohjelmointivirheitä ja varmistaa testien avulla, että korjaukset toimivat.

## Aloita kurssi

Siirry ensimmäiseen osaan:

[**01 – Miksi ohjelmia testataan?**](01_miksi_testataan/)

---

Kurssin tarkoitus on opettaa testaamaan käytännössä. Virhe ei ole epäonnistuminen, vaan mahdollisuus selvittää, miten ohjelma toimii ja miten siitä tehdään luotettavampi.