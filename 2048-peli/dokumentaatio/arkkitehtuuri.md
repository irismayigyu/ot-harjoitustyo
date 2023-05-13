


## Rakenne

Koodin simppeli pakkausrakenne on seuraavanlainen:

```mermaid
flowchart LR
    ui <---> services
    ui <---> data
```

## Pakkausrakenne ja tiedostoista lyhyesti

Ui sisältää käyttöliittymän tiedostot grid.py, won.py, start.py ja ending.py. Jokainen kuvaa jotain käyttöliittymän näyttöä sovelluksessa. Grid piirtää pelinäkymän ja ruudukon matrix.py:n mukaisesti, ja kutsuu won.py ja ending.py:n luokkia. Start.py kutsuu grid.py:tä. Ui sisältää piirtämisen sekä sen miten käyttäjä voi käyttää sovellusta. 

Ui:n grid.py:hyn menee myös data-kansion highscore.py, joka sisältää highscoren tekstikansiossa. 

Services-kansion ainoa tiedosto on matrix.py, joka hoitaa yksinään sovelluslogiikan, jota grid.py mallintaa.

# Käyttöliittymä

UI sisältää neljä erilaista näkymää:

- Aloitusruutu
- Peliruutu
- Voittoruutu
- Häviämisruutu

Jokainen näistä on toteutettu omana luokkanaan ja ruuduista yksi on aina kerrallaan näkyvänä. Käyttöliittymä on pyritty eristämään sovelluslogiikasta. Se kutsuu services Matrix-luokan metodeja.


## Sovelluslogiikka

Luokka Matrix sisältää koko sovelluslogiikan. Siellä luodaan matriisi, joka kuvaa pelin ruudukkoa. Lisäksi siellä on määritelty miten liikkeet ja yhdistäminen toimivat, milloin ja miten luodaan uusia laattoja sekä milloin pelaaja on voittanut tai hävinnyt pelin.


```mermaid
 classDiagram
      class Matrix{
          grid

      }
```


Esimerkkejä luokan metodeista ovat esim: 


- `movement_up, movement_down, movement_left, movement_right`
- `starting_cubes` ja
- `new_cubes`

## Tiedon pysyväistallennus

Kansio data, sisältää highscore-tiedoston johon tallentuu suurin highscore. Kun viimeisin highscore ylittyy, tiedostoon päivitetään uusin highscore. 

## Luokkakaavio

Alla vielä luokkakaavio ohjelman luokista. (main on funktio omassa tiedostossaan). Colours on luokka, jossa luodaan värivaihtoehdot ja HandleHighscore-luokassa käsitellään datan highscore.py-tiedostoa.

```mermaid
 classDiagram
      Matrix "*" --> "1" Grid
      HandleHighscore "*" --> "1" Grid
      Colours "*" --> "1" Grid
      Grid "*" --> "1" Ending
      Grid "*" --> "1" Won
      Main "*" --> "1" Start
      Start "*" --> "1" Grid
      class Grid{
      }
      class Matrix{

      }
```


```mermaid
 sequenceDiagram
      participant grid
      participant matrix
      grid ->> matrix: movement(up)
      matrix ->> grid: movement_up()
      
```
## Päätoiminnallisuudet

Seuraavaksi esimerkkejä ohjelman päätoiminnallisuuksista sekvenssikaavioina:

### Liike

Sekvenssikaavio kuvaa kun pelaaja on pelinäkymässä ja painaa vasenta arrow-key-näppäintä. Eli Grid-luokan tapahtumien käsittelijä kutsuu Matrix-luokan liikemetodia joka kutsuu apumetodeita luokan sisällä. Matrix ei palauta mitään Grid-luokalle, sillä Grid saa matriisin parametrinä ja sen draw_cubes metodi piirtää sitä koko ajan. 

```mermaid
sequenceDiagram
  actor Player
  participant Grid
  participant Matrix
  Player->>Grid: press left arrow key
  Grid->>Matrix: matrix.movement_left()
  Matrix->>Matrix: get_next_tile_left()
  Matrix->>Matrix: changes_left_and_right()

```

### Voittamistilanne

Sekvenssikaavio kuvaa kun pelaaja on pelinäkymässä ja saavuttaa luvun 2048 painamalla ylös-nappia. Eli liike tehdään matrix-luokassa, joka myös testaa onko voitettu. Jos kyllä, niin kutsutaan restart_game-metodia, joka puolestaan kutsuu Won-luokan metodia. Se nollaa tämän hetkisen ruudukon ja palauttaa tyhjän ruudukon. Sitten Grid kutsuu vielä HandleHighscoren metodia, joka päivittää uuden ennätyksen tiedostoon + palauttaa sen. 

```mermaid
sequenceDiagram
  actor Player
  participant Grid
  participant Matrix
  Player->>Grid: press arrow key up
  Grid->>Matrix: matrix.movement_up()
  Matrix->>Matrix: get_next_tile_up()
  Matrix->>Matrix: changes_up_and_down()
  Grid->>Matrix: matrix.win_checker()
  Matrix-->>Grid: True
  Grid->>Grid: restart_game()
  Grid->>Won: you_won(matrix)
  Won-->>Grid: emptied_matrix
  Grid->>HandleHighscore: update_highscore(2048)
  HandleHighscore-->>Grid: 2048


```

### Värinvaihto

Sekvenssikaavio kuvaa värinvaihtotilannetta, kun pelaaja haluaa valita dark mode-laatat. Pelaajan valittua värin, se asettaa muuttujan dark todeksi. Tämä muuttuja on parametrina Grid-luokan metodille, joka asettaa draw_cubessa käytettäviksi väreiksi tummat värit.

```mermaid
sequenceDiagram
  actor Player
  participant Start
  participant Grid
  Player->>Start: press 2
  Start->>Grid: dark=True
  Grid->>Grid: choose_colour(dark)
  Grid->>Grid: draw_cubes


```

### Muut toiminnallisuudet

Saman tyylinen periaate on sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka päivittää matriisia ja käyttöliittymä piirtää. Esimerkiksi häviämisikkunan logiikka muistuttaa paljon voittamisikkunan toiminnallisuuden logiikkaa.

## Ohjelman rakenteeseen jääneet heikkoudet

### Repository-suunnittelumalli

Ohjelmassa ei ole käytetty Repository-suunnittelumallia. Jatkossa tämä olisi hyvä ottaa käyttöön, jotta tiedon tallentaminen voisi olla laajempaan ja käytännönläheisempää. Jos joku asia muuttuisi jossain tiedostossa, suunnittelumallin ansiosta asioita pystyisi muuttaa paikallisemmin. 