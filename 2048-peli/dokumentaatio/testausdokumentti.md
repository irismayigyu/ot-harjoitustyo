# Testausdokumentti

Peliä on testattu automatisoiduin pääosin yksikkötestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

Sillä sovelluksen sovelluslogiikan hoitaa vain yksi luokka, integraatiotestausta ei ole sen erityisemmin tehty.

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa `Matrix`-luokkaa testataan [matrix_test.py -tiedostossa](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/src/tests/matrix_test.py)-testiluokalla.

### Testauskattavuus

Ottamatta huomioon User Interface-luokkia, sovelluksen testauksen haarautumakattavuus on 93%

![](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kuvakaappaukset/coveragereport.png)


Testaamatta jäivät _build.py_- ja _initialize\_database.py_-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle. Lisäksi testaatamatta jäivät mm. tilanteet, joissa haetaan kirjautumattoman käyttäjän tekemättömät tehtävät ja uloskirjautuminen.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/kayttoohje.md) kuvaamalla tavalla macOS- ja Linux-ympäristössä. 


### Toiminnallisuudet

Melkein kaikki [määrittelydokumentin](https://github.com/irismayigyu/ot-harjoitustyo/blob/master/2048-peli/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen listaamat sovelluslogiikaan toiminnallisuudet on käyty läpi testauksessa. 

## Jääneet laatuongelmat

keksi jotai...