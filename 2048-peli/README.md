# 2048

Laita tähän linkki release kakkoseen ja viimeiseen.

[Release 1](https://github.com/irismayigyu/ot-harjoitustyo/releases/tag/viikko5)

Pieni retro pastelliversio yksinpeli [2048:stä](https://en.wikipedia.org/wiki/2048_(video_game)) käyttäen pygame-kirjastoa. Pelissä yhdistellään 4x4 ruudukon laattoja keskenään käyttäen nuolinäppäimiä. Tavoite on päästä lukuun 2048. 

## Python-versio

Sovelluksen toimintaa testattu Python-versiolla `3.8`. On siis mahdollista että varsinkin vanhempien Python-versioiden kanssa esiintyy ongelmia. 

## Dokumentaatio

[Muutosloki](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/changelog.md)

[Tyoaikakirjanpito](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/tyoaikakirjanpito.md)

[Vaatimusmäärittely](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/vaatimusmaarittely.md) 

[Pakkauskaavio](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Riippuvuudet voi asentaa komennolla:

```bash
poetry install
```
3. Sovelluksen pitäisi luoda database.sqlite automaattisesti, mutta jos tällaista ei näy data-kansiossa,
sen saa luotua komennolla:

```bash
poetry run invoke build
```

2. Sovelluksen käynnistäminen:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testien suorittaminen onnistuu komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin saa komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```
## HUOM

Tiedoston databasen alustamisen ja yhteydenluonnin suorina lähteinä on käytetty kurssimateriaalia!