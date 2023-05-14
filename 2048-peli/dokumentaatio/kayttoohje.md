# Käyttöohje

Lataa sovelluksen viimeisimmän releasen lähdekoodi. 

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, riippuvuudet voi asentaa komennolla:

```bash
poetry install
```

Nyt voit käynnistää sen komennolla:

```
poetry run invoke start
```

## Aloitus
Sovellus avautuu aloitusnäkymään. 

![](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kuvat/aloitusnaytto.png)

Voit vaihtaa värejä näppäimillä. (Weird-tilesit saat salaisellä näppäimellä. Saat vastauksen kun olet voittanut pelin kerran!) Peliin pääsee painamalla Enter-näppäintä.

## Pelaaminen

Nyt pääset pelaamaan peliä, tarkoitus on siis yhdistää laattoja toisiinsa, tavoitteena luku 2048. Käytä nuolinäppäimiä hallitaksesi laattojen liikettä! 

![](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kuvat/pelinakyma.png)

## Pelin päättyminen

Pelaaja häviää, jos ruudukko on täynnä eikä yhdistyksiä voi enää tehdä. Tällöin sovellukseen avautuu lopetusnäyttö. Toisaalta, jos pelaaja saavuttaa luvun 2048, voittonäyttö aukeaa. Paina välilyönti-näppäintä aloittaaksesi uuden pelin. 

![](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kuvat/lopetusnaytto.png)

Nyt peli palaa takaisin pelaamisnäkymään. Sovelluksesta pääsee pois painamalla ruksia! 
