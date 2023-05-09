# Vaatimusmäärittely 2048-peli
## Sovelluksen tarkoitus
One player game

# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on vuoropohjainen viihdetarkoitukseen oleva peli, jossa käytetään nuolinäppäimiä saavuttaakseen luvun 2048. 

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli eli pelaaja.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä

laita tähän piirros havainnollistamaan.

Sovellus aukeaa aloitusnäkymään, josta on mahdollista siirtyä pelivaiheeseen. Kun pelaaja häviää niin sovellus avaa lopetusnäkymän, josta pääsee takaisin pelivaiheeseen painamalla välilyönti-näppäintä.

## Perusversion tarjoama toiminnallisuus

### Ennen pelin alkamista

- Aloitusnäkymä aukeaa kun ohjelma käynnistetään. 

### Pelin alkamisen jälkeen
- Kun peli alkaa, aloitusruudukko, jossa on kaksi aloituslaattaa satunnaisilla paikoilla, on luotu.
- Jos kaksi laattaa, joilla on sama arvo ovat samalla rivillä/kolumnilla, ilman että välissä on muita laattoja, pelaaja voi yhdistää nämä yhdeksi laataksi, jonka arvo on kaksi kertaa isompi. Jokaisella pelissä mahdollisella arvolla on oma värinsä.
- Riippuen siitä mitä näppäintä pelaaja painaa, ruudut liikkuvat näppäimen suuntaan mahdollisimman reunalle ruudukkoa.
- Yhdistymisen ja liikkumisen jälkeen ruudukkoon luodaan uusi laatta satunnaiselle paikalle. Laatan arvo on yleensä 2, mutta 1/10 ajasta se on 4. Jos pelaaja painaa nuolinäppäimiä, mutta ruudukossa ei tapahdu liikettä niin uutta laattaa ei luoda.
- Peli laskee pelaajan scorea sekä osaa tallettaa highscoren.
- Pelaaja häviää kun ruudukko on täynnä eikä yhdistämisiä voi enää tehdä.
- Lopetusnäkymä avautuu pelaajan hävittyä ja siitä takaisin peliin pääsee painalla välilyöntiä.

## Jatkokehitysideoita
- Player can choose between light mode and dark mode grids.
- Cube pulses when a merge is done. 
