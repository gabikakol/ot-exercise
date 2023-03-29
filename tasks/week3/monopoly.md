```mermaid
 classDiagram
      Monopoly_game "1" -- "2-8" Player 
      Monopoly_game "1" --> "2" Dice
      Monopoly_game "1" -- "1" Board
      Board "1" -- "40" Tiles
      Tiles "1" --> "1" Next_tile
      Player "1" --> "2" Dice
      Dice "2" --> "1" Pawn
      Pawn "1" --> "1" Tiles
      
```
