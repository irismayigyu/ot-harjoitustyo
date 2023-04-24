# 2048

[2048](https://en.wikipedia.org/wiki/2048_(video_game)). 

## Dokumentaatio

# Muutosloki
[changelog.md](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/changelog.md)

#Tyoaikakirjanpito
[tyoaikakirjanpito.md](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/tyoaikakirjanpito.md)

#Vaatimusmäärittely
[vaatimusmaarittely.md](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/vaatimusmaarittely.md) 

#Pakkauskaavio
[arkkitehtuuri.md](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Riippuvuudet voi asentaa komennolla:

```bash
poetry install
```

2. Sovelluksen käynnistäminen:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suorittaminen komennolla:

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
