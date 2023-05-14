# Testausdokumentti

Peliä on testattu automatisoiduin pääosin yksikkötestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

Sillä sovelluksen sovelluslogiikan hoitaa vain yksi luokka, integraatiotestausta ei ole sen erityisemmin tehty.

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa `Matrix`-luokkaa testataan [matrix_test.py -tiedostossa](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/src/tests/matrix_test.py)-testiluokalla. Myös HandleHighscorea ja Colours luokkaa on testattu.

### Testauskattavuus

Ottamatta huomioon User Interface-luokkia, sovelluksen testauksen haarautumakattavuus on 92%

![](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kuvat/coveragereport.png)


## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kayttoohje.md) kuvaamalla tavalla macOS- ja Linux-ympäristössä. 


### Toiminnallisuudet

Melkein kaikki [määrittelydokumentin](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen listaamat sovelluslogiikaan toiminnallisuudet on käyty läpi testauksessa. 

## Jääneet laatuongelmat

Ajan salliessa testejä voisi lisätä vielä. 