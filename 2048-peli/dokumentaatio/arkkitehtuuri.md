
```mermaid
 classDiagram
      Matrix "*" --> "1" Grid
      Grid "*" --> "1" Main
      Colours "*" --> "1" Matrix
      class Grid{
          screen
          colours
          font
          cubes
      }
      class Matrix{
          matrix grid
      }
```


```mermaid
 sequenceDiagram
      participant grid
      participant matrix
      grid ->> matrix: movement(up)
      matrix ->> grid: movement_up()
      
```